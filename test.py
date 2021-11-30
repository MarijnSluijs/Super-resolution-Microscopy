from PIL import Image
from numpy import asarray
import numpy as np
np.set_printoptions(threshold=np.inf)

# Show image
im1 = Image.open('Tubulins_II/01796.tif')
im1.show()

# Output image as matrix
matrix1 = asarray(im1)
mat1 = np.matrix(matrix1, dtype=np.int64)

with open('outfile.txt','wb') as f:
    for line in mat1:
        np.savetxt(f, line, fmt='%.0f')


from skimage import io
im = io.imread('Tubulins_I/00500.tif')
print(im)