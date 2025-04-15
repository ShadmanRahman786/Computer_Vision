import cv2 as cv
import numpy as np
img=cv.imread('/Users/Development/OpenCV/Photos/pexels-ferdie-drone-297619-13874296.jpg')
cv.imshow('image',img)
# Here we will learn about two different type of thresholding 1.Simple 2.Adaptive

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Simple thresholding
threshold,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY)# we set 255 for binarizing image
cv.imshow('Simple Thresholded',thresh)
cv.waitKey(0) #black part of image change to white

threshold,thresh_inv=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)# we set 255 for binarizing image
cv.imshow('Simple Thresholded Inverse',thresh_inv)
cv.waitKey(0) #white part of image change to black


#Adaptive thresholding
adaptive_thresh= cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('Adaptive thresholding',adaptive_thresh)
cv.waitKey(0)

