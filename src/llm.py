import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY is not set. "
        "Please add it to your .env file."
    )


client = Groq(api_key=GROQ_API_KEY)

MODEL_NAME = "openai/gpt-oss-20b"


def generate_response(user_question: str, faq_context: str) -> str:
    """
    Generate a concise FAQ response using only the retrieved FAQ context.
    """

    system_prompt = """
You are an FAQ customer support chatbot.

Your job is to answer the user's question using ONLY the
information provided in the FAQ context.

Strict rules:

1. Do not add facts that are not present in the FAQ context.
2. Do not make assumptions.
3. Do not provide advice that is not present in the FAQ context.
4. Do not ask follow-up questions.
5. Do not offer additional help.
6. Keep the answer concise and natural.
7. You may rephrase the FAQ answer, but you must preserve
   the facts and meaning.
8. If the FAQ context does not contain enough information,
   respond exactly with:
   "I don't have enough information in the FAQ knowledge base
   to answer that question."
"""

    user_prompt = f"""
FAQ Context:
{faq_context}

User Question:
{user_question}

Answer the user using only the FAQ context.
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=0.1,
        max_completion_tokens=200
    )

    return response.choices[0].message.content.strip()
