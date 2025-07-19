import threading

class DetectedFaces():
    def __init__(self):
        self.detected_faces = []
        self.lock = threading.Lock()
    
    def get_detected_faces(self):
        with self.lock:
            return self.detected_faces
        
    def set_detected_faces(self, faces:list):
        with self.lock:
            self.detected_faces = faces

