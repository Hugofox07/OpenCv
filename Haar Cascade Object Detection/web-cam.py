import cv2 as cv 
import numpy as np

cap = cv.VideoCapture(0)  # 0 para webcam

while True:
    ret, frame = cap.read()
            
    cv.imshow('frame',frame)
    key = cv.waitKey(1)
    if key == 27:
        break

cap.realese() 
cv.destroyAllWindows()
