import os
from dotenv import load_dotenv

load_dotenv()  # loads the .env file
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
ELEVEN_API_KEY = os.getenv("ELEVENLABS_API_KEY")

#os.environ["OPENAI_API_KEY"] = ""
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

#ELEVEN_API_KEY = ""
VOICE_ID = "3NFDHTNDKqip06i6bFkQ"  # Rachel (or another voice ID)
RECORD_SECONDS = 5
FILENAME = "temp.wav"
SAMPLERATE = 44100  # CD-quality audio

SAMPLE_RATE = 16000
FRAME_DURATION = 30  # ms
FRAME_SIZE = int(SAMPLE_RATE * FRAME_DURATION / 1000)
MAX_SILENCE_FRAMES = 15  # ~0.5 seconds of silence