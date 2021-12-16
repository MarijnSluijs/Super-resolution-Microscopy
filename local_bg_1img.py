# Import libraries
import numpy as np
import cv2
from functions import *
from fcn_deletevalues import *
from fcn_mrSE import *
from fcn_bg_intensity import *
from scipy.ndimage import convolve
np.seterr(divide='ignore', invalid='ignore')

# Create grayscale matrix
img_src = 'Tubulins_I/00001.tif'
img_matrix = cv2.imread(img_src, cv2.IMREAD_UNCHANGED)
img_matrix2 = cv2.imread(img_src, cv2.IMREAD_UNCHANGED)

#with open('outfile.txt','wb') as f:
#   for line in img_matrix:
#       np.savetxt(f, img_matrix, fmt='%.0f')

# Returns matrix with spots, background is removed. (second argument is stepsize)
spots_matrix, x_coordinates, y_coordinates = fcn_bg_intensity(img_matrix,16)

# Resizes image with a scaling factor (second argument)
resized_matrix = resize_img(spots_matrix, 100)

# Delete dubble points
new_x, new_y = deletevalues(x_coordinates,y_coordinates)

# Cut segments
segments = segmentation(img_matrix2, new_x, new_y)

gradient_operator(segments, new_x, new_y)
# Show image
#cv2.imshow(img_src, resized_matrix)
#cv2.waitKey()