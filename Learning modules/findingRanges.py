import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import hsv_to_rgb
#finding yellow

dark_orange =(30, 150, 150)
light_orange = (45, 255, 255)

lo_square = np.full((10, 10, 3), dark_orange, dtype='uint8') / 255.0
do_square = np.full((10, 10, 3), light_orange, dtype='uint8') / 255.0

plt.subplot(1, 2, 1)
plt.imshow(hsv_to_rgb(do_square))
plt.subplot(1, 2, 2)
plt.imshow(hsv_to_rgb(lo_square))
plt.show()
