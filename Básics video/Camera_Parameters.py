import cv2 as cv 
import numpy as np 

# read the webcam 
capture = cv.VideoCapture(0)

# show the width and the height of the video 
print(capture.get(cv.CAP_PROP_FRAME_WIDTH))
print(capture.get(cv.CAP_PROP_FRAME_HEIGHT))

# Change the width and the height of the video 
capture.set(3,3000)
capture.set(4,720)
print(capture.get(3))
print(capture.get(4))

# Loop
while True: 
    check, frame = capture.read()
    gray_scale = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
  
 # show the frame in the webcam 
    cv.imshow('Video', frame)
    cv.imshow('Video_Gray', gray_scale)
   
  # stoping the video press q 
    key = cv.waitKey(1) 
    if key == 27:
     break    

capture.release()
cv.destroyAllWindows()