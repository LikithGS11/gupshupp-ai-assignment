"""
Gupshupp AI Assignment - Dark Theme Redesigned Streamlit Application (Groq API)
Author: AI Engineer Candidate
"""

import streamlit as st
import json
from memory_extractor import MemoryExtractor
from personality_engine import PersonalityEngine

# Page configuration
st.set_page_config(
    page_title="Chat Memory and Personality Transformer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dark Theme CSS
st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Dark Theme */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Dark Background */
    .stApp {
        background: #0a0e27;
        color: #e0e6ed;
    }
    
    /* Main container */
    .block-container {
        background: #12172e;
        border-radius: 0;
        padding: 2rem 3rem;
        max-width: 1400px;
    }
    
    /* Modern Dark Header */
    .main-header {
        text-align: center;
        padding: 3rem 2rem;
        background: linear-gradient(135deg, #1e2a4a 0%, #2d1b3d 100%);
        border: 1px solid rgba(124, 92, 255, 0.2);
        border-radius: 16px;
        margin-bottom: 3rem;
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #7c5cff, #ff6b9d);
    }
    
    .main-header h1 {
        font-size: 2.8rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        color: #ffffff;
        text-shadow: 0 0 20px rgba(124, 92, 255, 0.6), 0 0 40px rgba(255, 107, 157, 0.4);
    }
    
    .main-header p {
        font-size: 1.1rem;
        color: #a0aec0;
        font-weight: 400;
    }
    
    /* Section Headers */
    h1, h2, h3 {
        color: #e0e6ed;
        font-weight: 600;
    }
    
    /* Dark Card styling */
    .feature-card {
        background: #1a1f3a;
        padding: 2rem;
        border-radius: 12px;
        border: 1px solid rgba(124, 92, 255, 0.2);
        margin-bottom: 1.5rem;
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        border-color: rgba(124, 92, 255, 0.4);
        box-shadow: 0 8px 32px rgba(124, 92, 255, 0.15);
        transform: translateY(-2px);
    }
    
    .feature-card h3 {
        color: #7c5cff;
        margin-top: 0;
        font-size: 1.3rem;
    }
    
    .feature-card p {
        color: #8892a6;
        margin-bottom: 0;
    }
    
    /* Modern Dark Buttons */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #7c5cff 0%, #ff6b9d 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.85rem 2rem;
        font-weight: 600;
        font-size: 0.95rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 20px rgba(124, 92, 255, 0.4);
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 30px rgba(124, 92, 255, 0.6);
    }
    
    .stButton>button:active {
        transform: translateY(0);
    }
    
    /* Dark Text Areas */
    .stTextArea textarea {
        background: #1a1f3a !important;
        border: 1px solid rgba(124, 92, 255, 0.3) !important;
        border-radius: 10px !important;
        color: #e0e6ed !important;
        padding: 1rem !important;
        font-size: 0.95rem !important;
        transition: all 0.3s ease !important;
    }
    
    .stTextArea textarea:focus {
        border-color: #7c5cff !important;
        box-shadow: 0 0 0 2px rgba(124, 92, 255, 0.2) !important;
    }
    
    .stTextArea textarea::placeholder {
        color: #4a5568 !important;
    }
    
    .stTextArea label {
        color: #a0aec0 !important;
    }
    
    /* Dark Select boxes */
    .stSelectbox > div > div {
        background: #1a1f3a !important;
        border: 1px solid rgba(124, 92, 255, 0.3) !important;
        border-radius: 10px !important;
        color: #e0e6ed !important;
    }
    
    .stSelectbox label {
        color: #a0aec0 !important;
    }
    
    /* Dark Output boxes */
    .output-box {
        background: #1a1f3a;
        padding: 1.5rem;
        border-radius: 12px;
        border-left: 4px solid #7c5cff;
        margin: 1rem 0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        color: #e0e6ed;
        line-height: 1.6;
    }
    
    .after-box {
        border-left: 4px solid #ff6b9d;
    }
    
    /* Dark Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: transparent;
        border-bottom: 1px solid rgba(124, 92, 255, 0.2);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: transparent;
        border-radius: 8px 8px 0 0;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        border: none;
        color: #8892a6;
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        background: rgba(124, 92, 255, 0.1);
        color: #7c5cff;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(124, 92, 255, 0.2) 0%, rgba(255, 107, 157, 0.2) 100%);
        color: #7c5cff;
        border-bottom: 2px solid #7c5cff;
    }
    
    /* Dark Sidebar */
    [data-testid="stSidebar"] {
        background: #0f1425;
        border-right: 1px solid rgba(124, 92, 255, 0.2);
    }
    
    [data-testid="stSidebar"] .stRadio > label {
        color: #e0e6ed !important;
        font-weight: 600;
    }
    
    [data-testid="stSidebar"] .stRadio label {
        color: #a0aec0;
        font-weight: 500;
        padding: 0.75rem 1rem;
        border-radius: 8px;
        transition: all 0.3s ease;
        background: transparent;
    }
    
    [data-testid="stSidebar"] .stRadio label:hover {
        background: rgba(124, 92, 255, 0.1);
        color: #7c5cff;
    }
    
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 {
        color: #e0e6ed;
    }
    
    [data-testid="stSidebar"] .stMarkdown {
        color: #a0aec0;
    }
    
    /* Dark Info boxes */
    .stInfo {
        background: rgba(124, 92, 255, 0.1) !important;
        border-left: 4px solid #7c5cff !important;
        border-radius: 8px !important;
        color: #a0aec0 !important;
    }
    
    /* Memory items */
    .memory-item {
        padding: 1.2rem;
        background: #1a1f3a;
        border-radius: 10px;
        margin: 0.75rem 0;
        border-left: 3px solid #7c5cff;
        box-shadow: 0 2px 12px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
        color: #e0e6ed;
    }
    
    .memory-item:hover {
        transform: translateX(8px);
        border-left-color: #ff6b9d;
        box-shadow: 0 4px 20px rgba(124, 92, 255, 0.2);
    }
    
    .memory-item strong {
        color: #7c5cff;
    }
    
    /* Dark Code blocks */
    .stCodeBlock {
        background: #1a1f3a !important;
        border-radius: 10px !important;
        border: 1px solid rgba(124, 92, 255, 0.2) !important;
    }
    
    /* Dark Success/Error messages */
    .stSuccess {
        background: rgba(72, 187, 120, 0.1) !important;
        border-left: 4px solid #48bb78 !important;
        border-radius: 8px !important;
        color: #68d391 !important;
    }
    
    .stError {
        background: rgba(245, 101, 101, 0.1) !important;
        border-left: 4px solid #f56565 !important;
        border-radius: 8px !important;
        color: #fc8181 !important;
    }
    
    /* Spinner */
    .stSpinner > div {
        border-color: #7c5cff !important;
    }
    
    /* Stats counter */
    .stat-box {
        text-align: center;
        padding: 2rem 1.5rem;
        background: #1a1f3a;
        border-radius: 12px;
        border: 1px solid rgba(124, 92, 255, 0.2);
        box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        margin: 0.5rem;
        transition: all 0.3s ease;
    }
    
    .stat-box:hover {
        border-color: rgba(124, 92, 255, 0.5);
        transform: translateY(-4px);
        box-shadow: 0 8px 30px rgba(124, 92, 255, 0.2);
    }
    
    .stat-number {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, #7c5cff 0%, #ff6b9d 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .stat-label {
        font-size: 0.85rem;
        color: #8892a6;
        margin-top: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        font-weight: 600;
    }
    
    /* Footer */
    .custom-footer {
        text-align: center;
        color: #4a5568;
        padding: 2rem;
        margin-top: 3rem;
        border-top: 1px solid rgba(124, 92, 255, 0.2);
    }
    
    /* Personality descriptions */
    .personality-desc {
        padding: 1rem 1.2rem;
        background: rgba(124, 92, 255, 0.1);
        border-radius: 8px;
        margin-top: 0.75rem;
        color: #a0aec0;
        border-left: 3px solid #7c5cff;
    }
    
    /* Download button override */
    .stDownloadButton>button {
        background: linear-gradient(135deg, #7c5cff 0%, #ff6b9d 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.85rem 2rem;
        font-weight: 600;
    }
    
    /* Horizontal rule */
    hr {
        border-color: rgba(124, 92, 255, 0.2);
        margin: 2rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'memory_extractor' not in st.session_state:
    st.session_state.memory_extractor = MemoryExtractor()
if 'personality_engine' not in st.session_state:
    st.session_state.personality_engine = PersonalityEngine()

# Main header
st.markdown("""
    <div class="main-header">
        <h1>🧠 Chat Memory and Personality Transformer</h1>
        <p>Advanced Memory Extraction & Personality Transformation Engine</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("🎯 Navigation")
page = st.sidebar.radio(
    "Choose a module:",
    ["Memory Extractor", "Personality Engine"],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 About")
st.sidebar.info(
    "**This system demonstrates:**\n\n"
    "🔍 Memory Extraction from conversations\n\n"
    "✨ Personality Transformation of text\n\n"
    "⚡ Powered by Groq API"
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🚀 Features")
st.sidebar.markdown("""
- Real-time Analysis
- Multi-personality Support
- JSON Export
- Blazing Fast Processing
""")

# ====================
# PAGE 1: Memory Extractor
# ====================
if page == "Memory Extractor":
    st.markdown("## 📝 Memory Extraction Module")
    st.markdown("Extract user preferences, emotional patterns, and key facts from chat conversations using advanced AI.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Input section with card
    st.markdown("""
        <div class="feature-card">
            <h3>💬 Input Chat Messages</h3>
            <p>Paste your chat history below. The system works best with 30+ messages.</p>
        </div>
    """, unsafe_allow_html=True)
    
    chat_input = st.text_area(
        "Chat Messages",
        height=300,
        placeholder="Example:\nHey! I love morning workouts at 6 AM\nI'm a product manager at a tech startup\nI feel stressed about Monday deadlines\nCoffee is my go-to drink\nI prefer working remotely\n\n(Add 25+ more messages for best results)",
        label_visibility="collapsed"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Extract button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        extract_button = st.button("🔍 EXTRACT MEMORY", type="primary")
    
    if extract_button:
        if not chat_input.strip():
            st.error("❌ Please enter some chat messages first!")
        else:
            with st.spinner("🤖 Analyzing messages with Groq AI..."):
                try:
                    # Call memory extraction
                    result = st.session_state.memory_extractor.extract_memory(chat_input)
                    
                    # Store in session state
                    st.session_state.memory_result = result
                    
                    st.success("✅ Memory extraction completed successfully!")
                    
                except Exception as e:
                    st.error(f"❌ Error during extraction: {str(e)}")
    
    # Display results if available
    if 'memory_result' in st.session_state:
        st.markdown("---")
        st.markdown("## 📊 Extraction Results")
        
        result = st.session_state.memory_result
        
        # Stats display
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""
                <div class="stat-box">
                    <div class="stat-number">{len(result['preferences'])}</div>
                    <div class="stat-label">Preferences</div>
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown(f"""
                <div class="stat-box">
                    <div class="stat-number">{len(result['emotional_patterns'])}</div>
                    <div class="stat-label">Patterns</div>
                </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown(f"""
                <div class="stat-box">
                    <div class="stat-number">{len(result['facts'])}</div>
                    <div class="stat-label">Key Facts</div>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Create tabs for different sections
        tab1, tab2, tab3, tab4 = st.tabs(["📋 Preferences", "💭 Emotional Patterns", "✅ Key Facts", "📥 JSON Export"])
        
        with tab1:
            st.markdown("### User Preferences")
            if result['preferences']:
                for i, pref in enumerate(result['preferences'], 1):
                    st.markdown(f"""
                        <div class="memory-item">
                            <strong>#{i}</strong> &nbsp;&nbsp; {pref}
                        </div>
                    """, unsafe_allow_html=True)
            else:
                st.info("No preferences detected in the conversation.")
        
        with tab2:
            st.markdown("### Emotional Patterns")
            if result['emotional_patterns']:
                for i, pattern in enumerate(result['emotional_patterns'], 1):
                    st.markdown(f"""
                        <div class="memory-item">
                            <strong>#{i}</strong> &nbsp;&nbsp; {pattern}
                        </div>
                    """, unsafe_allow_html=True)
            else:
                st.info("No emotional patterns detected in the conversation.")
        
        with tab3:
            st.markdown("### Facts Worth Remembering")
            if result['facts']:
                for i, fact in enumerate(result['facts'], 1):
                    st.markdown(f"""
                        <div class="memory-item">
                            <strong>#{i}</strong> &nbsp;&nbsp; {fact}
                        </div>
                    """, unsafe_allow_html=True)
            else:
                st.info("No key facts detected in the conversation.")
        
        with tab4:
            st.markdown("### Complete JSON Output")
            st.markdown("Download or copy the complete extraction results:")
            json_str = json.dumps(result, indent=2)
            st.code(json_str, language="json")
            
            # Download button
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.download_button(
                    label="📥 DOWNLOAD JSON",
                    data=json_str,
                    file_name="memory_extraction.json",
                    mime="application/json",
                    use_container_width=True
                )

# ====================
# PAGE 2: Personality Engine
# ====================
elif page == "Personality Engine":
    st.markdown("## ✨ Personality Transformation Engine")
    st.markdown("Transform any text into different personality tones with the power of AI.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Input section with card
    st.markdown("""
        <div class="feature-card">
            <h3>📝 Base Reply</h3>
            <p>Enter the text you want to transform into a different personality style.</p>
        </div>
    """, unsafe_allow_html=True)
    
    base_reply = st.text_area(
        "Base Reply",
        height=150,
        placeholder="Example: You need to prioritize your tasks and manage your time better. Start by creating a schedule and sticking to it.",
        label_visibility="collapsed"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Personality selection with enhanced UI
    st.markdown("""
        <div class="feature-card">
            <h3>🎭 Select Personality Style</h3>
            <p>Choose how you want the message to be transformed.</p>
        </div>
    """, unsafe_allow_html=True)
    
    personality = st.selectbox(
        "Personality",
        ["calm mentor", "witty friend", "therapist", "formal", "playful"],
        index=0,
        label_visibility="collapsed"
    )
    
    # Enhanced personality descriptions
    personality_descriptions = {
        "calm mentor": "🧘 **Wise Guide** - Patient, encouraging, and insightful guidance with a nurturing tone",
        "witty friend": "😄 **Casual Buddy** - Humorous, relatable, and conversational with a friendly vibe",
        "therapist": "💆 **Empathetic Counselor** - Supportive, reflective, and deeply understanding",
        "formal": "👔 **Professional Advisor** - Structured, objective, and business-appropriate",
        "playful": "🎉 **Energetic Motivator** - Fun, enthusiastic, and uplifting"
    }
    
    st.markdown(f"""
        <div class="personality-desc">
            {personality_descriptions[personality]}
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Transform button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        transform_button = st.button("🎨 TRANSFORM", type="primary")
    
    if transform_button:
        if not base_reply.strip():
            st.error("❌ Please enter a base reply first!")
        else:
            with st.spinner(f"🤖 Transforming to {personality} style..."):
                try:
                    # Call personality transformation
                    result = st.session_state.personality_engine.transform_personality(
                        base_reply, 
                        personality
                    )
                    
                    # Store in session state
                    st.session_state.transform_result = result
                    
                    st.success(f"✅ Successfully transformed to {personality} style!")
                    
                except Exception as e:
                    st.error(f"❌ Error during transformation: {str(e)}")
    
    # Display results if available
    if 'transform_result' in st.session_state:
        st.markdown("---")
        st.markdown("## 🔄 Transformation Results")
        
        result = st.session_state.transform_result
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📝 Original Text")
            st.markdown(f"""
                <div class="output-box">
                    {result['before']}
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown(f"### ✨ {personality.title()} Style")
            st.markdown(f"""
                <div class="output-box after-box">
                    {result['after']}
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Copy section
        st.markdown("### 📋 Copy Transformed Text")
        st.code(result['after'], language=None)

# Footer
st.markdown("""
    <div class="custom-footer">
        <p style="font-size: 1rem; font-weight: 600; margin-bottom: 0.5rem;">
            Built with ❤️ using Streamlit + Groq API
        </p>
        <p style="font-size: 0.85rem;">
            Gupshupp Founding AI Engineer Assignment
        </p>
    </div>
""", unsafe_allow_html=True)