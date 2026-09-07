from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
AUDIO_DIR = BASE_DIR / "audio"

INPUT_AUDIO_PATH = AUDIO_DIR / "input"
OUTPUT_AUDIO_PATH = AUDIO_DIR / "output"

INPUT_AUDIO_PATH.mkdir(parents=True, exist_ok=True)
OUTPUT_AUDIO_PATH.mkdir(parents=True, exist_ok=True)
