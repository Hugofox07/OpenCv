import cv2 as cv 
import numpy as np

cap = cv.VideoCapture(0)  # 0 para webcam

while True:
    ret, frame = cap.read()
    if not ret:
        break

# webcam mostra o video cinza 
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('Vídeo em Escala de Cinza', gray)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.imshow('Imagem', cap)   
cap.realese() 
cv.destroyAllWindows()
