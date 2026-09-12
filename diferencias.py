import numpy as np
import matplotlib.pyplot as plt
import scipy as spy # optimización y ajuste de curvas, procesamiento de imagenes, AL avanzada, estadística, integración y EDOs.
from skimage import io # procesamiento de imágenes digitales. 

salon = io.imread('imagen_salon.png')

print(salon.shape)
plt.imshow(salon)

