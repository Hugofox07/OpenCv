import cv2 as cv
import numpy as np 

# Load an image
image = cv.imread('imagem/red_panda.jpg')

# Define the callback function
def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:  # Left mouse button click
        print(f"Left click at: ({x}, {y})")
        cv.circle(image, (x, y), 5, (255, 0, 0), -1)  # Draw a circle
        cv.imshow("Interactive Image", image)

    elif event == cv.EVENT_RBUTTONDOWN:  # Right mouse button click
        print(f"Right click at: ({x}, {y})")
        text = f"{x}, {y}"
        cv.putText(image, text, (x, y), cv.FONT_HERSHEY_SIMPLEX, 
                    0.5, (0, 255, 0), 1)  # Write coordinates
        cv.imshow("Interactive Image", image)

# Bind callback function to window
cv.namedWindow("Interactive Image")
cv.setMouseCallback("Interactive Image", click_event)

# Display image and wait for interactions
while True:
    cv.imshow("Interactive Image", image)
    if cv.waitKey(1) & 0xFF == 27:  # Exit on 'ESC' key
        break

cv.destroyAllWindows()