# COM_mp.py

# This program implements the Center of Mass in an Unbounded 2D Environment algorithm to create a super-resolution image from a given dataset. 
# The code has been sped up using the Python multiprocessing module

# Import libraries
import cv2
import timeit
import numpy as np
from PIL import Image
import multiprocessing
from datetime import datetime
from functools import partial

# Import functions
from fcn_resize_img import *
from fcn_segmentation import *
from fcn_COM import *
from fcn_spots_coordinates import *
from fcn_removecoordinates import *
np.seterr(divide='ignore', invalid='ignore')

def COM(n,total,img_height,stepsize,choose_dataset):

    print(n,'/', total ,'images analyzed')

    # Convert image to matrix
    if choose_dataset==1:
        img_matrix = cv2.imread('Tubulins_I/'+str(n).zfill(5)+'.tif', cv2.IMREAD_UNCHANGED)
    elif choose_dataset==2:
        img_matrix = cv2.imread('Tubulins_II/'+str(n).zfill(5)+'.tif', cv2.IMREAD_UNCHANGED)
    else:
        img_matrix = cv2.imread('Tubulins_SOFI/'+str(n)+'.tif', cv2.IMREAD_UNCHANGED)

    # Returns coordinates of spots
    x_spots, y_spots = spots_coordinates(img_matrix,img_height,stepsize)

    # Delete double coordinates (when a spot consists of multiple high intensity pixels)
    x_spots_unique, y_spots_unique = removecoordinates(x_spots,y_spots,img_matrix)

    # Cut segments from image around spot
    segments = segmentation(img_matrix, x_spots_unique, y_spots_unique)
    
    # Determine the coordinates of the exact location of the molecule in the segment
    x_segment_lst = []
    y_segment_lst = []
    for i in range(0, len(segments)):
        x = x_COM(segments[i])
        y = y_COM(segments[i])
        x_segment_lst.append(x)
        y_segment_lst.append(y)

        create_segment_images = False # Set True only when segment images are required (it produces a lot of images)
        if create_segment_images == True:
            # Create image from segment including calculated molecule coordinate
            scale_factor = 39
            segment_resized = resize_img(segments[i], scale_factor*100)
            x_segment = scale_factor*x+19
            y_segment = scale_factor*y+19
            segment_resized[int(y_segment)][int(x_segment)] = 0
            segment_resized[int(y_segment)+1][int(x_segment)] = 0
            segment_resized[int(y_segment)-1][int(x_segment)] = 0
            segment_resized[int(y_segment)][int(x_segment)+1] = 0
            segment_resized[int(y_segment)][int(x_segment)-1] = 0
            segment_resized[int(y_segment)+2][int(x_segment)] = 0
            segment_resized[int(y_segment)-2][int(x_segment)] = 0
            segment_resized[int(y_segment)][int(x_segment)+2] = 0
            segment_resized[int(y_segment)][int(x_segment)-2] = 0

            rgb_img = np.array((segment_resized.T, segment_resized.T, segment_resized.T)).T

            for a in range(0,scale_factor*segments[i].shape[0]):
                for b in range(0,scale_factor*segments[i].shape[0]):
                    if rgb_img[a][b][0] == 0:
                        rgb_img[a][b] = [255,0,0]
                    
            # Save segment to an image
            img_saved = Image.fromarray(rgb_img, 'RGB')
            img_saved.save("images/segment_"+str(n)+"_"+str(i)+".tiff")


    # Add calculated coordinates of the molecule in the segment to the coordinates of the spots to 
    # obtain the coordinates of the molecule in the complete image
    x_lst = np.nan_to_num(np.add(np.multiply(np.add(np.add(x_segment_lst,-3),x_spots_unique),5),2))
    y_lst = np.nan_to_num(np.add(np.multiply(np.add(np.add(y_segment_lst,-3),y_spots_unique),5),2))

    return x_lst, y_lst


if __name__ == '__main__':
    # Start multiprocessing (define the amount of logical processors used)
    pool = multiprocessing.Pool(processes=8)

    # Record total runtime
    start = timeit.default_timer()

    # Choose which dataset to use, 1 for Tubulins 1, 2 for Tubulins II, 3 for Tubulins SOFI
    choose_dataset = 1
    if choose_dataset==1 or choose_dataset==2:
        img_height = 256
        stepsize = 16
        total = 2401
    else:
        img_height = 500  
        stepsize = 20   
        total = 8000

    coordinates = pool.map(partial(COM,total=total,img_height=img_height,stepsize=stepsize,choose_dataset=choose_dataset), range(1,total+1))
    pool.close()
    pool.join()

    # Retrieve x and y coordinates
    x_lst = []
    y_lst = []
    for i in range(0,len(coordinates)):
        for j in range(0,len(coordinates[i][0])):
            x_lst.append(coordinates[i][0][j])
        for j in range(0,len(coordinates[i][1])):
            y_lst.append(coordinates[i][1][j])
        
    # Create a matrix for super-resolution image
    superres_matrix = np.zeros((5*img_height,5*img_height), dtype=np.uint8)
    
    # If a coordinate is just outside the image, it will be shifted to the edge of the image.
    # Last if-statement places the molecules in the matrix
    for i in range(0,len(x_lst)):
        if x_lst[i] > 5*img_height-1:
            x_lst[i] = 5*img_height-1
        if y_lst[i] > 5*img_height-1:
            y_lst[i] = 5*img_height-1
        if superres_matrix[int(y_lst[i])][int(x_lst[i])]<252:
            superres_matrix[int(y_lst[i])][int(x_lst[i])]+=28

    # Create colored image from super-resolution matrix
    rgb_img = np.array((superres_matrix.T, superres_matrix.T, superres_matrix.T)).T

    for i in range(0,5*img_height):
        for j in range(0,5*img_height):
            if rgb_img[i][j][0] == 28:
                rgb_img[i][j] = [51,0,102]
            elif rgb_img[i][j][0] == 56:
                rgb_img[i][j] = [76,0,153]
            elif rgb_img[i][j][0] == 84:
                rgb_img[i][j] = [102,0,204]
            elif rgb_img[i][j][0] == 112:
                rgb_img[i][j] = [127,0,255]
            elif rgb_img[i][j][0] == 140:
                rgb_img[i][j] = [153,51,255]
            elif rgb_img[i][j][0] == 168:
                rgb_img[i][j] = [153,0,153]
            elif rgb_img[i][j][0] == 196:
                rgb_img[i][j] = [204,0,204]
            elif rgb_img[i][j][0] == 224:
                rgb_img[i][j] = [255,0,255]
            elif rgb_img[i][j][0] == 252:
                rgb_img[i][j] = [255,51,255]

    # Print runtime
    stop = timeit.default_timer()
    print('Time: ', int((stop - start)/60),'minute(s) and', round(((stop - start)/60 - int((stop - start)/60))*60), 'second(s)')

    # Save super-resolution matrix to an image
    img_saved = Image.fromarray(rgb_img, 'RGB')
    now = datetime.now()
    current_time = now.strftime("%H%M%S")
    img_saved.save("images/COM_mp_"+current_time+".tiff")