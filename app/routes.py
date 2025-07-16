from fastapi import APIRouter, HTTPException
from app.models import SentimentRequest, SentimentResponse
from app.sentiment_service import analyze_sentiment

router = APIRouter(prefix="/v1")

@router.post("/analyze", response_model=SentimentResponse)
def analyze(request: SentimentRequest):
    try:
        result = analyze_sentiment(request.text, request.gcp_credentials_json)
        return SentimentResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/health")
def health_check():
    return {"status": "ok"}
