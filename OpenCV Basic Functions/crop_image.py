import cv2 as cv 
import numpy as np 

path = 'imagem/sudoku-game.png'
img = cv.imread(path)
print(img.shape)

# Cropping the image 
cropped_img = img[50:804, 300:800]
print(cropped_img.shape)

cv.imshow('Original', img)
cv.imshow('Crop_Image', cropped_img)

cv.waitKey(0)
cv.destroyAllWindows()
