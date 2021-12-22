# Import libraries
import numpy as np
import cv2
from functions import *
from fcn_deletevalues import *
from fcn_mrSE import *
from fcn_bg_intensity import *
from scipy.ndimage import convolve
import sympy as sym
from fcn_removecoords import *
np.seterr(divide='ignore', invalid='ignore')
x, y = sym.symbols('x y', real=True)
import timeit

start = timeit.default_timer()

added_matrix = np.zeros((1280,1280))
total = 100
for n in range(1,total+1):
    print(n,'/',total,'images')
    # Create grayscale matrix
    img_matrix = cv2.imread('Tubulins_I/'+str(n).zfill(5)+'.tif', cv2.IMREAD_UNCHANGED)

    # Returns matrix with spots, background is removed. (second argument is stepsize)
    x_coordinates, y_coordinates = fcn_bg_intensity(img_matrix,16)

    # Resizes image with a scaling factor (second argument)
    #resized_matrix = resize_img(img_matrix, 500)

    # Delete double points
    new_x, new_y = removecoords(x_coordinates,y_coordinates,img_matrix)

    # Cut segments
    segments = segmentation(img_matrix, new_x, new_y)

    x_lst,y_lst = gradient_operator(segments, new_x, new_y)
    x_img_lst = np.add(np.multiply(new_x,5),2+np.multiply(x_lst,5)).astype(int)
    y_img_lst = np.add(np.multiply(new_y,5),2+np.multiply(y_lst,-5)).astype(int)

    for i in range(0,len(x_lst)):
        added_matrix[y_img_lst[i]][x_img_lst[i]]=255

stop = timeit.default_timer()

print('Time: ', int((stop - start)/60), 'minutes')  

#Show image
cv2.imshow("local_bg_allimg", added_matrix)
cv2.waitKey()

