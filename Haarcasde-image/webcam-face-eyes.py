import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

# Carregar o classificador Haar Cascade específico 
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')

while(True):
	ret, frame = cap.read()

	gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:

		# Draw rectangle shape
		cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

		# Gray scale image
		roi_gray = gray[y:y+h, x:x+w]

		# ROI(Region of Interest)
		roi_color = frame[y:y+h, x:x+w]
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for (ex,ey,ew,eh) in eyes:

			# Draw rectangle shape
			cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

     # Displayed the frame
	cv.imshow('frame',frame)

	# button esc to finishing the frame
	key = cv.waitKey(1)
	if key == 27:
		break

cap.release()
cv.destroyAllWindows()