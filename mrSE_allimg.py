# Import libraries
import cv2
import timeit
import numpy as np
from PIL import Image
from fcn_mrSE import *
from functions import *
from fcn_bg_intensity import *
from fcn_removecoords import *
from fcn_segmentation import *

np.seterr(divide='ignore', invalid='ignore')

start = timeit.default_timer()

added_matrix = np.zeros((1280,1280))

total = 3
for n in range(1,total+1):
    print(n,'/',total,'images')
    # Create grayscale matrix
    img_matrix = cv2.imread('Tubulins_I/'+str(n).zfill(5)+'.tif', cv2.IMREAD_UNCHANGED)

    # Returns coordinates of spots (second argument is stepsize)
    x_coordinates, y_coordinates = fcn_bg_intensity(img_matrix,16)

    # Delete double points
    new_x, new_y = removecoords(x_coordinates,y_coordinates,img_matrix)

    # Cut segments
    segments = segmentation(img_matrix, new_x, new_y)

    x_lst,y_lst = gradient_operator(segments, new_x, new_y)
    x_img_lst = np.add(np.multiply(new_x,5),2+np.multiply(x_lst,5)).astype(int)
    y_img_lst = np.add(np.multiply(new_y,5),2+np.multiply(y_lst,-5)).astype(int)

    for i in range(0,len(x_lst)):
        added_matrix[y_img_lst[i]][x_img_lst[i]]=255

  

# Save and show image
img_saved = Image.fromarray(added_matrix)
img_saved.save("images/mrSE_allimg.tif")


