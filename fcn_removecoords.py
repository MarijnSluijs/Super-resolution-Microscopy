# Import libraries
import numpy as np
import cv2
from tkinter import filedialog
from scipy.ndimage import convolve

def removecoords(x_list, y_list, matrix):

    popped = 0
    for i in range(1,len(x_list)):
        i = i - popped
        distance = np.sqrt((x_list[i]-x_list[i-1])**2 + (y_list[i]-y_list[i-1])**2)

        if distance < 8:
            if matrix[y_list[i]][x_list[i]] < matrix[y_list[i-1]][x_list[i-1]]:
                x_list.pop(i)
                y_list.pop(i)

            else:
                x_list.pop(i-1)
                y_list.pop(i-1)
            
            popped += 1

    return x_list, y_list
