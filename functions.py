# Import libraries
import cv2
import numpy as np
from tkinter import filedialog

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

