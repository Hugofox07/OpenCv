import cv2 as cv
import numpy as np

red = (0, 0, 255)

# Carregar os classificadores HaarCascade para rosto
carregaAlgoritimo = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Carregando a imagem
path = 'Fotos/imagem1.jpg'
img = cv.imread(path)

img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

faces = carregaAlgoritimo.detectMultiScale(img_gray)
print(faces)

for (x, y, l, a) in faces:
    cv.rectangle(img, (x, y), (x + l, y + a), red, 2)

# Show the image
cv.imshow('faces', img)
cv.waitKey(0)
cv.destroyAllWindows()