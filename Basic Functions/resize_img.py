import cv2 as cv
import numpy as np

path = 'imagem/visao_computacional.png'
img = cv.imread(path)
cv.imshow('Imagem', img)

img_resized = cv.resize(img, (400,400), cv.INTER_CUBIC)
cv.imshow('Resize_Image', img_resized)

cv.waitKey(0)
cv.destroyAllWindows()