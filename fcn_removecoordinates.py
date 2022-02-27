# fcn_removecoordinates.py

# This function deletes double coordinates. In case two high intensity pixels are close to each other, one is removed to prevent cutting two segments around the same molecule. This saves memory and runtime.

# Import libraries
import numpy as np

def removecoordinates(x_list, y_list, matrix):

    popped = 0
    for i in range(1,len(x_list)):
        i = i - popped
        distance = np.sqrt((x_list[i]-x_list[i-1])**2 + (y_list[i]-y_list[i-1])**2)

        # In case two high intensity pixels are less than 4 pixels apart (in any direction), one is removed. (sqrt[4^2+4^2]=5.7)
        if distance < 5.7:
            if matrix[y_list[i]][x_list[i]] < matrix[y_list[i-1]][x_list[i-1]]:
                x_list.pop(i)
                y_list.pop(i)
            else:
                x_list.pop(i-1)
                y_list.pop(i-1)
            popped += 1

    return x_list, y_list
