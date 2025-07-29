import cv2
import pygame
import threading
from simple_facerec import SimpleFacerec
from detected_faces import DetectedFaces

# Class to handle video capture from a camera
class FaceRecognitionThread(threading.Thread):
    def __init__(self, camera_id:int, window_name:str, images_path:str, detected_faces: DetectedFaces, stop_event: threading.Event):
        threading.Thread.__init__(self)
        self.camera_id = camera_id
        self.window_name = window_name
        self.cap = cv2.VideoCapture(camera_id)
        self.running = True

        self.sfr = SimpleFacerec()
        self.images_path = images_path
        self.detected_faces = detected_faces

        self.stop_event = stop_event

    def run(self):
        self.sfr.load_encoding_images(self.images_path)

        # Initialize Pygame
        pygame.init()

        # Set up the window
        window_size = (640, 480)
        screen = pygame.display.set_mode(window_size)

        while self.running and not self.stop_event.is_set():

            ret, frame = self.cap.read()
            if not ret:
                print(f"Failed to capture frame from camera {self.camera_id}")
                break

            # Detect faces
            face_locations, face_names = self.sfr.detect_known_faces(frame)

            is_new_face_detected = False
            
            my_detected_faces = []

            # Loop through detected faces and draw rectangles and text
            for face_loc, name in zip(face_locations, face_names):
                y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

                if name != "Unknown":
                    if "Jon" in name:
                        name = "Jon Spahiu"
                    cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

                    my_detected_faces.append(name)

            self.detected_faces.set_detected_faces(my_detected_faces)
            
            # Display the frame in a window
            #cv2.imshow(self.window_name, frame)

            # Convert BGR to RGB (Pygame expects RGB format)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Convert to Pygame Surface
            #frame_surface = pygame.surfarray.make_surface(frame_rgb)

            frame_surface = pygame.image.frombuffer(frame_rgb.tobytes(), frame_rgb.shape[1::-1], "RGB")


            # Display the frame
            screen.blit(frame_surface, (0, 0))
            pygame.display.update()

            # Check for user input to close the camera window
            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.stop()
                break

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()
                    break

        # Release the capture object and close the window
        pygame.quit()
        self.cap.release()
        #cv2.destroyWindow(self.window_name)

    def stop(self):
        self.running = False
        # Signal all threads to stop
        self.stop_event.set()

