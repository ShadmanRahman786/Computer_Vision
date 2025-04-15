# For smoothing and denoising we use blurring
# kernal is a window which has rows and columns and it moves through out photo for blurring
import cv2 as cv
img=cv.imread('Photos/pexels-ferdie-drone-297619-13874296.jpg')
resized_img=cv.resize(img,(600,400),interpolation=cv.INTER_AREA)
# Average blurring
average=cv.blur(resized_img,(11,11))
cv.imshow('Average blur',average)
cv.waitKey(0)

# Gaussian blur (less than average blur)
gauss=cv.GaussianBlur(resized_img,(11,11),0) 
#sigmaX value(0.5/1)=sharp gaussian curve. Tight less blur
#sigmaX value(5/10)=wide gaussian curve. Heavy smooth blur
cv.imshow('Gaussian blur',gauss)
cv.waitKey(0)

# Median blur
median=cv.medianBlur(resized_img,11) # It will automatically assume kernal is 3*3
cv.imshow('Median blur',median)
cv.waitKey(0)

#Bilateral blur
# used in advance CV it will blur retaining edges
bilateral=cv.bilateralFilter(resized_img,15,35,25)
cv.imshow('Bilateral',bilateral)
cv.waitKey(0)
