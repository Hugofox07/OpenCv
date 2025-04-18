import numpy as np
import cv2 as cv

path = 'video/Lamborghini Aventador SVJ ALA.mp4'
cap = cv.VideoCapture(path)

while True:
    ret, frame = cap.read()
 
    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    cv.imshow('frame', frame)
    if cv.waitKey(30) == ord('q'):
        break
 
cap.release()
cv.destroyAllWindows()