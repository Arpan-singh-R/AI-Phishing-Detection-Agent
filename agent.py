from dotenv import load_dotenv
import os

from langchain_groq import ChatGroq

from parser import parse_email, parse_email_text
from tools import calculate_risk
from prompts import SYSTEM_PROMPT
from config import MODEL_NAME, TEMPERATURE

# Load .env
load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model=MODEL_NAME,
    temperature=TEMPERATURE
)


def build_prompt(email, analysis):
    """
    Build the prompt for the AI model.
    """
    return f"""
{SYSTEM_PROMPT}

Email Details:
Sender: {email['sender']}
Subject: {email['subject']}

Email Body:
{email['body']}

URLs:
{email['urls']}

Attachments:
{email['attachments']}

Rule-Based Analysis:
Risk Score: {analysis['score']}
Risk Level: {analysis['risk']}

Findings:
{chr(10).join('- ' + item for item in analysis['findings'])}

Please provide:
1. A short summary.
2. Why this email is suspicious or safe.
3. Overall risk level.
4. Recommendations for the user.
"""


def analyze_email(file_path):
    """
    Analyze an uploaded email file.
    """
    email = parse_email(file_path)

    analysis = calculate_risk(email)

    prompt = build_prompt(email, analysis)

    response = llm.invoke(prompt)

    return response.content


def analyze_email_text(email_text):
    """
    Analyze pasted email text.
    """
    email = parse_email_text(email_text)

    analysis = calculate_risk(email)

    prompt = build_prompt(email, analysis)

    response = llm.invoke(prompt)

    return email, analysis, response.content