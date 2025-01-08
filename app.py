import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
import re
import time
import os

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")


chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
)


def generate_questions(chat, tech):
    """Generates 3-5 technical questions for a specific tech item, starting from easy to advanced."""
    prompt = (
        f"You are a technical interviewer. Create 3 to 5 technical interview questions for the technology: {tech}. "
        "Don't mention level of question and just provide the questions directly."
        
    )
    open_ended_response = chat.send_message(prompt, stream=True)
    open_ended_response.resolve()
    open_ended= open_ended_response.text if open_ended_response.text else "Unable to generate open-ended questions."
    # print(open_ended)
    return  open_ended





# Streamlit UI
st.title("TalentScout - Hiring Assistant Chatbot")
st.sidebar.title("Candidate Details")

# Collect Candidate Information
with st.sidebar.form("candidate_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number")
    experience = st.number_input("Years of Experience", min_value=0, step=1)
    position = st.text_input("Desired Position")
    location = st.text_input("Current Location")
    tech_stack = st.text_area("Tech Stack (comma-separated)").split(",")
    submit = st.form_submit_button("Submit")

if submit:
    st.success("Candidate information submitted successfully!")

    # Display Candidate Information
    st.write("### Candidate Information")
    st.write(f"**Name:** {name}")
    st.write(f"**Email:** {email}")
    st.write(f"**Phone:** {phone}")
    st.write(f"**Experience:** {experience} years")
    st.write(f"**Position:** {position}")
    st.write(f"**Location:** {location}")
    st.write(f"**Tech Stack:** {', '.join(tech_stack)}")
    
    

    # Interactive Question and Answer Section
    st.write("### Technical Questions")
    all_answers = []

    if tech_stack:
        for tech in tech_stack:
            tech = tech.strip()
    
            if tech:

                st.write(f"**Questions for {tech}:**")
                questions = generate_questions(chat, tech[:5])
                for idx, question in enumerate(questions.split("\n\n")):
                    st.write(f"{question.strip("\n")}")
                    
                    answer = st.text_area(f"Answer for Q{idx+1} ({tech})", key=f"answer_{tech}_{idx}")
                    all_answers.append({"question": question, "answer": answer})
        # Final Submission Button
        if  st.button("Submit All Answers"):
           
            st.write("### Thank You for Completing the Questions!")
            st.write("We appreciate your time and effort in answering the questions.")
            st.write("Our team will review your responses and get back to you shortly.")
            st.write("Warm regards,\nTalentScout Team")
    else:
        st.error("Please provide a valid tech stack.")

# Exit Conversation
# if st.button("End Conversation"):
#     st.write("Thank you for using TalentScout! Best of luck to the candidates.")
#     st.stop()