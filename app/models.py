from pydantic import BaseModel

class SentimentRequest(BaseModel):
    text: str
    gcp_credentials_json: str  # Base64-encoded Google credentials JSON

class SentimentResponse(BaseModel):
    score: float
    magnitude: float
    sentiment: str
