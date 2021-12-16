# Import libraries
from PIL import Image
from numpy import asarray
import numpy as np
import cv2
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.inf)

# Create grayscale matrix
img_matrix = cv2.imread('Tubulins_I/00005.tif', cv2.IMREAD_UNCHANGED)

#### Show coordinates of high intensity spots
# top-left corner is (0,0)
# j = x, i = y
min_intensity = 600
k=0
for i in range(0,256):
        for j in range(0,256):
            if img_matrix[i][j] > min_intensity:
                k = k+1
                print("(%s, %s), intensity: %s" % (j, i, img_matrix[i][j]))
            else:
                img_matrix[i][j] = 0

# Print amount of high intensity spots
print("Amount of spots: %s" %k)

# Create and show image from matrix
image = cv2.convertScaleAbs(img_matrix, alpha=0.22)
cv2.imshow("image", image)
cv2.waitKey()






