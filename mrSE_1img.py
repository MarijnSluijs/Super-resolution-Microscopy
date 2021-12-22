# Import libraries
import numpy as np
import cv2
from functions import *
from fcn_deletevalues import *
from fcn_mrSE import *
from fcn_bg_intensity import *
from scipy.ndimage import convolve
from fcn_removecoords import *
import sympy as sym
np.seterr(divide='ignore', invalid='ignore')
x, y = sym.symbols('x y', real=True)

added_matrix = np.zeros((1280,1280))

# Create grayscale matrix
img_src = 'Tubulins_I/00033.tif'
img_matrix = cv2.imread(img_src, cv2.IMREAD_UNCHANGED)

# Returns matrix with spots, background is removed. (second argument is stepsize)
x_coordinates, y_coordinates = fcn_bg_intensity(img_matrix,16)

# Resizes image with a scaling factor (second argument)
resized_matrix = resize_img(img_matrix, 500)

# Delete double points
new_x, new_y = removecoords(x_coordinates,y_coordinates,img_matrix)

# Cut segments
segments = segmentation(img_matrix, new_x, new_y)

x_lst,y_lst = gradient_operator(segments, new_x, new_y)
x_img_lst = np.add(np.multiply(new_x,5),2+np.multiply(x_lst,5)).astype(int)
y_img_lst = np.add(np.multiply(new_y,5),2+np.multiply(y_lst,-5)).astype(int)

for i in range(0,len(x_lst)):
    resized_matrix[y_img_lst[i]][x_img_lst[i]]=255

# Show image
cv2.imshow(img_src, resized_matrix)
cv2.waitKey()

# coordinates for 1 segment
#x_img_lst = np.multiply(x_lst,10).astype(int)
#y_img_lst = np.multiply(y_lst,10).astype(int)


# Print segments
#for i in range(0,len(x_lst)):
  #  resized_segment = resize_img(segments[i], 1000)

  #  resized_segment[45-y_img_lst[i]][45+x_img_lst[i]]=255
  #  print(x_img_lst[i],y_img_lst[i])
    # Show image
   # cv2.imshow(img_src, resized_segment)
   # cv2.waitKey()