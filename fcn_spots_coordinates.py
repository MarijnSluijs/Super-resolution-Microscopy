# fcn_spots_coordinates.py

# This functions finds high intensity pixels in the image. The molecules are positioned at these high intensity pixels.
# A pixel is determined to have a molecule in case the intensity is 3 standard deviations higher than the average
# intensity a small area around it.

# Import libraries
import numpy as np

# Returns matrix with spots, background is removed.
def spots_coordinates(matrix, img_height, stepsize):

    x_coordinates = []
    y_coordinates = []
    xpos = stepsize
    ypos = stepsize
    sum = 0

    for y_shift in range(0,int(img_height/stepsize)):
        for x_shift in range(0,int(img_height/stepsize)):

            # Determine background intensity in small area
            for x in range(xpos-stepsize,xpos):
                for y in range(ypos-stepsize,ypos):
                    sum += matrix[y][x]

            bg_intensity = sum/(stepsize*stepsize)
            std_matrix = np.std(np.matrix.flatten(matrix))

            # Find spots
            for x in range(xpos-stepsize,xpos):
                for y in range(ypos-stepsize,ypos):
                    if matrix[y][x] >= bg_intensity + 3*std_matrix:
                        x_coordinates.append(x)
                        y_coordinates.append(y)
    
            xpos += stepsize
            sum = 0

        ypos += stepsize
        xpos = stepsize
   
    return x_coordinates, y_coordinates