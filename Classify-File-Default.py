# Visionoscope

from tkinter.filedialog import askopenfilename
from ultralytics import YOLO
import cv2

model = YOLO('../YOLO-Weights/yolov8n-cls.pt')

image_path = askopenfilename()
model(image_path, show=True)

cv2.waitKey(0)