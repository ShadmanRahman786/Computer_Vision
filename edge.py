import cv2 as cv
import numpy as np
img=cv.imread('/Users/Development/OpenCV/Photos/pexels-ferdie-drone-297619-13874296.jpg')
cv.imshow('image',img)
# Here we will learn about two different type of thresholding 1.Simple 2.Adaptive

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#Edge detection
#Laplacian 
lap=cv.Laplacian(gray,cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)
cv.waitKey(0)

#Sobel
sobelx=cv.Sobel(gray,cv.CV_64F,1,0)
sobely=cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel=cv.bitwise_or(sobelx,sobely)
cv.imshow('Sobel X',sobelx)
cv.imshow('Sobel Y',sobely)
cv.imshow('Combined Sobel',combined_sobel)
cv.waitKey(0)

#we have learned about canny edge detection previously