import cv2 as cv 
import numpy as np

path = 'imagens/baboon.jpg'
image = cv.imread(path)
cv.imshow('Original', image)

#-Gray scale image
gray_image = cv.cvtColor(image,(cv.COLOR_BGR2GRAY))
cv.imshow('Gray_Image', gray_image)

sobelx = cv.Sobel(image, cv.CV_64F, 1, 0, ksize=5)  # horizontal
sobely = cv.Sobel(image, cv.CV_64F, 0, 1, ksize=5)  # vertical

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.waitKey(0)
cv.destroyAllWindows()
