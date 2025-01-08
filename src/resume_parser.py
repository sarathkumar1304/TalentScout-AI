from pdfminer.high_level import extract_text
import re
from datetime import datetime

class ResumeParser:
    def parse(self, resume_file):
        """Extracts text from a PDF resume and processes candidate information."""
        text = extract_text(resume_file)
        return self.extract_candidate_info(text)

    def extract_candidate_info(self, text):
        """Extracts candidate details from the parsed resume text."""
        return {
            "name": self.extract_name(text),
            "email": self.extract_email(text),
            "phone": self.extract_phone(text),
            "experience": self.extract_experience(text),
            "position": self.extract_position(text),
            "location": self.extract_location(text),
            "tech_stack": self.extract_tech_stack(text),
        }

    @staticmethod
    def extract_name(text):
        """Extracts the candidate's name from the first line or common patterns."""
        # Split text into lines and take the first non-empty line
        lines = text.splitlines()
        for line in lines:
            line = line.strip()
            if line:  # Ignore empty lines
                # Check for a valid name format (e.g., avoiding single words like "Resume")
                if len(line.split()) >= 2:  # Name should have at least two words
                    return line
                break
        return "Name not found"

    @staticmethod
    def extract_email(text):
        """Extracts the candidate's email address."""
        match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
        return match.group(0) if match else "Email not found"

    @staticmethod
    def extract_phone(text):
        """Extracts the candidate's phone number."""
        match = re.search(r"\+?\d{10,13}", text)
        return match.group(0) if match else "Phone number not found"

    @staticmethod
    def extract_position(text):
        """Extracts the candidate's position (e.g., Job Title)."""
        match = re.search(r"(?i)experience(?:\:|\s+)([^\n]+)", text)
        return match.group(1).strip() if match else "Position not found"

    @staticmethod
    def extract_location(text):
        """Extracts the candidate's location."""
        # Regex to match patterns like 'Location: Bengaluru, Karnataka' or standalone 'Bengaluru, Karnataka'
        match = re.search(r"(?i)location(?:\:|\s+)([^\n]+)|\b([A-Za-z\s]+,\s*[A-Za-z\s]+)\b", text)
        if match:
            # Group 1 matches 'Location: <value>' and Group 2 matches '<City>, <State>'
            location = match.group(1) or match.group(2)
            return location.strip()
        return "Location not found"

    @staticmethod
    def extract_tech_stack(text):
        """Extracts technical skills dynamically from the skills section."""
        # Find the 'Skills' or 'Technical Skills' section in the text
        match = re.search(r"(?i)(skills|technical skills)(?:\:|\s+)([^\n]+)", text)
        if match:
            tech_line = match.group(2).strip()
            # Split the skills based on common delimiters (comma, semicolon, etc.)
            skills = re.split(r"[,\;\|]", tech_line)
            # Strip whitespace and return unique skills
            return [skill.strip() for skill in skills if skill.strip()]
        return ["No tech stack found"]
    @staticmethod
    def extract_experience(text):
        """Extracts and calculates the candidate's total experience based on date ranges."""
        # Updated regex pattern to match abbreviated and full month names along with 'Present'
        date_pattern = r"(\b(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?) \d{4})"
        regex = rf"{date_pattern}\s*-\s*({date_pattern}|Present)"

        matches = re.findall(regex, text, re.IGNORECASE)

        total_months = 0
        for match in matches:
            start_date_str = match[0]
            end_date_str = match[1]

            start_date = ResumeParser.parse_date(start_date_str)
            end_date = datetime.now() if "Present" in end_date_str else ResumeParser.parse_date(end_date_str)

            if start_date and end_date:
                delta = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
                total_months += delta

        years = total_months // 12
        months = total_months % 12

        return f"{years} years, {months} months" if total_months > 0 else "Experience not found"

    @staticmethod
    def parse_date(date_str):
        """Parses a date string like 'January 2015' or 'Feb 2024' into a datetime object."""
        try:
            return datetime.strptime(date_str, "%b %Y")  # Abbreviated month
        except ValueError:
            try:
                return datetime.strptime(date_str, "%B %Y")  # Full month
            except ValueError:
                return None

    