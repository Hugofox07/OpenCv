import cv2 as cv 
import numpy as np 

# Carregar os classificadores Haar Cascade para rosto e olhos
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')

# Ler a imagem (substitua pelo caminho da sua imagem ou use a webcam)
path = 'Fotos/imagem3.jpg'
image = cv.imread(path) 

# Converter a imagem para escala de cinza
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  

# Detectar rostos
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

for (x, y, w, h) in faces:
# Desenhar um retângulo ao redor do rosto
    cv.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = image[y:y + h, x:x + w]

# Detectar olhos dentro da região do rosto
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
     cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

# Mostrar a imagem com detecções
cv.imshow('Deteccao de Olhos', image)
cv.waitKey(0)
cv.destroyAllWindows()