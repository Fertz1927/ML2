import cv2
import numpy as np
from scipy.signal import convolve

# matrices
M1 = cv2.imread('res/left.png')
M2 = cv2.imread('res/right.png')

def primerpunto():
    diff = np.abs(M1.astype(np.int16) - M2.astype(np.int16))
    diff = diff.astype(np.uint8)

    cv2.imwrite('output/diferencia.png', diff)

def segundopunto():
    M1_float = cv2.cvtColor(M1,cv2.COLOR_BGR2GRAY).astype(np.float32)
    maximos = []

    for i in range(1,6):
        # kernel y centering
        kernel_obj = cv2.imread(f'res/Object-{i}.png', cv2.IMREAD_GRAYSCALE).astype(np.float32)
        kernel_obj_center = kernel_obj - np.mean(kernel_obj)

        # convolucion
        resultado = convolve(M1_float, np.flip(kernel_obj_center), mode='same')

        # normalizacion
        resultado = np.abs(resultado/np.max(resultado) * 255)
        maximos.append(np.unravel_index(np.argmax(resultado.astype(np.uint8)), resultado.shape))

        resultado = np.where(resultado > 200, resultado ** 5, 0)
        resultado = np.abs(resultado/np.max(resultado) * 255)

        resultado = resultado.astype(np.uint8)
        # escritura
        cv2.imwrite(f'output/diferencialol{i}.png', resultado)
        print(f'objeto {i} hecho!11!')

    for i in range(1, 6):
        nombre_obj = f'res/Object-{i}.png'
        objeto_gray = cv2.imread(nombre_obj, cv2.IMREAD_GRAYSCALE)

        # Buscar coincidencia en left.png
        (y, x) = maximos[i-1]
        (h, w) = objeto_gray.shape

        # Delimitar caja alrededor de la coordenada detectada
        top_left = (int(x - w / 2), int(y - h / 2))
        bottom_right = (int(x + w / 2), int(y + h / 2))

        # Dibujar rectángulo y puntaje de confianza
        cv2.rectangle(M1, top_left, bottom_right, (0, 255, 0), 2)
        cv2.putText(M1, f'Obj {i}',
                    (top_left[0], max(top_left[1] - 5, 12)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

    cv2.imwrite('output/objetos_encontrados.png', M1)

#primerpunto()
segundopunto()
