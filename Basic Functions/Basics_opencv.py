import cv2 as cv 
import numpy as np

#Use the kernel
#kernel = np.ones((5,5),np.uint8)
#print(kernel)

path = 'imagem/visao_computacional.png'
img = cv.imread(path)
cv.imshow('Imagem', img)

# Using method Grayscale 
gray_img = cv.cvtColor(img,(cv.COLOR_BGR2GRAY))
cv.imshow('GRAY_Image', gray_img)

# Using method Blur
img_blur = cv.GaussianBlur(img,(7,7),0)
cv.imshow('Blur_Image', img_blur)

# Using method Canny Edges
img_canny = cv.Canny(img, 25, 25) # Alternar a imagem como blur, grayscale.
cv.imshow('Canny_Image', img_canny)

# Using method Dilation image
# img_dilated = cv.dilate(img_canny,kernel, iterations=1)
img_dilated = cv.dilate(img_canny,(7,7), iterations=1) # Alternar a imagem como blur, grayscale.
cv.imshow('Dilate_Image', img_dilated)

# Using method Eroding
img_eroded = cv.erode(img_dilated,(3,3),iterations=1)# Alternar a imagem como blur, grayscale.
cv.imshow('Eroded_Image', img_eroded)

# Using method Resize
img_resized = cv.resize(img, (400,400), cv.INTER_CUBIC)
cv.imshow('Resize_Image', img_resized)

# Using img_cropped = img[] method 
img_cropped = img[200:400, 200:500]
cv.imshow('Cropped_Image', img_cropped)

# Using method flip 
# Use Flip code 0 to flip vertically image
img_flip = cv.flip(img, 1) # 0,-1,1
cv.imshow('Flipping', img_flip)

cv.waitKey(0)
cv.destroyAllWindows()