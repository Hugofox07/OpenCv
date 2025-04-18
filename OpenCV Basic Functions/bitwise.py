import cv2 as cv 
import numpy as np 

path = 'imagem/drawing_1.png'
path2 = 'imagem/drawing_2.png'
img1 = cv.imread(path)
img2 = cv.imread(path2)

# Bitwise Operators
bit_and = cv.bitwise_and(img1, img2)
bit_or = cv.bitwise_or(img1, img2)
bit_xor = cv.bitwise_xor(img1, img2)
bit_not = cv.bitwise_not(img1, img2)

cv.imshow('Img1', img1)
cv.imshow('img2', img2)
cv.imshow('Bit_and', bit_and)
cv.imshow('Bit_or', bit_or)
cv.imshow('Bit_xor', bit_xor)
cv.imshow('Bit_not', bit_not)

cv.waitKey(0)
cv.destroyAllWindows()
