
import streamlit as st
class PromptGenerator:
    def get_prompts(self, tech):
        
        prompt = (
        f"You are a technical interviewer. Create 3 to 5 technical interview questions for the technology: {tech}. "
        "Don't mention level of question and just provide the questions directly."
        
    )
        return prompt
    def evaluate_prompt(self):
        evaluation_prompt = """
Evaluate each answer based on accuracy, relevance, and clarity. If an answer is provided, assess it; if not, mark it as "No answer provided." After evaluating all answers, return the percentage of valid answers (answers that are accurate, relevant, and clear).
"""
        
        return evaluation_prompt


