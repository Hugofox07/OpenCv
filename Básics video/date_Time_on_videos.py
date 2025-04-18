import cv2 as cv 
import numpy as np
import datetime

capture = cv.VideoCapture(0)
# show the width and the height of the video 
print(capture.get(cv.CAP_PROP_FRAME_WIDTH))
print(capture.get(cv.CAP_PROP_FRAME_HEIGHT))

# Change the width and the height of the video 
#capture.set(3,3000)
#capture.set(4,720)
#print(capture.get(3))
#print(capture.get(4))

# Color of the text
red = (0, 0, 255)

while True:
    ret, frame = capture.read()
 
# Putting tex in videos 
    font = cv.FONT_HERSHEY_SIMPLEX
    text = 'Width: ' + str(capture.get(3))  +  ' Height: ' + str(capture.get(4))
    datet = str(datetime.datetime.now())
    frame = cv.putText(frame, datet, (10,50), font, 1, red, 2,  cv.LINE_AA )

# show the image with text
    cv.imshow('frame', frame)
    if cv.waitKey(30) == ord('q'):
        break
 
capture.release()
cv.destroyAllWindows()