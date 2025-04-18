import cv2 as cv 
import numpy as np 

cap = cv.VideoCapture(0)

while True: 
    check, frame = cap.read()
    # show the frame in the webcam 
    cv.imshow('Frame', frame)

    # hsv frame  
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)  

    # Red mask color
    low_red = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])
    red_mask = cv.inRange(hsv_frame, low_red, high_red)
    red = cv.bitwise_and(frame, frame, mask=red_mask)
    # show the red bitwise of the frame
    #cv.imshow('Red', red)

    # Blue mask color
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])
    blue_mask = cv.inRange(hsv_frame, low_blue, high_blue)
    blue = cv.bitwise_and(frame, frame, mask=blue_mask)
    # show the red bitwise of the frame
    #cv.imshow('Blue', blue)

    # Green mask color
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])
    green_mask = cv.inRange(hsv_frame, low_green, high_green)
    green = cv.bitwise_and(frame, frame, mask=green_mask)
    # show the red bitwise of the frame
    #cv.imshow('Green', green) 
   
     # Every color except white
    low = np.array([0, 42, 0])
    high = np.array([179, 255, 255])
    mask = cv.inRange(hsv_frame, low, high)
    result = cv.bitwise_and(frame, frame, mask=mask)
    # show the red bitwise of the frame
    cv.imshow('Result', result) 
   
  # stoping the video press q 
    key = cv.waitKey(1) 
    if key == 27:
     break    

cap.release()
cv.destroyAllWindows()