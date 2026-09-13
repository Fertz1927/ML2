import cv2
import numpy as np

# primer punto
M1 = cv2.imread('left.png')
M2 = cv2.imread('right.png')

diff = np.abs(np.round(M1/2) - np.round(M2/2))
diff = diff.astype(np.uint8)

cv2.imwrite('diferencia.png', diff)

# segundo punto
