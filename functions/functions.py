# Import libraries
import cv2
import numpy as np
from tkinter import filedialog
import math
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


# center of mass for periodic systems
def x_coordinate(matrix):
    matrix_size = matrix.shape[0]
    mass_sum = matrix.sum()
    phi = np.zeros((matrix_size,matrix_size))
    xi = np.zeros((matrix_size,matrix_size))
    zeta = np.zeros((matrix_size,matrix_size))
    xi_sum = 0
    zeta_sum = 0

    for i in range(0,matrix_size):
        for j in range(0,matrix_size):
            phi[i][j] =  j/matrix_size*2*np.pi          
            xi = np.cos(phi[i][j])        
            zeta = np.sin(phi[i][j])  

            xi_sum += matrix[i][j]*xi
            zeta_sum += matrix[i][j]*zeta

    xi_avg = 1/mass_sum*xi_sum
    zeta_avg = 1/mass_sum*zeta_sum

    phi_avg = math.atan2(-1*zeta_avg, -1*xi_avg) + np.pi

    x_final = matrix_size*phi_avg/(2*np.pi)

    return x_final

def y_coordinate(matrix):
    matrix_size = matrix.shape[0]
    mass_sum = matrix.sum()
    phi = np.zeros((matrix_size,matrix_size))
    xi = np.zeros((matrix_size,matrix_size))
    zeta = np.zeros((matrix_size,matrix_size))
    xi_sum = 0
    zeta_sum = 0

    for i in range(0,matrix_size):
        for j in range(0,matrix_size):
            phi[i][j] =  i/matrix_size*2*np.pi          
            xi = np.cos(phi[i][j])        
            zeta = np.sin(phi[i][j])  

            xi_sum += matrix[i][j]*xi
            zeta_sum += matrix[i][j]*zeta

    xi_avg = 1/mass_sum*xi_sum
    zeta_avg = 1/mass_sum*zeta_sum

    phi_avg = math.atan2(-1*zeta_avg, -1*xi_avg) + np.pi

    y_final = matrix_size*phi_avg/(2*np.pi)

    return y_final

