# Import libraries
import numpy as np
import cv2
from tkinter import filedialog
from scipy.ndimage import convolve

# Resizes image with factor scale_percent
def resize_img(matrix, scale_percent):
    # Decreases intensity to view image on 8-bit screen
    matrix = cv2.convertScaleAbs(matrix, alpha=0.25)

    width = int(matrix.shape[1] * scale_percent / 100)
    height = int(matrix.shape[0] * scale_percent / 100)
    dim = (width, height)

    resized = cv2.resize(matrix, dim, interpolation = cv2.INTER_AREA)

    return resized

# Calculates standard deviation of matrix
def std(matrix):
    list = np.matrix.flatten(matrix)

    std = np.std(list)

    return std

# Save image to disk
def savefile():
    filename = filedialog.asksaveasfile(mode='wb', defaultextension=".tif")
    if not filename:
        return
    img.save(filename)

# Segmentation of spots
def segmentation(matrix, x, y):
    num_spots = len(x)
    segments = []
    for i in range(0,num_spots):
        segments.append(matrix[y[i]-4:y[i]+5, x[i]-4:x[i]+5])
        
        #print(segments[i])

    return segments

