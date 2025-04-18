import cv2 as cv 
import numpy as np 

#exibindo outra imagem 
img1 = cv.imread('imagem/visao_computacional.png')
img2 = cv.imread('imagem/visao_computacional.png')
print(img1.shape)
print(img2.shape)

# The image need to be the same size
img1 = cv.resize(img1, (0,0), None, 0.5, 0.5)
img2 = cv.resize(img2, (0,0), None, 0.5, 0.5)

# Position horizontal and vertical
hor = np.hstack((img1, img2))
ver = np.vstack((img1, img2))

# Show the image in horizontal and vertical
cv.imshow('Horizontal', hor)
cv.imshow('Vertical', ver)

cv.waitKey(0)
cv.destroyAllWindows()
