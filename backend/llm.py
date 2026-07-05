from dotenv import load_dotenv
import os
from groq import Groq

from backend.prompt import SYSTEM_PROMPT

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise Exception("GROQ_API_KEY not found in .env")

client = Groq(api_key=GROQ_API_KEY)


def generate_response(user_message, memory=""):
    prompt = f"""
{SYSTEM_PROMPT}

Relevant Memory:
{memory}

User:
{user_message}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content