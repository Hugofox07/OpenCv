import cv2 as cv 
import numpy as np

path = 'imagem/visao_computacional.png'
img = cv.imread(path)
cv.imshow('Imagem', img)

# Using method Canny Edges
img_canny = cv.Canny(img, 25, 25) # Alternar a imagem como blur, grayscale.
cv.imshow('Canny_Image', img_canny)

cv.waitKey(0)
cv.destroyAllWindows()