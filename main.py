from components.resume_entry import ResumeUploader
import streamlit as st
from src.greetings import end_conversation,start_greeting
from components.manual_entry import EnterManually
from src.feedback import feed_back
from src.home_page import home_ui, about_me


# run_main()
import streamlit as st
from streamlit_option_menu import option_menu
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Resume Uploader", "Manual Enter","About Me"],
        icons=["house", "app-indicator", "bar-chart","person-video" ],
        menu_icon="cast",
        default_index=1,)
if selected == "Home":
    home_ui()
if selected == "Resume Uploader":
    resume_uploader = ResumeUploader()
    greets =resume_uploader.resume_upload()
    if greets:
        st.write(greets)
        # feed_back()

if selected == "Manual Enter":
    st.title("TalentScout - Hiring Assistant Chatbot")
    start_greeting()
    enter_manually = EnterManually()
    greets = enter_manually.manual_entry()
    if greets:
        st.write(greets)
        # feed_back()

if selected == "About Me":
    about_me()

