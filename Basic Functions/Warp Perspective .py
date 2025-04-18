import cv2 as cv
import numpy as np

path = 'imagem/UnoCards.jpg'
img = cv.imread(path)
cv.imshow('Imagem', img)






cv.waitKey(0)
cv.destroyAllWindows()