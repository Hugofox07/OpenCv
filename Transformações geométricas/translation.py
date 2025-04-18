import cv2 as cv 
import numpy as np 

# Carregar imagem
path = 'imagem/baboon.jpg'
image = cv.imread(path)

# Definir deslocamento (tx, ty)
tx, ty = 50, 100  # Move 50 pixels para a direita e 100 pixels para baixo

# Criar matriz de translação (x=50, y=30)
M = np.float32 ([[1,0,100], [0,1,50]])

# Obter dimensões da imagem
rows, cols = image.shape[:2]

# Aplicar transformação
translation = cv.warpAffine(image, M, (cols,rows))

# Mostrar resultado
cv.imshow('Original',image)
cv.imshow('Translation_image', translation)
cv.waitKey(0)
cv.destroyAllWindows()