import os
import streamlit as st
import google.generativeai as genai

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Auto Hub | AI Assistant",
    page_icon="🚗",
    layout="wide",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* Main background */
    .stApp { background-color: #0d0d0d; }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(160deg, #1a1a2e 0%, #16213e 100%);
        border-right: 1px solid #e63946;
    }
    [data-testid="stSidebar"] * { color: #f0f0f0 !important; }

    /* Chat message bubbles */
    .user-msg {
        background: linear-gradient(135deg, #e63946, #c1121f);
        color: white;
        padding: 12px 16px;
        border-radius: 18px 18px 4px 18px;
        margin: 8px 0 8px 60px;
        box-shadow: 0 2px 8px rgba(230,57,70,0.3);
    }
    .bot-msg {
        background: linear-gradient(135deg, #1e1e2e, #2a2a3e);
        color: #e0e0e0;
        padding: 12px 16px;
        border-radius: 18px 18px 18px 4px;
        margin: 8px 60px 8px 0;
        border-left: 3px solid #e63946;
        box-shadow: 0 2px 8px rgba(0,0,0,0.3);
    }
    .msg-label {
        font-size: 11px;
        opacity: 0.6;
        margin-bottom: 4px;
        font-weight: 600;
        letter-spacing: 0.5px;
        text-transform: uppercase;
    }

    /* Header */
    .brand-header {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 16px 0 8px 0;
        border-bottom: 2px solid #e63946;
        margin-bottom: 20px;
    }
    .brand-title {
        font-size: 28px;
        font-weight: 800;
        color: #ffffff;
        letter-spacing: 1px;
    }
    .brand-subtitle {
        font-size: 13px;
        color: #e63946;
        font-weight: 500;
    }

    /* Input area */
    .stTextInput > div > div > input {
        background: #1e1e2e !important;
        color: white !important;
        border: 1px solid #e63946 !important;
        border-radius: 10px !important;
    }

    /* Buttons */
    .stButton > button {
        background: linear-gradient(135deg, #e63946, #c1121f) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        width: 100%;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #c1121f, #a00e18) !important;
        transform: translateY(-1px);
    }

    /* Quick question chips */
    .chip-row { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 16px; }
    .chip {
        background: #1e1e2e;
        border: 1px solid #e63946;
        color: #e63946;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 12px;
        cursor: pointer;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #555;
        font-size: 12px;
        margin-top: 30px;
        padding-top: 16px;
        border-top: 1px solid #222;
    }
    
    /* Hide default streamlit elements */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── Session state ──────────────────────────────────────────────────────────────
if "history" not in st.session_state:
    st.session_state.history = []
if "chat_obj" not in st.session_state:
    st.session_state.chat_obj = None

# ── Load API Key ───────────────────────────────────────────────────────────────
if os.path.exists(".env"):
    from dotenv import load_dotenv
    load_dotenv(override=True)

API_KEY = os.getenv("API_KEY")

if not API_KEY:
    try:
        API_KEY = st.secrets["API_KEY"]
    except Exception:
        API_KEY = None

if not API_KEY:
    st.error("⚠️ No API Key found! Please add your Google Gemini API key to the `.env` file.")
    st.code('API_KEY="Your-Google-Gemini-API-Key-Here"', language="bash")
    st.stop()

# ── Initialize Gemini ──────────────────────────────────────────────────────────
genai.configure(api_key=API_KEY)

SYSTEM_PROMPT = """You are the Auto Hub AI Assistant — a friendly, knowledgeable, and professional virtual sales advisor for Auto Hub, a premium car dealership.

About Auto Hub:
- Premium dealership offering Electric Vehicles, rugged SUVs, luxury sedans, and high-performance sports cars
- Fleet includes: Toyota Hilux, Toyota Fortuner, BMW 5 Series, Mercedes S-Class, Mahindra Scorpio N, Toyota Land Cruiser, BYD eMAX 7, Thar Roxx Star Edition, Porsche Cayenne, Porsche 911 Carrera 4 GTS
- Services: Test drive bookings, vehicle financing guidance, trade-in inquiries, after-sales support
- Contact: +91 956XXXXX05
- Website: https://gamma.app/docs/From-electric-vehicles-to-rugged-SUVs-luxury-sedans-to-high-perfo-l8gycapahc8xcq5

Your role:
- Help customers find their perfect vehicle based on their needs and budget
- Answer questions about car specs, features, and comparisons
- Guide customers through the test drive booking process
- Provide financing and EMI information in a general sense (always recommend speaking to our finance team for exact figures)
- Be enthusiastic about cars but never pushy
- If asked something outside your expertise, politely redirect to our team

Tone: Warm, professional, and knowledgeable. Use emojis occasionally to stay friendly. Always end with an offer to help further or suggest next steps (like booking a test drive)."""

if st.session_state.chat_obj is None:
    model = genai.GenerativeModel(
        model_name="gemini-2.5-flash",
        system_instruction=SYSTEM_PROMPT
    )
    st.session_state.chat_obj = model.start_chat(history=[])

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🚗 Auto Hub")
    st.markdown("**Your Dream Car Awaits**")
    st.markdown("---")

    st.markdown("### 🏎️ Our Fleet")
    vehicles = [
        "🛻 Toyota Hilux",
        "🚙 Toyota Fortuner",
        "🔵 BMW 5 Series",
        "⭐ Mercedes S-Class",
        "🏔️ Mahindra Scorpio N",
        "🌍 Toyota Land Cruiser",
        "⚡ BYD eMAX 7",
        "🔥 Thar Roxx Star Edition",
        "🏁 Porsche Cayenne",
        "🚀 Porsche 911 Carrera 4 GTS",
    ]
    for v in vehicles:
        st.markdown(f"<small>{v}</small>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 📞 Contact Us")
    st.markdown("📱 +91 956XXXXX05")
    st.markdown("[🌐 Visit Website](https://gamma.app/docs/From-electric-vehicles-to-rugged-SUVs-luxury-sedans-to-high-perfo-l8gycapahc8xcq5)")

    st.markdown("---")
    if st.button("🗑️ Clear Chat"):
        st.session_state.history = []
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            system_instruction=SYSTEM_PROMPT
        )
        st.session_state.chat_obj = model.start_chat(history=[])
        st.rerun()

# ── Main area ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="brand-header">
    <span style="font-size:40px">🚗</span>
    <div>
        <div class="brand-title">AUTO HUB</div>
        <div class="brand-subtitle">AI-Powered Car Assistant • Drive Your Dream Today</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Quick question buttons
quick_questions = [
    "What SUVs do you have?",
    "Tell me about electric vehicles",
    "How do I book a test drive?",
    "Compare BMW 5 Series vs Mercedes S-Class",
    "What's the most affordable car?",
]

cols = st.columns(len(quick_questions))
for i, q in enumerate(quick_questions):
    with cols[i]:
        if st.button(q, key=f"quick_{i}"):
            # Process quick question
            with st.spinner("Auto Hub AI is thinking..."):
                try:
                    response = st.session_state.chat_obj.send_message(q)
                    st.session_state.history.append({"role": "user", "text": q})
                    st.session_state.history.append({"role": "bot", "text": response.text})
                except Exception as e:
                    st.error(f"Error: {e}")

st.markdown("---")

# Chat history display
chat_container = st.container()
with chat_container:
    if not st.session_state.history:
        st.markdown("""
        <div style="text-align:center; padding: 40px; color: #555;">
            <div style="font-size: 50px; margin-bottom: 16px;">👋</div>
            <div style="font-size: 20px; color: #888; margin-bottom: 8px;">Welcome to Auto Hub!</div>
            <div style="font-size: 14px; color: #555;">Ask me anything about our vehicles, test drives, or financing options.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        for msg in st.session_state.history:
            if msg["role"] == "user":
                st.markdown(f"""
                <div class="user-msg">
                    <div class="msg-label">You</div>
                    {msg["text"]}
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div class="bot-msg">
                    <div class="msg-label">🚗 Auto Hub AI</div>
                    {msg["text"]}
                </div>
                """, unsafe_allow_html=True)

st.markdown("---")

# Input area
col1, col2 = st.columns([5, 1])
with col1:
    user_input = st.text_input(
        "Message",
        placeholder="Ask about cars, test drives, pricing, features...",
        label_visibility="collapsed",
        key="user_input"
    )
with col2:
    send = st.button("Send 🚀")

if send and user_input.strip():
    with st.spinner("Auto Hub AI is thinking..."):
        try:
            response = st.session_state.chat_obj.send_message(user_input.strip())
            st.session_state.history.append({"role": "user", "text": user_input.strip()})
            st.session_state.history.append({"role": "bot", "text": response.text})
            st.rerun()
        except Exception as e:
            st.error(f"Something went wrong: {e}")

st.markdown("""
<div class="footer">
    Auto Hub AI Assistant &nbsp;|&nbsp; Powered by Google Gemini &nbsp;|&nbsp; Drive Your Dream Today 🚗
</div>
""", unsafe_allow_html=True)
