import cv2 as cv 
import numpy as np

camera = cv.VideoCapture(0)

while True:
    check,img = camera.read()
cv.imshow('Imagem', img)   
cv.waitKey(1) 
cv.destroyAllWindows()
