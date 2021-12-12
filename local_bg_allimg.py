# Import libraries
import numpy as np
import cv2
from functions import *

added_matrix = np.zeros((256,256))

for n in range(1,10):
    # Create grayscale matrix
    img_matrix = cv2.imread('Tubulins_I/'+str(n).zfill(5)+'.tif', cv2.IMREAD_UNCHANGED)

    # Returns matrix with spots, background is removed. (second argument is stepsize)
    spots_matrix = fcn_bg_intensity(img_matrix,16)
    added_matrix = added_matrix + spots_matrix
    
# Resizes image with a scaling factor (second argument)
resized_matrix = resize_img(added_matrix, 200)

#Show image
cv2.imshow("local_bg_allimg", resized_matrix)
cv2.waitKey()