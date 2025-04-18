import cv2 as cv
import numpy as np

# Carrega a imagem
path = 'imagem/dog.jpeg'
img = cv.imread(path)

# Define um kernel (3x3 média)
kernel = np.ones((3,3), np.float32) / 9

# Aplica o filtro
img_filtrada = cv.filter2D(img, -1, kernel)

cv.imshow('Original', img)
cv.imshow('Filtrada com Kernel 3x3', img_filtrada)
cv.waitKey(0)
cv.destroyAllWindows()