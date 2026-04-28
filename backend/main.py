from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests
import json
import os

app = FastAPI()

# ✅ CORS (allow frontend to connect)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔐 Gemini API Key (Render ENV variable)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

class Input(BaseModel):
    text: str


@app.post("/analyze")
def analyze(data: Input):

    prompt = f"""
You are a cybersecurity AI system.

Classify the user input.

Return ONLY valid JSON (no text, no explanation, no markdown):

{{
  "score": number between 0 and 100,
  "status": "SAFE" or "BLOCKED"
}}

Rules:
- BLOCKED → phishing, hacking, malware, fraud, scams, illegal instructions
- SAFE → educational, normal, harmless queries

User Input: {data.text}
"""

    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

    response = requests.post(url, json={
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    })

    try:
        # 🔥 Extract Gemini response text
        text_output = response.json()["candidates"][0]["content"]["parts"][0]["text"]

        # 🧹 Clean response (remove ```json if present)
        cleaned = text_output.strip().replace("```json", "").replace("```", "")

        # 🔄 Convert to JSON
        parsed = json.loads(cleaned)

        return {
            "result": parsed
        }

    except Exception as e:
        return {
            "result": {
                "score": 50,
                "status": "BLOCKED",
                "error": "Parsing failed"
            }
        }
