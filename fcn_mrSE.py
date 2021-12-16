#Maximum radial symmetry estimation
import numpy as np
import cv2
from functions import *
from scipy.ndimage import convolve
import sympy as sym

def fcn_theta(gx, gy, m, n):

    theta = np.arctan(gy[m,n]/gx[m,n])

    return theta
        
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
    
    # Variables
    x, y = sym.symbols('x y', real=True)
    sol_lst = []
    

    for i in range(0, len(segment)):
        # Matrix convolution
        gx_a = convolve(segment[i],gx)
        gy_a = convolve(segment[i],gy)
        D_sum = 0

        
        # D_sum
        for n in range(0, 9):
            for m in range(0, 9):
                K = np.tan(fcn_theta(gx_a,gy_a,m,n))
                C = (n - K*m)
                D = (np.abs(K*x - y + C)/np.sqrt(1 + K**2))**2
                D_sum += D
        
        
        # Solve Derivative = 0
        dD_sumdx = sym.diff(D_sum, x)
        dD_sumdy = sym.diff(D_sum, y)

        eq1 = sym.Eq(dD_sumdx, 0)
        eq2 = sym.Eq(dD_sumdy, 0)

        sol = sym.solve((eq1, eq2), (x, y))
        sol_lst.append(sol)

        print(segment[i])
        print(sol_lst)
        sol_lst = []
    