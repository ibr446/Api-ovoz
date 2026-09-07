from fastapi import APIRouter
from fastapi.responses import FileResponse
from app.schemas.text import TextSchema
from app.services.tts_services import text_to_speech

router = APIRouter()

@router.post("/")
def tts(data: TextSchema):
    audio_path = text_to_speech(data.text)
    return FileResponse(audio_path, media_type="audio/mpeg")
