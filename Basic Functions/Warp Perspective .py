import cv2 as cv
import numpy as np

# Carregar a imagem
path = 'imagem/UnoCards.jpg'
image = cv.imread(path)

# Dimensão da imagem de saída
width, height = 300, 400

# Pontos da perspectiva original (manual ou via detecção)
points_original = np.float32([[669, 229], [797,292], [497, 367], [624, 440]])

# Pontos da visão transformada (destino)
points_destination = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

# Calcular a matriz de transformação
matrix = cv.getPerspectiveTransform(points_original, points_destination)

# Aplicar a transformação
warped_image = cv.warpPerspective(image, matrix, (width, height))

# Exibir os resultados
cv.imshow("Original", image)
cv.imshow("Warp Perspective", warped_image)
cv.waitKey(0)
cv.destroyAllWindows()