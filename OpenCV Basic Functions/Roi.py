import cv2 as cv 
import numpy as np

#path and read the image
img_path = 'imagem/thor.jpg'
img = cv.imread(img_path)
cv.imshow('Original_Image',img )

 # Resize img width, height
height = 640
width = 360
img_resize = cv.resize(img,(height,width))
cv.imshow('Resize_Image',img_resize)

# ROI(Region of Interest)
# Img coordinate(522:13) (770:292)
# Roi,[(y2:x2),(y1:x1)]
roi_img = img[13:292, 522:770] # storing your region of interest
cv.imshow('Region of Interest',roi_img)

cv.waitKey(0)
cv.destroyAllWindows()