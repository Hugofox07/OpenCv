import cv2 as cv
import numpy as np

path = 'imagem/obama.jpeg'
img = cv.imread(path)
print(img.shape)

# copy the rows and the columns of the  image 
tag = img[500:700, 600:900]
# Pasting the rows and columns in the image 
img[100:300, 650:950] = tag

cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()