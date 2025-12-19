import os
import json

# pip install google-generativeai
import google.generativeai as genai

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

def call_gemini(system_prompt: str, user_payload: Dict, model_name: str = "gemini-1.5-pro") -> str:
    model = genai.GenerativeModel(model_name)
    prompt = f"{system_prompt}\n\nINPUT(JSON):\n{json.dumps(user_payload, ensure_ascii=False)}"
    resp = model.generate_content(prompt)
    return resp.text
