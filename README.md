# 🛡️ AI Phishing Detection Agent

An AI-powered phishing email detection system built using Python, LangChain, Groq LLM, and Streamlit.

## Features

- 📧 Analyze uploaded email (.txt)
- 📋 Analyze pasted email text
- 🤖 AI explanation using Groq LLM
- 📊 Rule-based phishing detection
- 📄 PDF report generation
- 🌐 URL analysis
- 📎 Attachment analysis
- 🚨 Risk scoring

## Tech Stack

- Python
- Streamlit
- LangChain
- Groq
- ReportLab
- dotenv

## Project Structure

```
AI_Phishing_Agent/
│
├── app.py
├── agent.py
├── parser.py
├── tools.py
├── prompts.py
├── report_generator.py
├── config.py
├── requirements.txt
├── README.md
├── sample_emails/
│   ├── phishing.txt
│   └── safe.txt
└── .env
```

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
streamlit run app.py
```

## Sample Email

```text
From: support@amaz0n.xyz
Subject: Verify Your Amazon Account

Dear Customer,

Verify your password immediately.

Visit:
http://amaz0n.xyz

Attachment: invoice.pdf.exe
```

## Author

**Arpan**

Agentic AI Internship Project