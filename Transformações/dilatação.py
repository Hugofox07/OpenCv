import cv2 as cv 
import numpy as np

path = 'imagem/pyramids.png'
img = cv.imread(path)
cv.imshow('Original', img)

# dilatando uma imagem
kernel = cv.getStructuringElement(cv.MORPH_RECT, (5,5))
imagem_dilatada = cv.dilate(img, kernel, iterations=1)
cv.imshow('Dilatação', imagem_dilatada)

cv.waitKey(0)
cv.destroyAllWindows()