# Import libraries
import numpy as np
import cv2
from tkinter import filedialog

# Returns matrix with spots, background is removed.
def fcn_bg_intensity(matrix, stepsize):

    # Determine spots in small area
    xpos = stepsize
    ypos = stepsize
    sum = 0

    for y_shift in range(0,int(256/stepsize)):
        for x_shift in range(0,int(256/stepsize)):

            # Determine background intensity in small area
            for x in range(xpos-stepsize,xpos):
                for y in range(ypos-stepsize,ypos):
                    sum += matrix[y][x]


            bg_intensity = sum/(stepsize*stepsize)
            img_std = std(matrix)

            # Remove background noise
            for x in range(xpos-stepsize,xpos):
                for y in range(ypos-stepsize,ypos):
                    if matrix[y][x] >= bg_intensity + 2*img_std:
                        print("(%s, %s)" % (x, y))
                    else:
                        matrix[y][x] = 0
        
            xpos += stepsize
            sum = 0

        ypos += stepsize
        xpos = stepsize

    return matrix

# Resizes image with factor scale_percent
def resize_img(matrix, scale_percent):
    # Decreases intensity to view image on 8-bit screen
    matrix = cv2.convertScaleAbs(matrix, alpha=0.25)

    width = int(matrix.shape[1] * scale_percent / 100)
    height = int(matrix.shape[0] * scale_percent / 100)
    dim = (width, height)

    resized = cv2.resize(matrix, dim, interpolation = cv2.INTER_AREA)

    return resized


def std(matrix):
    list = np.matrix.flatten(matrix)

    std = np.std(list)

    return std