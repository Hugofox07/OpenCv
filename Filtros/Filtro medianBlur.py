import cv2 as cv
import numpy as np 

path = 'imagem/visao_computacional.png'
imagem = cv.imread(path)
cv.imshow('Original', imagem)

# Filtro medianBlur deve ser um valor ímpar
median_Blur = cv.medianBlur(imagem,11)
cv.imshow('Janela_MedianBlur', median_Blur)
cv.waitKey()
cv.destroyAllWindows()