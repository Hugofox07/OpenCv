import cv2 as cv 
import numpy as np

# Loading image from memory
path = 'imagem/fluxograma para opencv.png'
image = cv.imread(path)

#Define the kernel 
kernel = np.ones((9,9), np.uint8)

#Dilatation the image
dilation = cv.dilate(image, kernel, iterations = 1)

#Erosion the image 
eroded = cv.erode(image, kernel, iterations = 1)

# Showing the image
cv.imshow('Original_Image', image)
cv.imshow('Dilation_Image', dilation)
cv.imshow('Eroded_Image', eroded)

# WaitKey to be press
cv.waitKey(0)
cv.destroyAllWindows()

