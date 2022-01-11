import cv2
import numpy as np
from PIL import Image
# load image as grayscale
#img = cv2.imread('images/Tubulins_I_colordepth.tif', cv2.IMREAD_UNCHANGED)
w, h = 512, 512
data = np.zeros((h, w, 3), dtype=np.uint8)
data[0:256, 0:256] = [255, 0, 0] # red patch in upper left
img = Image.fromarray(data, 'RGB')
img.save('my.png')
img.show()