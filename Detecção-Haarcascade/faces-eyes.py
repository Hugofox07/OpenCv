import cv2 as cv 
import numpy as np 

# Carregar os classificadores Haar Cascade para rosto e olhos
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')

# Inicializar a captura de vídeo (0 para webcam padrão)
cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Erro: Não foi possível acessar a webcam.")
    exit()

while True:
    # Capturar frame da webcam
    ret, frame = cap.read()
    if not ret:
        print("Erro: Não foi possível capturar frame.")
        break

    # Converter o frame para escala de cinza
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detectar rostos no frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Desenhar um retângulo ao redor do rosto
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detectar olhos dentro da região do rosto
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    # Exibir o frame com as detecções
    cv.imshow('Detecção de Olhos - Webcam', frame)

    # Pressione 'q' para sair
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a webcam e fechar janelas
cap.release()
cv.destroyAllWindows()
