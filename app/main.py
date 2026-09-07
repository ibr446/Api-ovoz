from fastapi import FastAPI
from app.api.tts import router as tts_router
from app.api.stt import router as stt_router

app = FastAPI(title="Voice API")

app.include_router(tts_router, prefix="/tts", tags=["Text to Speech"])
app.include_router(stt_router, prefix="/stt", tags=["Speech to Text"])
