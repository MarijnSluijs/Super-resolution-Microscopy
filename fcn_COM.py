# fcn_COM.py

# These functions implement the Center of Mass in an Unbounded 2D Environment algorithm. The algorithm is used in both x and y direction to get the position of the molecule.

# Import libraries
import numpy as np
import math

# Center of mass in x-direction
def x_COM(matrix):
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

# Center of mass in y-direction
def y_COM(matrix):
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