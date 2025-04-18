import cv2 as cv 
import numpy as np 

# read the webcam 
capture = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVDI')
out = cv.VideoWriter('video/flipped_webcam.mp4', fourcc, 20.0, (604, 480))


while True: 
  ret, frame = capture.read()

  print(frame.shape)

  frame2 = cv.flip(frame, 1)
   
 # show the image in the webcam 
  cv.imshow('Video', frame)
  cv.imshow('frame', frame2)

  out.write(frame2)
   
  # stoping the video press q 
  key = cv.waitKey(30) 
  if key == 27:
    break    

out.release()
capture.release()
cv.destroyAllWindows()