# compare_images.py

# This program adds the super-resolution image to the image as seen by the normal microscope.

# Import libraries
import cv2
import timeit
import numpy as np
from PIL import Image
import multiprocessing
from datetime import datetime
from functools import partial

img_matrix1 = cv2.imread('Tubulins_I_normalmicroscope.jpg')
img_matrix2 = cv2.imread('phasorfitting_mp_Tubulins_I_colored.tiff')
img_matrix3 = cv2.imread('Tubulins_SOFI_normalmicroscope.jpg')
img_matrix4 = cv2.imread('phasorfitting_mp_Tubulins_SOFI_colored.tiff')

for i in range(0,1280):
    for j in range(0,1280):
        if img_matrix2[i][j][0] > 0:
            img_matrix1[i][j] = img_matrix2[i][j]

for i in range(0,2500):
    for j in range(0,2500):
        if img_matrix4[i][j][0] > 0:
            img_matrix3[i][j] = img_matrix4[i][j]

img_saved = Image.fromarray(img_matrix1)
img_saved.save("images/images_compared_Tubulins_I.tif")

img_saved = Image.fromarray(img_matrix3)
img_saved.save("images/images_compared_Tubulins_SOFI.tif")