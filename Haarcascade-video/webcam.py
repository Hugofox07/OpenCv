import cv2 as cv 
import numpy as np 

webcamera = cv.VideoCapture(0)

# Loop while
while True:

    camera, frame = webcamera.read()

# Displayed the frame
    cv.imshow('Webcam-Image', frame) 

# button esc to finishing the frame
    if cv.waitKey(1) == ord('f'):
        break

  
webcamera.release()
cv.destroyAllWindows()    