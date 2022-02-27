# fcn_segmentation.py

# This function cuts a segment of the image around the calculated molecule position.
# This segment is used in either the Center of Mass in an Unbounded 2D Environment algorithm or maximal radial symmetry estimation algorithm to find the exact position of the molecule.

# Import libraries
import numpy as np

# Segmentation of spots
def segmentation(matrix, x, y):
    num_spots = len(x)
    segments = []

    for i in range(0,num_spots):
        segment = np.zeros((7,7))
        matrix_segment = matrix[y[i]-3:y[i]+4, x[i]-3:x[i]+4]

        segment[0:matrix_segment.shape[0],0:matrix_segment.shape[1]] = matrix_segment
        segments.append(segment)

    return segments