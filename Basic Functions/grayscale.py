import cv2 as cv
import numpy as np 

path = 'imagem/elon.jpeg'
img = cv.imread(path)
cv.imshow('Original', img)

#-Gray scale image
gray_image = cv.cvtColor(img,(cv.COLOR_BGR2GRAY))
cv.imshow('Gray_Image', gray_image)

cv.waitKey(0)
cv.destroyAllWindows()