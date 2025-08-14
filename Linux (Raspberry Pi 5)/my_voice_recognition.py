import threading
import os.path
import os
import speech_recognition as sr
import cv2
from detected_faces import DetectedFaces
import time
#import pyttsx3
from chatbot import Chatbot
import random
from Config import *
import sounddevice as sd
import soundfile as sf
from elevenlabs import play
from elevenlabs.client import ElevenLabs
from Config import *
import webrtcvad 
import numpy as np
# Add at top of file
import whisper
from datetime import datetime
import requests
import geocoder
import yt_dlp
import vlc
import requests

whisper_model = whisper.load_model("base")

class VoiceRecognitionThread(threading.Thread):
    def __init__(self, mic_index:int, detected_faces: DetectedFaces, stop_event: threading.Event):
        threading.Thread.__init__(self)
        self.mic_index = mic_index
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 400
        self.recognizer.pause_threshold = 1.0
        self.recognizer.dynamic_energy_threshold = True

        self.eleven = ElevenLabs(
            api_key=ELEVEN_API_KEY,
        )
        
        self.vad = webrtcvad.Vad(0)
        
        self.running = True
        self.detected_faces = detected_faces

        self.stop_event = stop_event

        self.chatbot = Chatbot(["data_sets/Bill of Rights Full.pdf", "data_sets/Floor_Hockey.pdf", "data_sets/electric_cars_america.pdf", "data_sets/global_warming.pdf", 
                                "data_sets/Justicia_Carnea.pdf", "data_sets/The Veldt.pdf", "data_sets/Nerves System.pdf", "data_sets/Parts Of Cells.pdf"], False)

        

    def run(self):
        
        self.chatbot.initialize()
        
        existing_detected_faces = []

        with sr.Microphone(device_index=self.mic_index) as source:
           
            try:
                while self.running and not self.stop_event.is_set():

                    detected_faces = self.detected_faces.get_detected_faces()

                    while not detected_faces:
                        detected_faces = self.detected_faces.get_detected_faces()
                        time.sleep(0.05)

                    print(f"Detected faces: {', '.join(detected_faces)}")

                    
                    new_faces_detected = [detected_face for detected_face in detected_faces if detected_face not in existing_detected_faces]
                    
                    if new_faces_detected:
                        weather_description, temp_description, temp = check_weather()
                        response_to_say = random_response(new_faces_detected, weather_description, temp_description)
                        #self.text_to_voice(f"Hi {" and ".join(new_faces_detected)}! How can I help you?")
                        self.speak_text(response_to_say)
                        existing_detected_faces.extend(new_faces_detected)
                    

                    print("Listening...")
                    
                    try:
                        self.record_with_vad()
                    except Exception as e:
                        print(f"Unexpected Error Occured! \n {e}")
                        continue

                    print(f"Audio captured...")

                    try:
                        text = self.speech_to_text()
                        print(f"You said: {text}")

                        if "play music" in text:
                            try:
                                self.speak_text(f"What music do you want to listen?")
                                print("Listening...")
                                self.record_with_vad()
                                print(f"Audio captured...")
                                music_name = self.speech_to_text()
                                search_and_play_video(music_name)
                            except sr.UnknownValueError as e:
                                print(f"Sorry, could not understand the audio.  {e}")
                                self.speak_text("Sorry, could not understand the audio. Try again.")
                            except KeyboardInterrupt:
                                print("Keyboard inturrupted")
                        elif "weather" in text:
                            weather_description, temp_description, temp = check_weather()
                            self.speak_text(f"The weather today is {weather_description} with tempartures currently {temp} fahrenheit!")
                            return
                        
                        elif "time" in text or "clock" in text:
                            what_time = what_time_exact()
                            time_day = time_of_day()
                            self.speak_text(f"Current it is {what_time} in the {time_day}!")
                            return


                        elif "bye" in text or "exit" in text:
                            chatbot_response = self.chatbot.query(text)
                            print (f"Chatbot Response: {chatbot_response}")
                            self.speak_text(chatbot_response)
                            print("PROGRAM IS STOPPING")
                            self.stop()
                            return
                        else:
                            chatbot_response = self.chatbot.query(text)
                            print(f"chatbot_response: {chatbot_response}")

                            self.speak_text(chatbot_response)

                    except sr.UnknownValueError as e:
                        print(f"Sorry, could not understand the audio.  {e}")
                        self.speak_text("Sorry, can you repeat what you were saying?")
                        
                    except sr.RequestError as e:
                        print(f"Error with the recognition service: {e}")
                        self.speak_text("Sorry, there was an error converting the audio to text. Try again.")

                    # Check for user input to close the camera window
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

            except KeyboardInterrupt:
                print("Stopped listening.")
                self.stop()
        

        

    def record_with_vad(self):
        global CHANNEL, SAMPLE_RATE, FRAME_SIZE, mic_index, MAX_SILENCE_FRAMES, FILENAME, MIC_NAME
        print("Listening... (speak now)")
        audio_frames = []
        voiced_frame_count = 0
        silence_frame_count = 0
        recording = False

        with sd.InputStream(device=mic_index, channels=CHANNEL, samplerate=SAMPLE_RATE, dtype='int16', blocksize=FRAME_SIZE) as stream:
            while True:
                audio_block, _ = stream.read(FRAME_SIZE)
                audio_bytes = audio_block.tobytes()
                is_speech = self.vad.is_speech(audio_bytes, SAMPLE_RATE)

                if is_speech:
                    voiced_frame_count += 1
                    silence_frame_count = 0
                    audio_frames.append(audio_block)
                    recording = True
                else:
                    if recording:
                        silence_frame_count += 1
                        audio_frames.append(audio_block)

                # Only stop after some silence and enough voiced frames
                if recording and silence_frame_count > MAX_SILENCE_FRAMES:
                    if voiced_frame_count > 10:  # 200ms minimum speech
                        break
                    else:
                        print("Stopped Short Speech")
                        audio_frames = []
                        voiced_frame_count = 0
                        silence_frame_count = 0
                        recording = False

        print("Done Recording")
        full_audio = np.concatenate(audio_frames, axis=0)
        sf.write(FILENAME, full_audio, SAMPLE_RATE)
        return full_audio


    def speech_to_text(self, filename=FILENAME):
        print("Bot Talking....")
        result = whisper_model.transcribe(filename)
        print("You said:", result["text"])
        return result["text"]

    def speak_text(self, text):
        print("Speaking...")
        audio = self.eleven.text_to_speech.convert(
            text=text,
            voice_id=VOICE_ID,
            model_id="eleven_monolingual_v1"
        )
        play(audio)

    def stop(self):
        self.running = False
        # Signal all threads to stop
        self.stop_event.set()


