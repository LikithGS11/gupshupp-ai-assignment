#  Gupshupp AI Assignment (Groq API Version)

A complete AI-powered system for memory extraction and personality transformation using Groq's powerful API.

##  Features

### Part 1: Memory Extraction Module
- Extracts user preferences from chat conversations
- Identifies emotional patterns and frequencies
- Captures key biographical facts
- Outputs structured JSON format

### Part 2: Personality Engine
- Transforms text into 5 different personality tones:
  -  Calm Mentor
  -  Witty Friend
  -  Therapist
  -  Formal
  -  Playful

### Part 3: Streamlit Web Interface
- Clean, modern dark theme UI with two main pages
- Real-time AI processing powered by Groq
- JSON export functionality
- Copy-to-clipboard features

##  Prerequisites

- Python 3.8 or higher
- Groq API key from https://console.groq.com
- Virtual environment recommended

##  Quick Start

### 1. Create Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file:
```
GROQ_API_KEY=gsk_YOUR_GROQ_API_KEY_HERE
```

### 4. Run the App
```bash
streamlit run app.py
```

Access at: `http://localhost:8501`

##  Getting Your Groq API Key

1. Visit: https://console.groq.com
2. Sign up with email or GitHub
3. Go to API Keys section
4. Create a new API key
5. Copy and paste into .env file

##  Usage Guide

### Memory Extraction
1. Go to 'Memory Extractor' tab
2. Paste 30+ chat messages
3. Click 'Extract Memory'
4. View preferences, emotional patterns, and facts
5. Download JSON if needed

### Personality Transformation
1. Go to 'Personality Engine' tab
2. Enter your text
3. Select personality style
4. Click 'Transform'
5. See before/after results

##  Project Structure

```
gupshupp-ai-assignment/
 app.py                    # Main Streamlit application
 memory_extractor.py       # Memory extraction module
 personality_engine.py     # Personality transformation engine
 requirements.txt          # Python dependencies
 .env.example             # Environment template
 .gitignore               # Git ignore rules
 README.md                # This file
```

##  Tech Stack

- **UI**: Streamlit 1.31.0
- **AI**: Groq API (llama-3.3-70b-versatile)
- **HTTP Client**: httpx 0.28.1 (with proxy-safe configuration)
- **Language**: Python 3.8+
- **Config**: python-dotenv 1.0.1

##  Technical Details

### Proxy Handling
- The app automatically clears system proxy environment variables
- Uses `httpx.Client(trust_env=False)` to prevent proxy conflicts
- Windows PowerShell users: proxies are handled automatically

### API Configuration
- **Model**: llama-3.3-70b-versatile
- **Temperature**: 0.3 (Memory), 0.7 (Personality)
- **Max Tokens**: 2000 (Memory), 1000 (Personality)

##  Troubleshooting

| Issue | Solution |
|-------|----------|
| GROQ_API_KEY not found | Create .env file with your API key |
| Module not found error | Run `pip install -r requirements.txt` |
| Connection timeout | Check internet connection and Groq API status |
| Memory extraction empty | Ensure 30+ messages in input for better results |

##  Resources

- Groq Console: https://console.groq.com
- Groq API Docs: https://console.groq.com/docs
- Streamlit Docs: https://docs.streamlit.io

##  License

MIT License - Free to use and modify

##  Author

Built by Likith • 2025 | Powered by Groq AI
