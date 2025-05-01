import cv2 as cv 
import numpy as np

azul = (255, 0, 0)

webcam = cv.VideoCapture(0)
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = webcam.read()

    cinza = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    detecta = face_cascade.detectMultiScale(cinza)

    for(x, y, l, a) in detecta:
        cv.rectangle(frame, (x, y), (x + l, y + a), azul, 2)

    cv.imshow('VideoWebCam', frame)

# button esc to finishing the frame
    key = cv.waitKey(1)
    if key == 27:
     break

webcam.release()
cv.destroyAllWindows()