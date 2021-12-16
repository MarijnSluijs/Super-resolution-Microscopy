# Import libraries
import numpy as np
import cv2
from tkinter import filedialog
from scipy.ndimage import convolve
from functions import *

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
                    if matrix[y][x] >= 2*bg_intensity:
                        x_coordinates.append(x)
                        y_coordinates.append(y)
                    else:
                        matrix[y][x] = 0
        
            xpos += stepsize
            sum = 0

        ypos += stepsize
        xpos = stepsize

   
    return matrix, x_coordinates, y_coordinates