import cv2
import numpy as np
from scipy.ndimage import convolve

M1 = cv2.imread('left.png')
M2 = cv2.imread('right.png')

def primerpunto():
    diff = np.abs(M1.astype(np.int16) - M2.astype(np.int16))
    diff = diff.astype(np.uint8)

    cv2.imwrite('diferencia.png', diff)

def segundopunto():
    for i in range(1,6):
        kernel = (cv2.imread(f'Object-{i}.png').astype(np.float32))
        resultado = convolve(M1.astype(np.float32), kernel)
        resultado = resultado/np.max(resultado) * 255
        resultado = resultado.astype(np.uint8)

        cv2.imwrite(f'diferencia{i}.png', resultado)
        print(f'objeto {i} hecho!11!')

segundopunto()
