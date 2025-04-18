import cv2 as cv 
import numpy as np

path = 'imagem/baboon.jpg'
image = cv.imread(path)
cv.imshow('Original', image)

#-Gray scale image
gray_image = cv.cvtColor(image,(cv.COLOR_BGR2GRAY))
cv.imshow('Gray_Image', gray_image)

#-Filtro GaussianBlur
blur_image = cv.bilateralFilter(image, 7, 75, 75)
cv.imshow('Blur_Image', blur_image)

#-Canny edge detection: 100 = limiar inferior, 200 = limiar superior.
edges = cv.Canny(blur_image, 100, 200)
cv.imshow('Edges_Image', edges)

cv.waitKey(0)
cv.destroyAllWindows()