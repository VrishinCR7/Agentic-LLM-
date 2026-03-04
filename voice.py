# core/voice.py

import edge_tts
import asyncio
import tempfile

VOICE = "en-US-GuyNeural"


async def _generate_audio_async(text: str, output_file: str):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(output_file)


def generate_speech(text: str):
    """
    Generate speech from text and return audio file path
    """

    if not text or text.strip() == "":
        return None

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    audio_path = temp_file.name
    temp_file.close()

    asyncio.run(_generate_audio_async(text, audio_path))

    return audio_path