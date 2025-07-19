from my_face_recognition import MyFaceRecognition
from my_voice_recognition import VoiceRecognitionThread
import threading
import cv2
import os
from detected_faces import DetectedFaces

os.environ["QT_QPA_PLATFORM"] = "xcb"  # Use the X11 plugin


threads = []

camera_id = 0

# Replace this with the correct microphone index
mic_index = 1  # Change to the index of your USB microphone

detected_faces = DetectedFaces()
stop_event = threading.Event()

face_thread = MyFaceRecognition(camera_id, "MyWindow", "images", detected_faces, stop_event)
face_thread.daemon = True
face_thread.start()
threads.append(face_thread)



voice_thread = VoiceRecognitionThread(mic_index, detected_faces, stop_event)
voice_thread.daemon = True
voice_thread.start()
threads.append(voice_thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()





cv2.destroyAllWindows()
