# fcn_resize_img.py

# This functions resizes a matrix to make the resulting better visible on a screen

# Import libraries
import cv2

# Resizes image with factor scale_percent
def resize_img(matrix, scale_percent):
    # Decreases intensity to view image on 8-bit screen
    #matrix = cv2.convertScaleAbs(matrix, alpha=0.25)

    width = int(matrix.shape[1] * scale_percent / 100)
    height = int(matrix.shape[0] * scale_percent / 100)
    dim = (width, height)

    resized = cv2.resize(matrix, dim, interpolation = cv2.INTER_AREA)

    return resized