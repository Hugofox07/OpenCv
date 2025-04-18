import cv2 as cv 
import numpy as np

path = 'imagem/visao_computacional.png'
img = cv.imread(path)
cv.imshow('Imagem', img)

# Using method Canny Edges
img_canny = cv.Canny(img, 25, 25) # Alternar a imagem como blur, grayscale.
cv.imshow('Canny_Image', img_canny)

# Using method Dilation image
img_dilated = cv.dilate(img_canny,(7,7), iterations=1) # Alternar a imagem como blur, grayscale.
cv.imshow('Dilate_Image', img_dilated)

# Using method Eroding
img_eroded = cv.erode(img_dilated,(3,3),iterations=1)# Alternar a imagem como blur, grayscale.
cv.imshow('Eroded_Image', img_eroded)
cv.waitKey(0)
cv.destroyAllWindows()