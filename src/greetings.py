import streamlit as st

import streamlit as st

def start_greeting():
    # Display a friendly greeting message to the candidate
    st.write("---")
    st.write("### Welcome to the TalentScout Hiring Assistant Chatbot! 🎉")
    
    # Greet the candidate and introduce the purpose of the chatbot
    st.write("Hello and thank you for applying! I'm here to help you through the interview process.")
    st.write("We'll be reviewing your skills and experience through a series of technical questions. Let's get started!")

    # Optionally, you can provide a brief overview of the process
    st.write("You'll have the opportunity to upload your resume or enter your details manually. Then, I'll generate some technical questions based on your expertise.")
    
    # Encourage the candidate to proceed
    st.write("Please select your preferred method to proceed, and we'll take it from there!")

# Call this function to display the greeting message at the beginning
# start_greeting()


def end_conversation():
    # After submitting answers, display a thank you message
    st.write("---")
    end_greetings = """
                ### Thank You for Your Responses!
                Thank you for your time and thoughtful answers. We appreciate your interest in the position!\n
                Our team will review your responses and contact you soon regarding the next steps in the hiring process.\n
                If you have any questions or need further assistance, feel free to reach out!\n
                Good luck and stay positive! 😊
                """
    return end_greetings

def home_greetings():
    st.write("Home page")
