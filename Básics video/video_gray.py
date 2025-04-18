import cv2 as cv
import numpy as np

video = cv.VideoCapture('video/Lamborghini Revuelto.mp4')

while True:
    ret, frame = video.read()
    frame2 = cv.flip(frame, 0)
 
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
 
 # Show the video in gray and colors
    cv.imshow('Original', frame)
    cv.imshow('Gray_frame', gray)
    cv.imshow('Fipping', frame2)

    if cv.waitKey(30) == ord('q'):
        break
    
video.release()
cv.destroyAllWindows()