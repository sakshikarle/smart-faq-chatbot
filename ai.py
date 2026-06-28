import os
from dotenv import load_dotenv
from google import genai

# Load .env
load_dotenv()

# Read API key
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# Gemini Client
client = genai.Client(api_key=API_KEY)


def ask_ai(question):
    prompt = f"""
You are a Smart FAQ Chatbot.

Instructions:
- Answer in simple English.
- Do not use Markdown.
- Do not use headings like ###.
- Do not use **bold** text.
- Keep the answer short.
- Maximum 120 words.
- Write in simple paragraphs.

User Question:
{question}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:
        return f"AI Error: {str(e)}"