import cv2 as cv 
import numpy as np 

path = 'imagem/visao_computacional.png'
img = cv.imread(path)
cv.imshow('Imagem', img)

# Using method flip 
# Use Flip code 0 to flip vertically image
img_flip = cv.flip(img, 1) # 0,-1,1
cv.imshow('Flipping', img_flip)

cv.waitKey(0)
cv.destroyAllWindows()