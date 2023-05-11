import os
import openai

from dotenv import load_dotenv

import prompts

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
        temperature=0.9
    ).choices[0].message.content

if __name__ == '__main__':
    print(prompts.MESSAGES)
    # print(generate(prompts.MESSAGES))
