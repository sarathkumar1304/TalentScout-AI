from src.manual_entry import ManualEntry
import streamlit as st
from generate_questions.questions_generator import QuestionGenerator
import google.generativeai as genai
import os
from src.feedback import feed_back
from src.greetings import end_conversation, home_greetings
import json

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

chat = model.start_chat(history=[])
manual_entry = ManualEntry()
questions_generator= QuestionGenerator()

                            
class EnterManually:
    def manual_entry(self):
        tech_stack = manual_entry.manual_entry_form()
        if tech_stack:
            st.session_state.tech_stack = tech_stack

        if "questions" not in st.session_state:
            st.session_state.questions = {}
        if "answers" not in st.session_state:
            st.session_state.answers = {}

        if st.session_state.tech_stack:
            if st.button("Generate Questions"):
                for tech in st.session_state.tech_stack:
                    if tech.strip() not in st.session_state.questions:
                        questions = questions_generator.generate_questions(chat, tech)
                        st.session_state.questions[tech] = questions.split("\n")
                        st.session_state.answers[tech] = [""] * len(st.session_state.questions[tech])

            if st.session_state.questions:
                for tech, questions in st.session_state.questions.items():
                    st.write(f"### Technical Questions for {tech}")
                    for idx, question in enumerate(questions):
                        st.write(f"{idx + 1}. {question}")
                        st.session_state.answers[tech][idx] = st.text_area(
                            f"Answer for Q{idx + 1} ({tech})",
                            value=st.session_state.answers[tech][idx],
                            key=f"answer_{tech}_{idx}",
                        )

                if st.button("Submit Answers"):
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
        