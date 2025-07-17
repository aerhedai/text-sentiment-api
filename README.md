# 🧠 Text Sentiment Analysis API

Analyze the sentiment of any input text using Google Cloud's Natural Language API — without using your own cloud budget.  
Users authenticate with their own GCP credentials (base64-encoded), ensuring costs run on their accounts, not ours.

---

## 📌 Features

- Built with **FastAPI** for high performance and automatic OpenAPI docs
- Users supply their own **base64-encoded Google Cloud service account JSON**
- Returns detailed sentiment analysis:
  - **score** (range -1.0 to 1.0)
  - **magnitude** (strength of sentiment)
  - **label** (`POSITIVE`, `NEGATIVE`, `NEUTRAL`)
- Health check endpoint to verify API status
- Containerized with Docker for easy deployment
- Versioned API routes with `/v1` prefix to support future upgrades

---

## 📦 Requirements

- Python 3.10+
- Google Cloud Platform project with **Natural Language API enabled**
- Service account JSON key file with **NLP API access**, base64-encoded

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/text-sentiment-api.git
cd text-sentiment-api
```
### 2. Create and activate a virtual environment (optional but recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
🛠️ Running Locally
Start the FastAPI server with:
```bash
uvicorn app.main:app --reload
```
API will be available at: http://localhost:8000

Interactive API docs (Swagger UI) at: http://localhost:8000/docs

🔧 Using the API
Endpoint: ```POST /v1/analyze```
Request

```json
{
  "text": "I love using AI!",
  "gcp_credentials_json": "<base64-encoded-service-account-json>"
}
```
- ```text```: The string to analyze sentiment on.
- ```gcp_credentials_json```: Your Google Cloud service account key JSON file, base64-encoded (single line, no line breaks).

Response

```json
{
  "score": 0.9,
  "magnitude": 0.8,
  "sentiment_label": "POSITIVE"
}
```
Endpoint: ```GET /v1/health```
Simple health check returning status.

### 🐳 Docker Usage
Build the Docker image:

```bash
docker build -t sentiment-api:1.0.0 .
```
Run the container:

```bash
docker run -p 8000:8000 sentiment-api:1.0.0
```
Then access the API at ```http://localhost:8000```.

### 🏷️ Versioning
API version is set to v1.0.0.

Routes are prefixed with /v1 to support parallel versions in the future.

Git tag ```v1.0.0``` marks this initial stable release.

Future major releases (e.g., v2.0.0) will include breaking changes and new features.

### 📜 CHANGELOG
See CHANGELOG.md for details on version history and changes.

### ⚙️ Deployment Notes
Users must enable Google Cloud Natural Language API in their own projects.

Users provide their own base64-encoded service account JSON, ensuring all billing happens on their accounts.

No credentials or secrets are stored on this API.

### 📄 License
This project is licensed under the MIT License. See LICENSE for details.

### 🔗 Links
GitHub Repo: https://github.com/yourusername/text-sentiment-api

Google Cloud Natural Language API docs: https://cloud.google.com/natural-language/docs

### 🙋‍♂️ Support / Questions
If you encounter any issues or have questions, feel free to open an issue on GitHub or contact the maintainer.

Thank you for using the Text Sentiment Analysis API!
