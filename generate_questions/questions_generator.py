import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
import os
from prompts.prompts import PromptGenerator
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")


chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
)

class QuestionGenerator:
    def generate_questions(self,chat, tech):
        """Generates 3-5 technical questions for a specific tech item, starting from easy to advanced."""
        # prompt = (
        #     f"You are a technical interviewer. Create 3 to 5 technical interview questions for the technology: {tech}. "
        #     "Don't mention level of question and just provide the questions directly."
            
        # )
        prompt = PromptGenerator().get_prompts(tech)
        open_ended_response = chat.send_message(prompt, stream=True)
        open_ended_response.resolve()
        open_ended= open_ended_response.text if open_ended_response.text else "Unable to generate open-ended questions."
        # print(open_ended)
        return  open_ended