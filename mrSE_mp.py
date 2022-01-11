import multiprocessing as mp
from datetime import datetime
import numpy as np
import ctypes as c
import cv2
import timeit
from PIL import Image
from functions.fcn_mrSE import *
from functions import *
from functions.fcn_segmentation import *
from functions.fcn_bg_intensity import *
from functions.fcn_removecoords import *
np.seterr(divide='ignore', invalid='ignore')

def mrSE(n):
    
    print(n,'/','total images')

    # Training data
    #img_matrix = cv2.imread('Tubulins_I/'+str(n).zfill(5)+'.tif', cv2.IMREAD_UNCHANGED)
    #added_matrix = np.zeros((1280,1280),dtype='uint8')
    #img_height = 256
    #stepsize = 16

    # Test data
    img_matrix = cv2.imread('Tubulins_SOFI/'+str(n)+'.tif', cv2.IMREAD_UNCHANGED)
    added_matrix = np.zeros((2500,2500),dtype='uint8')
    img_height = 500
    stepsize = 20

    # Returns coordinates of spots (second argument is stepsize)
    x_coordinates, y_coordinates = fcn_bg_intensity(img_matrix,img_height,stepsize)

    # Delete double points
    new_x, new_y = removecoords(x_coordinates,y_coordinates,img_matrix)

    # Cut segments
    segments = segmentation(img_matrix, new_x, new_y)

    x_lst,y_lst = gradient_operator(segments, new_x, new_y)
    x_img_lst = np.add(np.multiply(new_x,5),2+np.multiply(x_lst,5)).astype(int)
    y_img_lst = np.add(np.multiply(new_y,5),2+np.multiply(y_lst,-5)).astype(int)

    for i in range(0,len(x_lst)):
        added_matrix[y_img_lst[i]][x_img_lst[i]]=1

    return added_matrix
    #return np.vstack((x_lst, y_lst))
    


if __name__ == '__main__':
    pool = mp.Pool(processes=8)
    start = timeit.default_timer()

    results = pool.map(mrSE, range(1,100))
    pool.close()
    pool.join()

    stop = timeit.default_timer()

    print('Time: ', int((stop - start)/60), 'minutes')
    print('Time: ', stop - start, 'seconds')

    img_saved = Image.fromarray(sum(results))
    now = datetime.now()
    current_time = now.strftime("%H%M%S")
    img_saved.save("images/mrSE_mp_img_"+current_time+".tif")