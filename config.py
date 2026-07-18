import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Groq API Key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Model Configuration
MODEL_NAME = "llama-3.3-70b-versatile"
TEMPERATURE = 0