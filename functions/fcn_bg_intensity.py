# Import libraries
import numpy as np
import cv2
from tkinter import filedialog
from scipy.ndimage import convolve
from functions.functions import *

# Returns matrix with spots, background is removed.
def fcn_bg_intensity(matrix, img_height, stepsize):

    x_coordinates = []
    y_coordinates = []
    xpos = stepsize
    ypos = stepsize
    sum = 0

    for y_shift in range(0,int(img_height/stepsize)):
        for x_shift in range(0,int(img_height/stepsize)):

            # Determine background intensity in small area
            for x in range(xpos-stepsize,xpos):
                for y in range(ypos-stepsize,ypos):
                    sum += matrix[y][x]

            bg_intensity = sum/(stepsize*stepsize)
            std_matrix = std(matrix) 

            # Find spots
            for x in range(xpos-stepsize,xpos):
                for y in range(ypos-stepsize,ypos):
                    if matrix[y][x] >= bg_intensity + 3*std_matrix:
                        x_coordinates.append(x)
                        y_coordinates.append(y)
    
            xpos += stepsize
            sum = 0

        ypos += stepsize
        xpos = stepsize
   
    return x_coordinates, y_coordinates