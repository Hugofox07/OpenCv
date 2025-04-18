import cv2 as cv 
import numpy as np

# Loading image from memory
path = 'imagem/messi5.jpg'
img = cv.imread(path)

# Showing the image 
cv.imshow('Original_Image', img)

height, width = img.shape[:2]

# Translation matrix
matrix = cv.getRotationMatrix2D((width/2,height/2), 10, 1)

# Applying the matrix to the image
translated_img = cv.warpAffine(img, matrix,(width,height))

#- Rotate the image
rotate_image = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
cv.imshow('Rotate_image', rotate_image)

# Showing the image 
cv.imshow('Translation_Image', translated_img)
cv.waitKey(0)
cv.destroyAllWindows(0)