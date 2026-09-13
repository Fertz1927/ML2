import cv2
import numpy as np

# primer punto
M1 = cv2.imread('left.png').astype(np.int16)
M2 = cv2.imread('right.png').astype(np.int16)

diff = np.abs(M1 - M2)
diff = diff.astype(np.uint8)

cv2.imwrite('diferencia.png', diff)
