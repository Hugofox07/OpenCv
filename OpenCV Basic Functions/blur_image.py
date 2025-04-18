import cv2 as cv 
import numpy as np

path = 'imagem/visao_computacional.png'
img = cv.imread(path)
cv.imshow('Imagem', img)

# Using method Blur
img_blur = cv.GaussianBlur(img,(7,7),0)
cv.imshow('Blur_Image', img_blur)

cv.waitKey(0)
cv.destroyAllWindows()