import os
import json
from typing import Tuple

# pip install openai
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def call_gpt(system_prompt: str, user_payload: Dict, model: str = "gpt-4.1-mini") -> Tuple[str, Dict]:
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": json.dumps(user_payload, ensure_ascii=False)}
        ],
        temperature=0.2
    )
    text = resp.choices[0].message.content
    meta = {"model": model, "usage": resp.usage.model_dump() if resp.usage else None}
    return text, meta
