# import opencv and numpy
import cv2 as cv
import numpy as np

# Read an image 
image = cv.imread("imagem/starry_night.jpg")
# show the image
cv.imshow('img', image)
# print the channel of the image
print(image.shape)

# RGB to gray
gray_image = cv.cvtColor(image,(cv.COLOR_BGR2GRAY))
# show the image
cv.imshow('Gray_Image', gray_image)

# Save image
cv.imwrite('Save_Image/starry_night_gray.png', gray_image) 

# show the image

cv.waitKey(0)
cv.destroyAllWindows()