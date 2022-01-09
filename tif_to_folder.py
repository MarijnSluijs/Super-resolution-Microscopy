from PIL import Image
import numpy as np

def read_tiff(path):

    img = Image.open(path)
    images = []
    for i in range(img.n_frames):
        img.seek(i)
        images.append(np.array(img))
    return np.array(images)

path = "Tubulin_SOFI_2D_flip.tif"
tif_to_matrix = read_tiff(path)

for i in range(0,8000):
    img = Image.fromarray(tif_to_matrix[i])
    img.save('Tubulins_SOFI/'+str(i)+'.tif')
