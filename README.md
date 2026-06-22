# 🚗 Auto Hub — AI Chatbot Assistant

> An AI-powered car dealership chatbot built with **Streamlit** and **Google Gemini**, designed for the Auto Hub dealership website.

---

## ✨ Features

- 🤖 **AI-Powered Conversations** — Answers questions about vehicles, test drives, financing, and more
- 🚗 **Full Fleet Knowledge** — Knows all Auto Hub vehicles from the Thar Roxx to the Porsche 911
- ⚡ **Quick Questions** — One-click buttons for common queries
- 🎨 **Branded UI** — Dark theme with Auto Hub's signature red accent
- 💬 **Chat History** — Full conversation thread per session
- 🔄 **Clear Chat** — Reset the conversation anytime

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Streamlit](https://streamlit.io) | Web app framework |
| [Google Gemini 2.5 Flash](https://aistudio.google.com) | AI language model |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Environment variable management |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yuviacc/auto-hub-chatbot.git
cd auto-hub-chatbot
```

### 2. Set Up Your API Key

You need a **Google Gemini API key** (free).

👉 Get one here: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

Create a `.env` file in the project root (copy from the example):

```bash
cp .env.example .env
```

Open `.env` and replace the placeholder with your actual key:

```env
API_KEY="Your-Google-Gemini-API-Key-Here"
```

> ⚠️ **Important:** Never commit your `.env` file. It is already listed in `.gitignore`.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run app.py
```

or

```bash
python -m streamlit run app.py
```

The app will open at `http://localhost:8501` in your browser.

---

## ☁️ Deploying to Streamlit Cloud

1. Push this repo to GitHub (without the `.env` file)
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. In **Settings → Secrets**, add:

```toml
API_KEY = "Your-Google-Gemini-API-Key-Here"
```

5. Deploy! 🎉

---

## 📁 Project Structure

```
auto-hub-chatbot/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env.example        # Template for environment variables
├── .env                # Your actual API key (NOT committed to git)
├── .gitignore          # Files to exclude from git
└── README.md           # This file
```

---

## 🚗 Auto Hub Fleet

The chatbot is pre-trained to know about all Auto Hub vehicles:

- 🛻 Toyota Hilux
- 🚙 Toyota Fortuner
- 🔵 BMW 5 Series
- ⭐ Mercedes S-Class
- 🏔️ Mahindra Scorpio N
- 🌍 Toyota Land Cruiser
- ⚡ BYD eMAX 7
- 🔥 Thar Roxx Star Edition
- 🏁 Porsche Cayenne
- 🚀 Porsche 911 Carrera 4 GTS

---

## 📞 Contact

**Auto Hub Dealership**
📱 +91 956XXXXX05
🌐 [Auto Hub Website](https://gamma.app/docs/From-electric-vehicles-to-rugged-SUVs-luxury-sedans-to-high-perfo-l8gycapahc8xcq5)

---

<p align="center">Made with ❤️ by <a href="https://github.com/yuviacc">yuviacc</a> &nbsp;|&nbsp; Auto Hub &nbsp;|&nbsp; Drive Your Dream Today 🚗</p>
