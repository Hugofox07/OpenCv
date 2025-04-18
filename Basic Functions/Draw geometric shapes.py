import cv2 as cv
import numpy as np

# Create the black image
image = np.zeros([800, 800, 3], np.uint8)
print = (image.shape)

# green
# image[:] = 0, 255, 0
# blue
# image[:] = 255, 0, 0
# red
# image[:] = 0, 0, 255

# Colors of geometric shapes
green = (0, 255, 0)
blue = (255, 0, 0)
red = (0, 0, 255)
yellow = (0, 255, 255)
white = (255, 255, 255)

# Draw geometric shapes
line = cv.line(image, (0, 0), (255, 255), green, 3)
arrowedLine = cv.arrowedLine(image, (0, 255), (255, 255), blue, 3)
rectangle = cv.rectangle(image, (385, 0), (510, 128), red, 3)#-1
circle = cv.circle(image, (447,63), 63, yellow, 3)#-1 center point(447,63),radius(63)

 # Put text in image
font = cv.FONT_HERSHEY_SIMPLEX
line_type = cv.LINE_AA
position_text = 10,500
text = cv.putText(image,'God is Good',position_text, font, 3, white, 10, line_type)

# Show the image 
cv.imshow('Black', image)

# Close the window
cv.waitKey(0)
cv.destroyAllWindows()