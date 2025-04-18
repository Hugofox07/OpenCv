import cv2 as cv
import numpy as np 

path = 'imagem/baboon.jpg'
image = cv.imread(path)
cv.imshow('Original', image)

#- Rotate the image
rotate_image = cv.rotate(image, cv.ROTATE_90_CLOCKWISE)
cv.imshow('Rotate_image', rotate_image)

# Save the image
cv.imwrite('Save_Image/baboon.png', rotate_image)

cv.waitKey(0)
cv.destroyAllWindows()