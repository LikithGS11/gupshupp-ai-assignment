# Gupshupp AI System — Memory Extraction & Personality Transformation

[Live demo on Streamlit → https://memoryai.streamlit.app/](https://memoryai.streamlit.app/)

> A lightweight Streamlit app that extracts structured memories (preferences, emotional patterns, key facts) from chat logs and rewrites text in different personality tones using the Groq LLaMA models.

---

## Quick Links

- Live app: https://memoryai.streamlit.app/
- Repository: https://github.com/LikithGS11/gupshupp-ai-assignment

---

## Features

- Memory Extraction: extracts preferences, emotional patterns, and facts from chat messages and returns a JSON object.
- Personality Engine: rewrites text in 5 tones (Calm Mentor, Witty Friend, Therapist, Formal, Playful).
- Streamlit UI: dark-themed, responsive, JSON export and copy-to-clipboard actions.

---

## Quick Start (local)

1. Clone the repo:

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

4. Add your Groq API key (create `.env`):

```text
GROQ_API_KEY=gsk_YOUR_GROQ_API_KEY_HERE
```

5. Run the app:

```bash
streamlit run app.py
```

Open: http://localhost:8501

---

## Usage

- Memory Extractor: Paste chat messages (30+ messages recommended) and press **Extract Memory** to get structured JSON output.
- Personality Engine: Enter text, pick a style, and press **Transform Text** to see the rewritten text.

---

## Configuration & Notes

- `requirements.txt` includes `streamlit`, `groq`, `httpx`, and `python-dotenv`.
- The app creates an `httpx.Client(trust_env=False)` to avoid Windows proxy/env issues—no extra proxy config needed.
- Tweak temperature and max_tokens inside the modules if you need different creativity/length.

---

## Deployments

- Streamlit Cloud (recommended): connect your GitHub repo and select `app.py` as the entrypoint.
- Render / Heroku: use `streamlit run app.py --server.port $PORT --server.headless true --server.enableCORS false` as the start command.

---

## Troubleshooting

- If the app raises `GROQ_API_KEY` errors, ensure `.env` exists and contains your key.
- If you see proxy-related errors on Windows, the app already disables `httpx` trust_env; ensure no conflicting network policies block outbound traffic.

---

## License & Credits

MIT License — built by Likith • 2025. Powered by Groq AI and Streamlit.

