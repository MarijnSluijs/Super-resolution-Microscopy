#Maximum radial symmetry estimation
import numpy as np
import cv2
from functions import *
from scipy.ndimage import convolve
import sympy as sym
from scipy import signal
import timeit

def gradient_operator(segment, x, y):
    # Define Gx and Gy without A
    gx = np.array([[-1, -1, 0, 1, 1],
          [-1, -1, 0, 1, 1],
          [-1, -1, 0, 1, 1]],dtype='uint8')
    gy = np.array([[1, 1, 1],
          [1, 1, 1],
          [0, 0, 0],
          [-1,-1,-1],
          [-1,-1,-1]],dtype='uint8')

    # Variables
    x, y = sym.symbols('x y', real=True)
    sol_lst_x = []
    sol_lst_y = []

    for i in range(0, len(segment)):
        # Matrix convolution
        
        #gx_a = convolve(segment[i],gx)
        #gy_a = convolve(segment[i],gy)
        
        #gx_a = signal.convolve2d(segment[i], gx, boundary='wrap', mode='full')
        #gy_a = signal.convolve2d(segment[i], gy, boundary='wrap', mode='full')

        gx_a = np.gradient(segment[i], axis=1)
        gy_a = np.gradient(segment[i], axis=0)
        D_sum = 0
        # D_sum
        
        for m in range(-3, 4):
            for n in range(-3, 4):
                
                K = gy_a[n+3][m+3]/gx_a[n+3][m+3]
                C = (n - K*m)
                
                D = (np.abs(K*x - y + C)/np.sqrt(1 + K**2))**2
                D_sum += D
                
        dD_sumdx = sym.diff(D_sum, x)
        dD_sumdy = sym.diff(D_sum, y)
        # Solve Derivative = 0

        eq1 = sym.Eq(dD_sumdx,0)
        eq2 = sym.Eq(dD_sumdy,0)

        sol = sym.solve((eq1, eq2), (x, y))

        if sol == []:
            sol_lst_x.append(0)
            sol_lst_y.append(0)
        else:
            sol_lst_x.append(sol[x])
            sol_lst_y.append(sol[y])
        #sol_lst.append(sol)
        #print(eq1, eq2, sol)
        #print(gx_a, gy_a)
        

    return sol_lst_x, sol_lst_y
    

