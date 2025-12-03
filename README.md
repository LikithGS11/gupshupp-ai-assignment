# 🚀 Gupshupp AI Assignment (Groq API)

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Groq](https://img.shields.io/badge/Groq-LLama3-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

An AI-powered system for **memory extraction** and **personality transformation**, built using **Groq’s ultra-fast LLaMA models** and **Streamlit**.

---

## 🌟 Features

### 🧠 Memory Extraction
- Extracts user preferences, emotions, and biographical facts  
- Detects emotional patterns and repeated behaviours  
- Outputs clean, structured JSON  

### 🎭 Personality Engine
Transforms text into 5 tones:
- Calm Mentor  
- Witty Friend  
- Therapist  
- Formal  
- Playful  

### 💻 Streamlit UI
- Modern dark-theme interface  
- Two simple pages: Memory Extractor & Personality Engine  
- Copy-to-clipboard + JSON export  

---

## 🛠️ Installation

### 1. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate # Mac/Linux
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Add Environment Variables  
Create `.env`:
```
GROQ_API_KEY=gsk_YOUR_KEY_HERE
```

### 4. Run App
```bash
streamlit run app.py
```

Open: http://localhost:8501

---

## 📁 Project Structure
```
gupshupp-ai-assignment/
├── app.py
├── memory_extractor.py
├── personality_engine.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## 📚 Resources
- Groq Console: https://console.groq.com  
- Streamlit Docs: https://docs.streamlit.io  

---

## ✨ Author
Built by **Likith (2025)** • Powered by **Groq AI**
