# 🛡 TrustLayer AI

### 🔐 Real-Time Context-Aware AI Misuse Detection and Prevention Gateway 

🔗 **Live Demo:** [https://trustlayerai.netlify.app/](https://trustlayerai.netlify.app/)
🔗 **Backend API:** [https://trustlayerai.onrender.com](https://trustlayerai.onrender.com)

---

## 🚀 Overview

**TrustLayer AI** is an AI-powered safety layer that analyzes user prompts in real time and classifies them as **SAFE** or **BLOCKED** based on cybersecurity risk, misuse patterns, and intent analysis.

It is designed to act as a **protective intelligence layer for AI systems**, preventing harmful, malicious, or unsafe prompt injections before they reach downstream models.

---

## 🎯 Problem Statement

With the rapid adoption of AI systems, prompt-based attacks such as:

* Phishing content generation
* Malware instructions
* Social engineering prompts
* Jailbreak attempts on LLMs

have become a serious security concern.

Most AI systems lack a **real-time prompt safety filter layer**.

---

## 💡 Our Solution

TrustLayer AI introduces an **AI-based moderation layer** that:

* Accepts user input prompts
* Sends them to a backend AI classifier (Gemini)
* Evaluates intent and risk level
* Returns:

  * 🟢 SAFE
  * 🔴 BLOCKED
  * Risk Score (0–100)

---

## ⚙️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python (FastAPI)
* **AI Model:** Google Gemini API
* **Hosting:**

  * Frontend → Netlify
  * Backend → Render
* **API Communication:** REST (JSON)

---

## 🏗 System Architecture

```
User Input (Frontend - Netlify)
        ↓
REST API Request
        ↓
Backend (FastAPI - Render)
        ↓
Google Gemini AI Model
        ↓
Risk Analysis Engine
        ↓
JSON Response
        ↓
Frontend Display (Score + Status)
```

---

## 🧠 Key Features

✔ Real-time prompt analysis
✔ AI-based intent classification (Gemini)
✔ Risk scoring system (0–100)
✔ SAFE / BLOCKED decision output
✔ Lightweight and fast API response
✔ Fully cloud deployed system

---

## 🌐 Live Deployment

* 🔗 Frontend: [https://trustlayerai.netlify.app](https://trustlayerai.netlify.app)
* 🔗 Backend: [https://trustlayerai.onrender.com](https://trustlayerai.onrender.com)

---

## 🛠️ Setup Instructions (Local Development)

### 1. Clone Repository

```bash
git clone https://github.com/zainam-decodes/TrustLayerAI.git
```

### 2. Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### 3. Frontend

Open:

```
frontend/index.html
```

---

## 🔐 Environment Variables (Render)

```
GEMINI_API_KEY = your_api_key_here
```

---

## 📊 Example Outputs

### Input:

> "Write a phishing email to steal passwords"

Output:

```
Score: 94
Status: BLOCKED
```

---

### Input:

> "Explain machine learning"

Output:

```
Score: 12
Status: SAFE
```

---

## 🔥 Impact

* Prevents unsafe AI prompt exploitation
* Adds security layer to LLM-based systems
* Useful for AI apps, chatbots, and enterprise tools
* Can be integrated into SaaS AI platforms

---

## 🚀 Future Scope

* Browser extension for real-time prompt filtering
* Multi-language risk detection
* Enterprise API for SaaS integration
* Advanced jailbreak detection system
* Logging dashboard for analytics

---

## 👨‍💻 Developer

Built with ❤️ by **Zainab Jahan Umaima**

* GitHub: [https://github.com/zainam-decodes](https://github.com/zainam-decodes)
* Project: TrustLayer AI


