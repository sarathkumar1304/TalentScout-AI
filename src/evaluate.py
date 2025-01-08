import google.generativeai as genai
from prompts.prompts import PromptGenerator
from dotenv import load_dotenv
load_dotenv
import os
api_key = os.getenv("GOOGLE_API_KEY")
class AnswerEvaluator:
    def __init__(self, api_key):
        """Initialize with the Gemini API key."""
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-pro")

    def evaluate_answers(self, all_answers):
        """Evaluates answers based on their relevance, accuracy, and clarity."""
        prompt = self._construct_prompt(all_answers)

        try:
            # Evaluate the answers using Gemini's model
            response = self.model.generate_content(
                prompt
            )

            # Return the response generated by the model
            return response.text.strip()

        except Exception as e:
            return f"Error in evaluation: {str(e)}"

    def _construct_prompt(self, all_answers):
        """Constructs a detailed prompt for the Gemini model."""
        prompt = PromptGenerator()
        evaluation_prompt = prompt.evaluate_prompt()

        for idx, item in enumerate(all_answers, 1):
            evaluation_prompt += f"\n{idx}. Question: {item['question']}\n   Answer: {item['answer']}\n"

        evaluation_prompt += "\nProvide your detailed evaluation below:"
        return evaluation_prompt


# Initialize with your Gemini API key
api_key = os.getenv("GOOGLE_API_KEY")
evaluator = AnswerEvaluator(api_key)

# Example answers
all_answers = [
    {"question": "What is machine learning?", "answer": "Machine learning is a subset of AI."},
    {"question": "Explain logistic regression.", "answer": "It is used to classify data points into classes."},
]

# Evaluate the answers
evaluation_result = evaluator.evaluate_answers(all_answers)
print(evaluation_result)