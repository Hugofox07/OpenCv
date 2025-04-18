import cv2 as cv 
import numpy as np 

cap_video = cv.VideoCapture(0)
lar = 480
alt = 320

while True: 
    ret, video = cap_video.read()

    videoRed = cv.resize(video, (lar,alt))
    video_cinza = cv.cvtColor(videoRed, cv.COLOR_BGR2GRAY)

    cv.imshow('Video', videoRed)
    cv.imshow('VideoGray', video_cinza)
    key = cv.waitKey(1) & 0xFF

    if key == ord('a'):
        break

cap_video.release()
cv.destroyAllWindows()
