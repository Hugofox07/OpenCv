import cv2 as cv
import numpy as np 


path = 'imagem/elon.jpeg'
img = cv.imread(path)

cv. imshow('COLOR_Bgr', img)


# Gray scale
img_gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv. imshow('COLOR_Gray', img_gray)

# Rgb scale 
img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('COLOR_Rgb', img_rgb)

cv.waitKey(0)
cv.destroyAllWindows()
