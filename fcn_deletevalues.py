# Import libraries
import numpy as np
import cv2
from tkinter import filedialog
from scipy.ndimage import convolve

def deletevalues(x_list, y_list):
    tot_list = []
    pop_list = []
    for x in range(0,len(x_list)):
        tot = x_list[x]**2 + y_list[x]**2
        tot_list.append(tot)
    for i in range(1,len(tot_list)):
        if abs(tot_list[i]-tot_list[i-1]) <= 500:
            pop_list.append(i)
    for a in range(0, len(pop_list)):
        pop = pop_list[a]-a
        x_list.pop(pop)
        y_list.pop(pop)

    return x_list, y_list