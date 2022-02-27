# add_images.py

# This program adds all images in the dataset, to show what image could be made with a normal microscope.

# Import libraries
import cv2
import timeit
import numpy as np
from PIL import Image
import multiprocessing
from datetime import datetime
from functools import partial

# Import functions
from fcn_resize_img import *

choose_dataset=1
if choose_dataset==1 or choose_dataset==2:
    total = 2401
else:
    total = 8000

n=1
# Convert image to matrix
if choose_dataset==1:
    img_matrix1 = cv2.imread('Tubulins_I/'+str(n).zfill(5)+'.tif', cv2.IMREAD_UNCHANGED)
elif choose_dataset==2:
    img_matrix1 = cv2.imread('Tubulins_II/'+str(n).zfill(5)+'.tif', cv2.IMREAD_UNCHANGED)
else:
    img_matrix1 = cv2.imread('Tubulins_SOFI/'+str(n)+'.tif', cv2.IMREAD_UNCHANGED)

for n in range(2,total+1):
    print(n,'/', total ,'images analyzed')

    # Convert image to matrix
    if choose_dataset==1:
        img_matrix = cv2.imread('Tubulins_I/'+str(n).zfill(5)+'.tif', cv2.IMREAD_UNCHANGED)
    elif choose_dataset==2:
        img_matrix = cv2.imread('Tubulins_II/'+str(n).zfill(5)+'.tif', cv2.IMREAD_UNCHANGED)
    else:
        img_matrix = cv2.imread('Tubulins_SOFI/'+str(n)+'.tif', cv2.IMREAD_UNCHANGED)

    if choose_dataset==1:
        for i in range(0,256):
            for j in range(0,256):
                if img_matrix[j][i] > img_matrix1[j][i]:
                    img_matrix1[j][i] = img_matrix[j][i]
    elif choose_dataset==2:
        for i in range(0,256):
            for j in range(0,256):
                if img_matrix[j][i] > img_matrix1[j][i]:
                    img_matrix1[j][i] = img_matrix[j][i]
    else:
        for i in range(0,500):
            for j in range(0,500):
                if img_matrix[j][i] > img_matrix1[j][i]:
                    img_matrix1[j][i] = img_matrix[j][i]

img_resized = resize_img(img_matrix1,500)

img_saved = Image.fromarray(img_resized)
img_saved.save("images/images_added_resized.tif")
