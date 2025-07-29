import threading
import os.path
import os
import speech_recognition as sr
import cv2
from detected_faces import DetectedFaces
import time
import pyttsx3
from my_chatbot import Chatbot
import random
from AppKit import NSSpeechSynthesizer

engine = pyttsx3.init()

class VoiceRecognitionThread(threading.Thread):
    def __init__(self, mic_index:int, detected_faces: DetectedFaces, stop_event: threading.Event):
        threading.Thread.__init__(self)
        self.mic_index = mic_index
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 400
        self.recognizer.pause_threshold = 1.0
        self.recognizer.dynamic_energy_threshold = True
        
        self.running = True
        self.detected_faces = detected_faces

        self.stop_event = stop_event

        self.chatbot = Chatbot(["data_sets/Bill of Rights Full.pdf", "data_sets/Floor_Hockey.pdf", "data_sets/electric_cars_america.pdf", "data_sets/global_warming.pdf", 
                                "data_sets/Justicia_Carnea.pdf", "data_sets/The Veldt.pdf", "data_sets/Nerves System.pdf", "data_sets/Parts Of Cells.pdf"], False)

        self.speechSynthesizer = NSSpeechSynthesizer.alloc().initWithVoice_("com.apple.speech.synthesis.voice.Bruce")
        

    def run(self):
        
        self.chatbot.initialize()

        existing_detected_faces = []
        
        with sr.Microphone(device_index=self.mic_index) as source:
            self.recognizer.adjust_for_ambient_noise(source)  # Reduce the duration here
           
            try:
                while self.running and not self.stop_event.is_set():

                    detected_faces = self.detected_faces.get_detected_faces()

                    while not detected_faces:
                        detected_faces = self.detected_faces.get_detected_faces()
                        time.sleep(0.05)

                    print(f"Detected faces: {", ".join(detected_faces)}")

                    new_faces_detected = [detected_face for detected_face in detected_faces if detected_face not in existing_detected_faces]
                    
                    if new_faces_detected:
                        response_to_say = random_response(new_faces_detected)
                        self.text_to_voice(response_to_say)
                        existing_detected_faces.extend(new_faces_detected)

                    print("Listening...")
                    
                    try:
                        audio = self.recognizer.listen(source, timeout=3, phrase_time_limit=10)
                    except Exception as e:
                        print(f"Unexpected Error Occured! \n {e}")
                        continue

                    print(f"Audio captured...")
                    
                    detected_faces = self.detected_faces.get_detected_faces()
                    
                    if not detected_faces:
                        print(f"Ugh...No faces on camera")
                        continue

                    try:
                        text = self.recognizer.recognize_google(audio, show_all=False)
                        print(f"You said: {text}")

                        if "bye" in text or "exit" in text:
                            chatbot_response = self.chatbot.query(text)
                            print (f"Chatbot Response: {chatbot_response}")
                            self.text_to_voice(chatbot_response)
                            print("PROGRAM IS STOPPING")
                            self.stop()
                            return
                        
                        chatbot_response = self.chatbot.query(text)
                        print (f"Chatbot Response: {chatbot_response}")

                        self.text_to_voice(chatbot_response)
                        
                    except sr.UnknownValueError as e:
                        print(f"Sorry, could not understand the audio.  {e}")
                        self.text_to_voice("Sorry, could not understand the audio. Try again.")
                    except sr.RequestError as e:
                        print(f"Error with the recognition service: {e}")
                        self.text_to_voice("Sorry, there was an error converting the audio to text. Try again.")
                    except Exception as e:
                        print(f"Unexpected Error Occured! \n {e}")

                    # Check for user input to close the camera window
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                    
                    time.sleep(0.5)

            except KeyboardInterrupt:
                print("Stopped listening.")
                self.stop()
        

        

    def text_to_voice(self, text):
        self.speechSynthesizer.startSpeakingString_(text)
        
        # Wait for speech to finish
        while self.speechSynthesizer.isSpeaking():
            time.sleep(0.1)

    def stop(self):
        self.running = False
        # Signal all threads to stop
        self.stop_event.set()

def random_response(name):
    responses = [f"Hi, how can I help you {name}?", f"Hi {name}", f"Anything I can help {name}?", f"Do you have a question to ask?"]
    response = random.choice(responses)
    return response

