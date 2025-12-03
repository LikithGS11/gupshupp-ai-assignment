<!-- prettier-ignore -->
# 🧠 Gupshupp AI System

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-orange.svg?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Groq](https://img.shields.io/badge/Groq-0.4.1-brightgreen.svg)](https://console.groq.com)
[![LLaMA](https://img.shields.io/badge/LLaMA-llama--3.3--70b-purple.svg)](https://console.groq.com)
[![Deployment](https://img.shields.io/badge/Deployment-Streamlit%20Cloud-blueviolet.svg?logo=heroku&logoColor=white)](https://memoryai.streamlit.app/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


[Live demo → https://memoryai.streamlit.app/](https://memoryai.streamlit.app/)

> Production-style demo showcasing memory extraction and personality transformation using Groq LLaMA models, delivered via a responsive Streamlit interface.

---

## ✨ Overview

Gupshupp AI is a compact, production-minded Streamlit application that demonstrates two practical NLP capabilities:

- **Memory Extraction** — Convert chat logs into structured memories (preferences, recurring emotions, key facts) as clean JSON.
- **Personality Engine** — Rewrites or reframes text into distinct personality tones (e.g., Calm Mentor, Witty Friend, Therapist, Formal, Playful) while preserving intent.

This repository is a strong portfolio piece for recruiters and technical reviewers: it's well-documented, environment-aware (handles Windows proxy pitfalls), and ready to deploy.

---

## 🚀 Highlights

- Clean Streamlit UI with dark theme and copy/export actions.
- Robust Groq integration with explicit `httpx.Client(trust_env=False)` to avoid Windows proxy issues.
- Clear prompt design and JSON-safe output parsing for reliable downstream use.
- Ready for Streamlit Cloud deployment (link above).

---

## 🧩 Features

- **Memory Extraction** — Produces structured JSON capturing:
	- preferences, biographical facts, and repeated behavioral patterns
	- emotional patterns and sentiment cues
	- concise, machine-readable outputs for downstream agents
- **Personality Engine** — Rewrites text across 5 polished tones:
	- Calm Mentor, Witty Friend, Therapist, Formal, Playful
- **Developer-Friendly**
	- Easy local setup via `requirements.txt`
	- `.env` support for `GROQ_API_KEY`
	- Cross-platform notes (PowerShell-ready commands included)
---

## 🧭 Quick Links

- Live app: https://memoryai.streamlit.app/
- Repository: https://github.com/LikithGS11/gupshupp-ai-assignment
- Groq Console: https://console.groq.com
- Streamlit Docs: https://docs.streamlit.io

---

## 🛠️ Quick Start (Local)

Follow these exact steps to run the app locally.

1. Clone the repository:

```bash
git clone https://github.com/LikithGS11/gupshupp-ai-assignment.git
cd gupshupp-ai-assignment
```

2. Create and activate a virtual environment:

Windows (PowerShell):
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Add your Groq API key (create a `.env` file):

```text
GROQ_API_KEY=gsk_YOUR_GROQ_API_KEY_HERE
```

5. Launch the app:

```bash
streamlit run app.py
```

Open the UI at: http://localhost:8501

---

## 🧪 Usage

- **Memory Extractor**: Paste chat messages (30+ messages recommended) and click **Extract Memory** — results are returned as structured JSON suitable for storage or downstream agents.
- **Personality Engine**: Enter a piece of text, select a target style, and click **Transform Text** to receive a polished rewrite in the chosen persona.

---

## ⚙️ Configuration & Notes

- `requirements.txt` includes `streamlit`, `groq`, `httpx`, and `python-dotenv`.
- The app constructs an `httpx.Client(trust_env=False)` and removes common proxy environment variables to avoid the `TypeError: Client.__init__() got an unexpected keyword argument 'proxies'` seen on some Windows setups. No extra proxy configuration should be necessary.
- Adjust temperature / max_tokens in the module files to control creativity and length.

---

## 📦 Deployments

- **Streamlit Cloud (recommended)**: Connect your GitHub repository and set `app.py` as the entrypoint.
- **Render / Heroku**: Use the following start command for headless servers:

```bash
streamlit run app.py --server.port $PORT --server.headless true --server.enableCORS false
```

---

## 🩺 Troubleshooting

- If you receive `GROQ_API_KEY` errors, ensure a `.env` file exists in the project root with a valid key.
- If proxy-related errors appear on Windows, the code already disables `httpx` environment-trusted proxy handling — check for organization-level network restrictions that may block outbound traffic.

---

## 📚 Resources

- Groq Console: https://console.groq.com
- Streamlit Docs: https://docs.streamlit.io

---
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=090909&height=185&section=footer&text=&fontSize=0"/>
</p>









