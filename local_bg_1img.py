# Import libraries
import numpy as np
import cv2
from functions import *

# Create grayscale matrix
img_src = 'Tubulins_I/00001.tif'
img_matrix = cv2.imread(img_src, cv2.IMREAD_UNCHANGED)

# Returns matrix with spots, background is removed. (second argument is stepsize)
spots_matrix = fcn_bg_intensity(img_matrix,16)

# Resizes image with a scaling factor (second argument)
resized_matrix = resize_img(spots_matrix, 100)

# Show image
cv2.imshow(img_src, resized_matrix)
cv2.waitKey()