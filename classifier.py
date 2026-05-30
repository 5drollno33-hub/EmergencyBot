from urllib import response

from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def classify(message):

    prompt = f"""
You are an emergency message classifier.

Classify messages into:

- NORMAL
- URGENT
- EMERGENCY
- SARCASM
- EXAGGERATION

Return ONLY JSON:

{{
    "classification":"",
    "confidence":0,
    "requires_attention":false,
    "reason":""
}}

Message:
{message}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

