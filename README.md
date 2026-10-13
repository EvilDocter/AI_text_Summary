# AI Text Summarizer

An AI-powered text summarization application built with Streamlit and Google Gemini (`google-genai`).

## Features

- Summarize long articles, reports, and notes quickly
- Structured JSON or concise text summarization powered by Gemini 3.5 Flash Lite
- Interactive Streamlit web interface

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone git@github.com:EvilDocter/AI_text_Summary.git
   cd AI_text_Summary
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables:**
   Copy `.env.example` to `.env` and fill in your Gemini API key:
   ```bash
   cp .env.example .env
   ```
   Add your Gemini API key:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

5. **Run the Application:**
   ```bash
   streamlit run text_summarizer.py
   ```
