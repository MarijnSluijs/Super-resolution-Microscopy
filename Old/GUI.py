from PIL import  ImageTk
import PIL.Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
from tkinter import *
from functions import *

def savefile():
    filename = filedialog.asksaveasfile(mode='wb', defaultextension=".tif")
    if not filename:
        return
    img.save(filename)

img_src = 'Tubulins_I/00002.tif'
img_matrix = cv2.imread(img_src, cv2.IMREAD_UNCHANGED)

img_matrix2 = resize_img(img_matrix, 100)
resized_matrix = resize_img(img_matrix, 200)

# Start GUI
root = Tk()  
root.title('Super-resolution image')
root.geometry("1000x700+100+100")
root.configure(bg='white')

# Place image in GUI
img_resized = PIL.Image.fromarray(resized_matrix)
img_tk = ImageTk.PhotoImage(image=img_resized) 
Label(root, image=img_tk).place(x=0,y=0) 

# Save image button
img = PIL.Image.fromarray(img_matrix2)
pixel = PhotoImage(width=1, height=1)
button = Button(root, bg='lightblue', text="save as TIF", font='Helvetica', image=pixel, command=savefile, height=30, width=100, compound="c")
button.place(x=206,y=520)

root.mainloop()