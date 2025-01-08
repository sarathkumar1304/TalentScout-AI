import streamlit as st
from src.resume_parser import ResumeParser
from generate_questions.questions_generator import QuestionGenerator
import google.generativeai as genai
import os
from src.greetings import end_conversation,start_greeting
import json
from src.feedback import feed_back

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

chat = model.start_chat(history=[])
resume_parser = ResumeParser()
questions_generator = QuestionGenerator()


class ResumeUploader:
    def resume_upload(self):
        st.title("TalentScout - Hiring Assistant Chatbot")
        start_greeting()
        st.sidebar.title("Candidate Details")

        if "tech_stack" not in st.session_state:
            st.session_state.tech_stack = []
        if "questions" not in st.session_state:
            st.session_state.questions = {}
        if "answers" not in st.session_state:
            st.session_state.answers = {}

        uploaded_file = st.sidebar.file_uploader("Upload Resume (PDF):", type=["pdf"])
        if uploaded_file:
            candidate_details = resume_parser.parse(uploaded_file)
            st.success("Resume uploaded and processed successfully!")
            st.write("### Candidate Information")
            st.write(f"**Name:** {candidate_details['name']}")
            st.write(f"**Email:** {candidate_details['email']}")
            st.write(f"**Phone:** {candidate_details['phone']}")
            st.write(f"**Experience:** {candidate_details['experience']}")
            st.write(f"**Position:** {candidate_details['position']}")
            st.write(f"**Location:** {candidate_details['location']}")
            st.write(f"**Tech Stack:** {', '.join(candidate_details['tech_stack'])}")
            st.session_state.tech_stack = candidate_details["tech_stack"][:5]

        if st.session_state.tech_stack:
            st.write("**Based on your Top 5 skills ,we generate Technical Question , you need to answer the question .If you are ready  please click Generate Questions button**")
            if st.button("Generate Questions"):
                for tech in st.session_state.tech_stack:
                    tech = tech.strip()
                    if tech not in st.session_state.questions:
                        questions = questions_generator.generate_questions(chat, tech)
                        st.session_state.questions[tech] = questions.split("\n")
                        st.session_state.answers[tech] = [""] * len(st.session_state.questions[tech])

            # Display questions and answers
            if st.session_state.questions:
                for tech, questions in st.session_state.questions.items():
                    st.write(f"### Technical Questions for {tech}")
                    for idx, question in enumerate(questions):
                        st.write(f"{idx + 1}. {question}")
                        st.session_state.answers[tech][idx] = st.text_area(
                            f"Answer for Q{idx + 1} ({tech})",
                            value=st.session_state.answers[tech][idx],
                            key=f"answer_{tech}_{idx}",)

                if st.button("Submit Answers"):
                    # Combine questions and answers into a JSON format
                    greets = end_conversation()
                    st.write(greets)
                    output_data = []
                    for tech, questions in st.session_state.questions.items():
                        for idx, question in enumerate(questions):
                            output_data.append({
                                "tech": tech,
                                "question": question,
                                "answer": st.session_state.answers[tech][idx]
                            })

                    # Save as JSON file
                    json_filename = "questions_answers.json"
                    with open(json_filename, "w") as json_file:
                        json.dump(output_data, json_file, indent=4)
                feed_back()