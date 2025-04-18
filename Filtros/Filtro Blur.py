import cv2 as cv
import numpy as np

path = 'visao_computacional.png'
img = cv.imread(path)
cv.imshow('Original', img)

#-Filter Blur
filter_blur = cv.blur(img, ksize= (3,3)) 
cv.imshow('Filter_blur',filter_blur)
cv.waitKey()
cv.destroyAllWindows()