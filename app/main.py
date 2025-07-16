from fastapi import FastAPI
from app.routes import router

app = FastAPI(
    title="Text Sentiment Analysis API",
    description="Analyze sentiment of text using Google Cloud Natural Language API.",
    version="1.0.0"
)

app.include_router(router)
