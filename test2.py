import numpy as np
from scipy import ndimage
import math
import cv2
from functions.functions import *
matrix1 = np.array(([52,35,37,42,32,38,36],
                    [43,31,44,37,38,38,33],
                    [42,44,50,57,42,34,40],
                    [47,53,122,127,61,37,33],
                    [41,47,119,122,53,34,37],
                    [44,39,56,46,34,38,36],
                    [43,36,40,33,33,36,32],), dtype=np.uint8)

matrix2 = np.array(([42,44,50,57,42],
                    [47,53,122,127,61],
                    [41,47,119,122,53],
                    [44,39,56,46,34],
                    [0,0,0,0,0]))

matrix2 = np.array(([0,0,0,0,0],
                    [0,0,0,0,0],
                    [0,0,4,4,0],
                    [0,0,4,4,0],
                    [0,0,0,0,0]))

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

            xi_sum += matrix1[i][j]*xi
            zeta_sum += matrix1[i][j]*zeta

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

            xi_sum += matrix1[i][j]*xi
            zeta_sum += matrix1[i][j]*zeta

    xi_avg = 1/mass_sum*xi_sum
    zeta_avg = 1/mass_sum*zeta_sum

    phi_avg = math.atan2(-1*zeta_avg, -1*xi_avg) + np.pi

    y_final = matrix_size*phi_avg/(2*np.pi)

    return y_final

x_coordinate(matrix1)
y_coordinate(matrix1)
print(ndimage.measurements.center_of_mass(matrix1))

cv2.imshow("segment", resize_img(matrix1,1000))
cv2.waitKey()