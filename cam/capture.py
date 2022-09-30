import cv2
import numpy as np
cap = cv2.VideoCapture(0)

ret, frame = cap.read()
cv2.imshow('frame', frame)
img_name = "opencv_frame.png"
cv2.imwrite(img_name, frame)

cap.release()