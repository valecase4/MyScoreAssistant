from dotenv import load_dotenv
import os

def get_credentials():
    load_dotenv()
    app_password = os.getenv("APP_PASSWORD")

    return app_password

import re

def parse_email_body(email_body):
    # Regex patterns for extracting the details
    exam_name_pattern = r"attività didattica (.+?) ,"
    exam_date_pattern = r"sostenuta in data (\d{2}/\d{2}/\d{4})"
    score_pattern = r"è (\d{1,2}/\d{1,2}) \."

    # Extract details using regex
    exam_name_match = re.search(exam_name_pattern, email_body)
    exam_date_match = re.search(exam_date_pattern, email_body)
    score_match = re.search(score_pattern, email_body)

    # Get the values if matches are found
    exam_name = exam_name_match.group(1) if exam_name_match else None
    exam_date = exam_date_match.group(1) if exam_date_match else None
    score = score_match.group(1) if score_match else None

    return {
        "exam_name": exam_name,
        "exam_date": exam_date,
        "score": score,
    }


