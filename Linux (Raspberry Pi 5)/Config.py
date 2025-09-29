import os
from dotenv import load_dotenv

load_dotenv()  # loads the .env file
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
ELEVEN_API_KEY = os.getenv("ELEVENLABS_API_KEY")

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

camera_id = 0  # Change to the index of your camera

# Replace this with the correct microphone index
mic_index = 1  # Change to the index of your microphone

VOICE_ID = "2BJW5coyhAzSr8STdHbE" # <------ Or Whatever Voice ID You Want!
RECORD_SECONDS = 5
FILENAME = "temp.wav"
SAMPLERATE = 44100  # CD-quality audio

SAMPLE_RATE = 16000
CHANNEL = 1 # Change to your right channel
FRAME_DURATION = 30  # ms
FRAME_SIZE = int(SAMPLE_RATE * FRAME_DURATION / 1000)
MAX_SILENCE_FRAMES = 15  # ~0.5 seconds of silence
