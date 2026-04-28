from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ CORS (IMPORTANT for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔐 Use ENV VARIABLE (Render safe way)
GEMINI_API_KEY = os.getenv("AIzaSyAxA-UsMh5D1faCy6mVVPy2iLb31zeOP4o")

class Input(BaseModel):
    text: str


@app.post("/analyze")
def analyze(data: Input):

    prompt = f"""
You are an AI safety classifier.

Return ONLY valid JSON like this:
{{
  "score": number between 0-100,
  "status": "SAFE or BLOCKED"
}}

Rules:
- BLOCKED = harmful, phishing, fraud, violence, malware
- SAFE = normal queries

Text: {data.text}
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
        text_output = response.json()["candidates"][0]["content"]["parts"][0]["text"]

        # return clean JSON string
        return {
            "result": text_output
        }

    except Exception as e:
        return {
            "result": '{"score":50,"status":"UNKNOWN"}'
        }