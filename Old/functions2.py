# Import libraries
import numpy as np
import cv2
from tkinter import filedialog
from scipy.ndimage import convolve

# Returns matrix with spots, background is removed.
def fcn_bg_intensity(matrix, stepsize):

    x_coordinates = []
    y_coordinates = []
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
                    if matrix[y][x] >= bg_intensity + 3*img_std:
                        x_coordinates.append(x)
                        y_coordinates.append(y)
                    else:
                        matrix[y][x] = 0
        
            xpos += stepsize
            sum = 0

        ypos += stepsize
        xpos = stepsize

   
    return matrix, x_coordinates, y_coordinates

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


def segmentation(matrix, x, y):
    num_spots = len(x)
    segments = []
    for i in range(0,num_spots):
        segments[i] = matrix[y[i]-4:y[i]+5, x[i]-4:x[i]+5]
        print(segments[i])

    return segment

def gradient_operator(segment, x, y):
    # Define Gx and Gy without A
    gx = [[-1, -1, 0, 1, 1],
          [-1, -1, 0, 1, 1],
          [-1, -1, 0, 1, 1]]
    gy = [[1, 1, 1],
          [1, 1, 1],
          [0, 0, 0],
          [-1,-1,-1],
          [-1,-1,-1]]
    

    for i in range(0, len(segment)):
        # Matrix convolution
        gx_a = convolve(segment[i],gx)
        gy_a = convolve(segment[i],gy)

        m = x[i]
        n = y[i]

        theta = np.arctan(gy_a/gx_a)
        K = np.tan(theta)
        C = (n - K * m))

    print(C)