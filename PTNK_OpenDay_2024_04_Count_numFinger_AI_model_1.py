import cv2
import mediapipe as mp
import HandtrackingModule as htm

# Constants for colours and camera size
BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
wCam, hCam = 640, 480

# Camera configuration
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

# Initialising the handheld detector
detector = htm.HandDetector(detectionCon=0.7)
numberOfFingers = 0

