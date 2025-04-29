import cv2 as cv 
import numpy as np 

# Carregar os classificadores Haar Cascade para rosto e olhos
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
eyes_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')
image = cv.imread('Fotos/imagem7.jpg')
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray)

for (x, y, l, a) in faces:
    image = cv.rectangle(image,(x,y), (x + l, y + a), ( 0, 255, 0), 2)
    roi_gray = gray[y:y + a, x:x + l]
    roi_color = image[y:y + a, x:x + l]

eyes = eyes_cascade.detectMultiScale(roi_gray)
for(ox, oy, ol, oa) in eyes:
    cv.rectangle(roi_color,(ox, oy), (ox + ol, oy +oa), ( 255, 0, 255), 2)
        
# Mostrar a imagem com detecções
cv.imshow('face and eyes Detection', image)
cv.waitKey(0)
cv.destroyAllWindows()