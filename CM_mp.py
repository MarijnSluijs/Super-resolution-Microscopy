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


def CM(n):
    print(n,'/ total images')

    choose_dataset = 3      # 1 for Tubulins 1, 2 for Tubulins II, 3 for Tubulins SOFI

    if choose_dataset==1 or choose_dataset==2:
        img_height = 256
        stepsize = 16
    else:
        img_height = 500  
        stepsize = 20   

    added_matrix = np.zeros((5*img_height,5*img_height), dtype=np.uint8)

    # Create grayscale matrix
    if choose_dataset==1:
        img_matrix = cv2.imread('Tubulins_I/'+str(n).zfill(5)+'.tif', cv2.IMREAD_UNCHANGED)
    elif choose_dataset==2:
        img_matrix = cv2.imread('Tubulins_II/'+str(n).zfill(5)+'.tif', cv2.IMREAD_UNCHANGED)
    else:
        img_matrix = cv2.imread('Tubulins_SOFI/'+str(n)+'.tif', cv2.IMREAD_UNCHANGED)

    # Returns coordinates of spots
    x_coordinates, y_coordinates = fcn_bg_intensity(img_matrix,img_height,stepsize)

    # Delete double points
    new_x, new_y = removecoords(x_coordinates,y_coordinates,img_matrix)

    # Cut segments
    segments = segmentation(img_matrix, new_x, new_y)

    x_lst = []
    y_lst = []
    
    for i in range(0, len(segments)):
        x = x_coordinate(segments[i])
        y = y_coordinate(segments[i])
        x_lst.append(x)
        y_lst.append(y)


    x_lst = np.nan_to_num(np.add(np.multiply(np.add(np.add(x_lst,-3),new_x),5),2))
    y_lst = np.nan_to_num(np.add(np.multiply(np.add(np.add(y_lst,-3),new_y),5),2))

    for i in range(0,len(x_lst)):
        if x_lst[i] > 5*img_height-1:
            x_lst[i] = 5*img_height-1
        if y_lst[i] > 5*img_height-1:
            y_lst[i] = 5*img_height-1
        if added_matrix[int(y_lst[i])][int(x_lst[i])]<255:
            added_matrix[int(y_lst[i])][int(x_lst[i])]+=51

    return added_matrix



if __name__ == '__main__':
    pool = mp.Pool(processes=10)
    start = timeit.default_timer()

    results = pool.map(CM, range(1,8000))
    pool.close()
    pool.join()

    stop = timeit.default_timer()

    print('Time: ', int((stop - start)/60), 'minutes')
    print('Time: ', stop - start, 'seconds')

    img_saved = Image.fromarray(sum(results))
    now = datetime.now()
    current_time = now.strftime("%H%M%S")
    img_saved.save("images/CM_mp_"+current_time+".tiff")