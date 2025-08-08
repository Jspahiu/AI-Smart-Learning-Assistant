from my_face_recognition import MyFaceRecognition
from my_voice_recognition import VoiceRecognitionThread
import threading
import cv2
import os
from detected_faces import DetectedFaces


# For Mac
#---------------------------
# pip install cmake
# pip install dlib==19.24.2    
# pip install face_recognition   
# pip install setuptool
# pip install numpy==1.26.4
# pip install opencv-python

os.environ["QT_QPA_PLATFORM"] = "xcb"  # Use the X11 plugin


threads = []

camera_id = 0

# Replace this with the correct microphone index
mic_index = 0  # Change to the index of your USB microphone

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