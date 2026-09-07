from gtts import gTTS
import uuid
from app.core.paths import OUTPUT_AUDIO_PATH

def text_to_speech(text: str) -> str:
    filename = f"{uuid.uuid4()}.mp3"
    filepath = OUTPUT_AUDIO_PATH / filename

    tts = gTTS(text=text, lang="uz")
    tts.save(filepath)

    return filepath
