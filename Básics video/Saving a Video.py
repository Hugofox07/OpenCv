import cv2 as cv 
import numpy as np

cap = cv.VideoCapture('video/Lamborghini Aventador SVJ ALA.mp4')

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('Lambo_output.avi', fourcc, 20.0, (640,480))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print('cant receive frame(stream end?). Exiting...')
        break
    frame = cv.flip(frame, 0)

# write the flipped frame
    out.write(frame)
    cv.imshow('frame', frame)
    if cv.waitkey(1) == ord('q'):
        break

# Release everything if job is finished
cap.release()
out.release()  
cv.destroyAllWindows()
