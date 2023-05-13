import os
import openai

from dotenv import load_dotenv

load_dotenv()

if os.getenv('OPENAI_API_BASE'):
    openai.api_base = os.getenv('OPENAI_API_BASE')

openai.api_key = os.getenv('OPENAI_API_KEY')

MODEL = os.getenv('OPENAI_CHAT_MODEL') or 'gpt-3.5-turbo'

def generate(messages: str):
    """Generates a new message based on the given messages."""

    return openai.ChatCompletion.create(
        model=MODEL,
        messages=messages,
        temperature=0.8,
        frequency_penalty=0.0,
        presence_penalty=2,

    ).choices[0].message.content
