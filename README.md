# ☀️ Solar Industry AI Assistant

This project analyzes rooftop satellite images to estimate solar panel installation potential and ROI.

## 💻 Features
- Rooftop analysis from uploaded image
- Estimates solar capacity, energy output, cost, and ROI
- AI-generated natural language report
- Streamlit web interface

## 🚀 Setup

```bash
git clone <repo>
cd solar_ai_assistant
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # Add your OpenRouter API key
streamlit run app.py
