import cv2
import pygame
import time
from MeetMePack.BackEnd.supporting_functions import resource_path


def intro():
    try:
        # Sound
        audio_path = resource_path('icons\\intro.mp3')
        pygame.mixer.init()
        pygame.mixer.music.load(audio_path)
        # Video
        video_path = resource_path('icons\\intro.mp4')
        cap = cv2.VideoCapture(video_path)

        # Play sound
        pygame.mixer.music.play()

        # Create window
        cv2.namedWindow('MeetMe', cv2.WINDOW_AUTOSIZE)
        # Set window to fixed size
        cv2.setWindowProperty('MeetMe', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_AUTOSIZE)
        cv2.resizeWindow('MeetMe', 700, 350)  # Adjust the size as needed

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            cv2.imshow('MeetMe', frame)

            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Wait a sec and then close video / sync with audio
        time.sleep(1)
        cap.release()
        cv2.destroyAllWindows()
        # Audio stop
        pygame.mixer.music.stop()

    except Exception as e:
        print(f"Υπήρξε πρόβλημα στη προβολή του βίντεο: {e}")