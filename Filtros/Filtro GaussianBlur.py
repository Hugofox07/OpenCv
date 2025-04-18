import cv2 as cv 
import numpy as np

path = 'visao_computacional.png'
img = cv.imread(path)
cv.imshow('Original',img)

#-Filtro GaussianBlur
filter_gaugaussian = cv.GaussianBlur(src=img,ksize=(13,13),sigmaX=0)
cv.imshow('Filter_Gaugaussian',filter_gaugaussian)
cv.waitKey()
cv.destroyAllWindows()