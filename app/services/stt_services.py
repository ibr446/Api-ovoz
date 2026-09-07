import whisper
from fastapi import UploadFile
from app.core.paths import INPUT_AUDIO_PATH

model = whisper.load_model("base")

async def speech_to_text(file: UploadFile) -> str:
    filepath = INPUT_AUDIO_PATH / file.filename

    with open(filepath, "wb") as f:
        f.write(await file.read())

    result = model.transcribe(str(filepath), language="uz")
    return result["text"]
