# core/llm.py
DEBUG_MODE = False

import os
import json
import re
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("HF_TOKEN")

if not api_key:
    raise ValueError("HF_TOKEN not found in environment.")

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=api_key,
)

MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"
DEFAULT_TEMPERATURE = 0.0


def call_llm(system_prompt: str, user_prompt: str, temperature: float = DEFAULT_TEMPERATURE):
    if DEBUG_MODE:
        print("⚠️ DEBUG MODE — No real API call made.")
        return """
1. Define core features
2. Design system architecture
3. Implement backend
4. Build frontend
5. Deploy MVP
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=temperature,
    )

    return response.choices[0].message.content