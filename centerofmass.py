# Import libraries
import cv2
import timeit
import numpy as np
from PIL import Image
from scipy import ndimage
from datetime import datetime
import matplotlib.pyplot as plt
from functions.fcn_mrSE import *
from functions.functions import *
from functions.fcn_bg_intensity import *
from functions.fcn_removecoords import *
from functions.fcn_segmentation import *
np.seterr(divide='ignore', invalid='ignore')

start = timeit.default_timer()

choose_dataset = 1      # 1 for Tubulins 1, 2 for Tubulins II, 3 for Tubulins SOFI

if choose_dataset==1 or choose_dataset==2:
    total = 100
    img_height = 256
    stepsize = 16
else:
    total = 8000
    img_height = 500  
    stepsize = 20   

added_matrix = np.zeros((5*img_height,5*img_height), dtype=np.uint8)
for n in range(1,total+1):
    print(n,'/',total,'images')

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

    # Show segments with calculated coordinate
    #x_segment = np.add(np.multiply(x_lst,9),4)
    #y_segment = np.add(np.multiply(y_lst,9),4)
    #for i in range(0,len(segments)):
    #    segments[i] = resize_img(segments[i],900)
    #    segments[i][int(y_segment[i])][int(x_segment[i])] = 0
    #    cv2.imshow("segment", segments[i])
    #    cv2.waitKey()



    x_lst = np.nan_to_num(np.add(np.multiply(np.add(np.add(x_lst,-3),new_x),5),2))
    y_lst = np.nan_to_num(np.add(np.multiply(np.add(np.add(y_lst,-3),new_y),5),2))

    for i in range(0,len(x_lst)):
        if x_lst[i] > 5*img_height-1:
            x_lst[i] = 5*img_height-1
        if y_lst[i] > 5*img_height-1:
            y_lst[i] = 5*img_height-1
        if added_matrix[int(y_lst[i])][int(x_lst[i])]<255:
            added_matrix[int(y_lst[i])][int(x_lst[i])]+=51


stop = timeit.default_timer()

print('Time: ', int((stop - start)/60), 'minutes')
print('Time: ', stop - start, 'seconds')

# Save image
img_saved = Image.fromarray(added_matrix)
now = datetime.now()
current_time = now.strftime("%H%M%S")

if choose_dataset==1:
    img_saved.save("images/Tubulins_I_"+current_time+".tiff")
elif choose_dataset==2:
    img_saved.save("images/Tubulins_II_"+current_time+".tiff")
else:
    img_saved.save("images/Tubulins_SOFI_"+current_time+".tiff")


#rgb_img = np.array((added_matrix, added_matrix, added_matrix)).T
#print(rgb_img[0][0][0])

#for i in range(0,5*img_height):
#    for j in range(0,5*img_height):
#        if rgb_img[i][j][0] == 51:
#            rgb_img[j][i] = [51,102,0]
#        elif rgb_img[i][j][0] == 102:
#            rgb_img[j][i] = [76,153,0]
#        elif rgb_img[i][j][0] == 153:
#            rgb_img[j][i] = [102,204,0]
#        elif rgb_img[i][j][0] == 204:
#            rgb_img[j][i] = [0,204,0]
 #       elif rgb_img[i][j][0] == 255:
   #         rgb_img[j][i] = [0,255,0]
#data[0:256, 0:256] = [255, 0, 0] # red patch in upper left
#img = Image.fromarray(rgb_img, 'RGB')
#img.save('my.tiff')
#img.show()