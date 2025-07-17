# 🧠 Text Sentiment Analysis API

Analyze the sentiment of any input text using Google Cloud's Natural Language API — without storing or using your own cloud budget.

## 📌 Features
- API built with FastAPI
- Users provide their own GCP credentials (base64-encoded)
- Returns sentiment score, magnitude, and label (positive/neutral/negative)

## 📦 Requirements
- Python 3.10+
- Google Cloud project with NLP API enabled
- Service account JSON key (base64-encoded)

## 🚀 Running the API

### 1. Install Requirements
```bash
pip install -r requirements.txt
