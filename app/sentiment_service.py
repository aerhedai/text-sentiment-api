import base64
import json
from google.cloud import language_v1
from google.oauth2 import service_account

def analyze_sentiment(text: str, credentials_json: str):
    # Decode and load base64-encoded service account JSON
    decoded_creds = base64.b64decode(credentials_json)
    creds_dict = json.loads(decoded_creds.decode("utf-8"))
    credentials = service_account.Credentials.from_service_account_info(creds_dict)

    # Create Google Cloud NLP client with the user's credentials
    client = language_v1.LanguageServiceClient(credentials=credentials)

    document = language_v1.Document(
        content=text,
        type_=language_v1.Document.Type.PLAIN_TEXT
    )

    response = client.analyze_sentiment(request={"document": document})
    sentiment = response.document_sentiment

    return {
        "score": sentiment.score,
        "magnitude": sentiment.magnitude,
        "sentiment": (
            "positive" if sentiment.score > 0.25 else
            "negative" if sentiment.score < -0.25 else
            "neutral"
        )
    }
