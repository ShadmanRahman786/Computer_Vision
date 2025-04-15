import cv2 as cv
import numpy as np

img=cv.imread('/Users/Development/OpenCV/Photos/pexels-dana-tentis-118658-691114.jpg')

blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank Image',blank)
mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),1500,255,-1)
cv.imshow('Mask',mask)
cv.waitKey(0)

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked image',masked)
cv.waitKey(0)

masked2=cv.bitwise_or(img,img,mask=mask)
cv.imshow('Masked again image',masked2)
cv.waitKey(0)