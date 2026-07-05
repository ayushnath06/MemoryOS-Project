from groq import Groq
from backend.prompt import SYSTEM_PROMPT
from backend.config import GROQ_API_KEY

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