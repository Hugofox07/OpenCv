import cv2 as cv 
import numpy as np 

path = 'imagem/visao_computacional.png'
img = cv.imread(path)
cv.imshow('Imagem', img)


# Using img_cropped = img[] method 
img_cropped = img[200:400, 200:500]
cv.imshow('Cropped_Image', img_cropped)

cv.waitKey(0)
cv.destroyAllWindows()
