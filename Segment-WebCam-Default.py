# Visionoscope

from ultralytics import YOLO
import cv2

model = YOLO("../YOLO-Weights/yolov8n-seg.pt")

webcam = cv2.VideoCapture(0)
webcam.set(3, 640)
webcam.set(4, 480)

while True:
    success, image = webcam.read()
    if success:
        model(image, show=True)

    cv2.waitKey(1)