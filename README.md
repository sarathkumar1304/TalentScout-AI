# TalentScout-AI

TalentScout-AI is an AI-powered hiring assistant chatbot designed to streamline the recruitment process. It enables users to upload resumes or manually enter technical skills, automatically generates relevant technical questions, collects responses, and exports the data in a structured JSON format.

---

## 🚀 Project Overview

TalentScout-AI offers:
- **Resume Parsing**: Extracts candidate details like name, email, phone, experience, and technical skills from uploaded resumes.
- **Manual Entry**: Allows manual entry of technical skills for customized input.
- **Question Generation**: Creates technical questions tailored to the candidate’s skills.
- **Feedback Collection**: Records answers and feedback for analysis.
- **Export Feature**: Saves questions and answers as a JSON file for easy access.

---

## 🛠️ Installation Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/TalentScout-AI.git
cd TalentScout-AI
```

### Set Up a Virtual Environment:


```bash
python -m venv venv
source venv/bin/activate  
# On Windows: 
venv\Scripts\activate
```
Install Dependencies:

```bash
pip install -r requirements.txt

```
### Set Up API Keys:

Obtain a Google PaLM API key and set it as an environment variable:


```bash
export GOOGLE_API_KEY=your_api_key_here

```
Run the Application:

```bash
streamlit run main.py
```
Access the Application:

Open your browser and navigate to http://localhost:8501.
## 📖 Usage Guide
### Home Page:

Overview of the TalentScout-AI system and navigation menu.
### Resume Uploader:

Upload a PDF resume, and the system will parse details and extract top technical skills.
Generate technical questions based on the extracted skills.
### Manual Entry:

Enter technical skills manually to generate related questions.
Respond to the generated questions directly in the app.
### About Me:

Information about the project and its developers.
### Feedback:

Submit responses and download them in JSON format for analysis.
## 🧰 Technical Details
Libraries Used:

**Streamlit**: Frontend and interactive web app.
**google-generativeai**: Integration with Google PaLM API.
**PyPDF2**: For PDF parsing and data extraction.
**json**: For saving and exporting responses.
**Model Details:**

Uses Google PaLM API (Gemini-Pro) for question generation and conversational AI.
### Architectural Decisions:

Modular design with separate classes for resume parsing, manual entry, and question generation.
State management via st.session_state in Streamlit for retaining user inputs.
## 💡 Prompt Design
Prompts were carefully crafted to:

Extract specific technical skills from candidate resumes.
Generate focused and relevant technical questions.
Facilitate smooth user interactions through clear instructions and feedback collection.
### Example Prompt:
"Generate 5 technical interview questions based on the skill: Python"

The model processes this prompt to create targeted and well-structured questions.

## 🛠️ Challenges & Solutions
Challenge 1: Handling Disappearing Text Areas
Issue: User responses in text areas were disappearing upon UI interactions.
Solution: Managed st.session_state effectively to persist user inputs.
Challenge 2: Resume Parsing
Issue: Difficulty in extracting structured data from varying resume formats.
Solution: Used PyPDF2 for text extraction and implemented robust parsing logic.
Challenge 3: API Response Latency
Issue: Delay in question generation using the Google PaLM API.
Solution: Implemented caching mechanisms and progress indicators to improve user experience.
## 📌 Future Enhancements
Add support for additional file formats (e.g., Word documents).
Enhance question generation using fine-tuned models.
Introduce analytics dashboards for visualizing candidate responses.
## ✨ Authors
Developed with ❤️ by R.Sarath Kumar and contributors.

Feel free to contribute to this project by submitting pull requests or reporting issues!


Let me know if you want me to add any additional details!
