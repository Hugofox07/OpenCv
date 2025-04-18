import cv2 as cv
import numpy as np

# definindo as dimensao da imagem.
Largura = 640
Altura = 960

# The path of image.
path = 'imagem/obama.jpeg'
image = cv.imread(path)
print(image.shape)

#Resize the window
resize_image = cv.resize(image,(Largura,Altura))
print(resize_image.shape)

# Show the image and resize image 
cv.imshow('Original',image)
cv.imshow('Janela Resize', resize_image)
cv.waitKey(0)
cv.destroyAllWindows()