from my_face_recognition import MyFaceRecognition
from my_voice_recognition import VoiceRecognitionThread
import threading
import cv2
import os
from detected_faces import DetectedFaces
from Config import *

os.environ["QT_QPA_PLATFORM"] = "xcb"  # Use the X11 plugin


threads = []

detected_faces = DetectedFaces()
stop_event = threading.Event()


voice_thread = VoiceRecognitionThread(mic_index, detected_faces, stop_event)
voice_thread.daemon = True
voice_thread.start()
threads.append(voice_thread)

face_recognition = MyFaceRecognition(camera_id, "MyWindow", "images", detected_faces, stop_event)
face_recognition.run()



# Wait for all threads to finish
for thread in threads:
    thread.join()



cv2.destroyAllWindows()
