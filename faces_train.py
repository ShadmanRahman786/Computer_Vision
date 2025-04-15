import os
import numpy as np
import cv2 as cv

people=['Ana_de_armas','Megan_fox']
p=[]
for i in os.listdir(r'/Users/Development/OpenCV/Faces'):
    p.append(i)

print(p)