# Import libraries
from PIL import Image
from numpy import asarray
import numpy as np
import cv2
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.inf)

added_matrix = np.zeros((256,256))

for n in range(1,2402):
    # Create grayscale matrix
    img_matrix = cv2.imread('Tubulins_I/'+str(n).zfill(5)+'.tif', cv2.IMREAD_UNCHANGED)

    min_intensity = 500

    for i in range(0,255):
            for j in range(0,255):
                if img_matrix[i][j] < min_intensity:
                    img_matrix[i][j] = 0

    added_matrix = added_matrix + img_matrix
        


# Create and show image from matrix
image = cv2.convertScaleAbs(added_matrix, alpha=0.22)
cv2.imshow("image", image)
cv2.waitKey()