def search_and_play_video(video_name):
    # Search for the video using yt-dlp
    options = {
        'quiet': True,  # Suppress yt-dlp console output
        'default_search': 'ytsearch',  # Search on YouTube
        'format': 'bestaudio/best',  # Get the best audio
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        result = ydl.extract_info(f"ytsearch:{video_name}", download=False)
        # Get the first search result
        video = result['entries'][0]
        video_url = video['url']
        print(f"Playing: {video['title']} ({video_url})")

    # Play the audio stream using VLC
    player = vlc.MediaPlayer(video_url)
    player.play()

    print("Streaming audio... Press Ctrl+C to stop.")
    try:
        while True:
            state = player.get_state()
            if state in [vlc.State.Ended, vlc.State.Stopped]:
                break
    except KeyboardInterrupt:
        player.stop()
        print("Playback stopped.")

def time_of_day():
    time_now = datetime.now()
    hour = int(time_now.strftime("%H"))
    if hour <= 11:
        return "morning"
    elif hour >= 12 and hour < 18:
        return "afternoon"
    elif hour >= 18:
        return "evening"

def what_time_exact():
    time_now = datetime.now()
    time = time_now.strftime("%I:%M %p")
    return time

def random_response(name, weather, temp):
    time_of_day_response = time_of_day()
    responses = [f"Hi, how can I help you {name}?", f"Good {time_of_day_response}, how can I help you today?", f"Anything I can help {name}?", f"Do you have a question to ask?", 
                 f"{weather} weather today! How can I help you?", f"{temp} day today! How can I help you?"]
    response = random.choice(responses)
    return response

def check_weather():
    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Fog",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Dense drizzle",
        61: "Slight rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Slight snow fall",
        73: "Moderate snow fall",
        75: "Heavy snow fall",
        80: "Slight rain showers",
        81: "Moderate rain showers",
        82: "Violent rain showers",
        95: "Thunderstorm",
        99: "Thunderstorm with hail"
    }
    
    def get_coordinates():
        g = geocoder.ip('me')
        latitude, longitude = g.latlng
        return latitude, longitude
    

    def get_weather(lat, lon):
        weather_url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": lat,
            "longitude": lon,
            "current": "temperature_2m,weather_code",
            "timezone": "auto"
        }
        response = requests.get(weather_url, params=params)
        data = response.json()
        return data["current"]["temperature_2m"], data["current"]["weather_code"]
    
    def define_temp(temp):
        if temp <= 32:
            return "very cold"
        elif temp >= 40 and temp <= 50:
            return "cold"
        elif temp >= 50 and temp <= 65:
            return "chilly"
        elif temp >= 70 and temp <= 85:
            return "warm"
        elif temp > 85 and temp < 100:
            return "hot"
        elif temp >= 100:
            return "very hot"
    
    
    
    lat, lon = get_coordinates()
    temperature, code = get_weather(lat, lon)
    description = weather_codes.get(code, "Unknown weather")
    temperature = (temperature * 9/5) + 32
    temperature = round(temperature)
    temp_description = define_temp(temperature)
    
    print(f"The current temperature today is {temperature}°C with {description.lower()}.")
    
    return description.lower(), temp_description, temperature
    
    
