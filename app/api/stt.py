from fastapi import APIRouter, UploadFile, File
from app.services.stt_services import speech_to_text

router = APIRouter()

@router.post("/")
async def stt(file: UploadFile = File(...)):
    text = await speech_to_text(file)
    return {"text": text}
