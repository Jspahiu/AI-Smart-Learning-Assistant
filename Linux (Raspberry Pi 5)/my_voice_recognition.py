import threading
import os.path
import os
import speech_recognition as sr
import cv2
from detected_faces import DetectedFaces
import time
import pyttsx3
from my_face_recognition import FaceRecognitionThread
from chatbot import Chatbot
import yt_dlp
import vlc
import requests

engine = pyttsx3.init()

class VoiceRecognitionThread(threading.Thread):
    def __init__(self, mic_index:int, detected_faces: DetectedFaces, stop_event: threading.Event):
        threading.Thread.__init__(self)
        self.mic_index = mic_index
        self.recognizer = sr.Recognizer()
        # self.recognizer.energy_threshold = 4000  # Lower threshold if background noise is high
        
        self.running = True
        self.detected_faces = detected_faces

        self.stop_event = stop_event

        self.chatbot = Chatbot(["data_sets/Bill of Rights Full.pdf", "data_sets/Dogs_and_Cats.pdf", "data_sets/result.pdf"], False)

        

    def run(self):
        
        self.chatbot.initialize()

        with sr.Microphone(device_index=self.mic_index) as source:
            # self.recognizer.adjust_for_ambient_noise(source, duration=0.5)  # Reduce the duration here
           
            try:
                while self.running and not self.stop_event.is_set():

                    detected_faces = self.detected_faces.get_detected_faces()

                    while not detected_faces:
                        detected_faces = self.detected_faces.get_detected_faces()
                        time.sleep(0.05)

                    print(f"Detected faces: {', '.join(detected_faces)}")

                    self.text_to_voice(f"Hi {', '.join(detected_faces)}! How can I help you?")

                    print("Listening...")
                    
                    # audio = self.recognizer.listen(source, timeout=3, phrase_time_limit=3)
                    audio = self.recognizer.listen(source)

                    print(f"Audio captured...")

                    try:
                        text = self.recognizer.recognize_google(audio, show_all=False)
                        #text = self.recognizer.recognize_sphinx(audio)
                        print(f"You said: {text}")

                        if "play music" in text:
                            try:
                                self.text_to_voice(f"What music do you want to listen?")
                                print("Listening...")
                                audio = self.recognizer.listen(source)
                                print(f"Audio captured...")
                                music_name = self.recognizer.recognize_google(audio, show_all=False)
                                search_and_play_video(music_name)
                            except sr.UnknownValueError as e:
                                print(f"Sorry, could not understand the audio.  {e}")
                                self.text_to_voice("Sorry, could not understand the audio. Try again.")
                            except KeyboardInterrupt:
                                print("Keyboard inturrupted")
                        elif "weather" in text:
                            Weather_Info = get_weather("Orland Park")
                            print(Weather_Info)
                            self.text_to_voice(Weather_Info)
                        # Somehow does not work!!
                        elif "bye" in text or "exit" in text:
                            self.text_to_voice("Shutdown Activated")
                            self.stop()
                            return
                        else:
                            chatbot_response = self.chatbot.query(text)
                            print (f"chatbot_response: {chatbot_response}")

                            self.text_to_voice(chatbot_response)

                    except sr.UnknownValueError as e:
                        print(f"Sorry, could not understand the audio.  {e}")
                        self.text_to_voice("Sorry, can you repeat what you were saying?")
                        
                    except sr.RequestError as e:
                        print(f"Error with the recognition service: {e}")
                        self.text_to_voice("Sorry, there was an error converting the audio to text. Try again.")

                    # Check for user input to close the camera window
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

            except KeyboardInterrupt:
                print("Stopped listening.")
                self.stop()
        

        

    def text_to_voice(self, text):
        os.system(f"espeak -s 140 -p 50 -a 150 \"{text}\"")
 
        # engine.say(text)
        # engine.runAndWait()

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

    # Set the VLC library path for macOS
    os.environ["DYLD_LIBRARY_PATH"] = "/Applications/VLC.app/Contents/MacOS/lib"

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

def get_weather(city_name):
    response = requests.get(f"https://wttr.in/{city_name}?format=%C+%t")
    if response.status_code == 200:
        return f"Weather in {city_name}: {response.text.strip()} Fahrenheit"
    else:
        return "Error fetching weather data."
