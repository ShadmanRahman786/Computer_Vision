import cv2 as cv
import numpy as np
img=cv.imread('Photos/pexels-ferdie-drone-297619-13874296.jpg')

#translate

def translate(img,x,y):#Basically shifting an image along x/y axis
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# -x-->left
# -y-->up
# x-->Right
# y-->Down

translated=translate(img,100,100)
cv.imshow('Translated image',translated)
cv.waitKey(0)

#Rotation
def rotate(img,angle,rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2) #center
    
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions=(width,height)
    return cv.warpAffine(img,rotMat,dimensions)
rotated=rotate(img,45) 
# +ve for clock wise
# -ve for anti clock wise
cv.imshow('Rotated',rotated)
cv.waitKey(0)

#Resize

resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA) #for shrinking
cv.imshow('Resized image',resized)
cv.waitKey(0)

#Flipping
flip=cv.flip(img,-1)
cv.imshow('Flipped image',flip)
cv.waitKey(0)
# 0-->flipping the image vertically x-axis
# 1-->flipping the image horizontally y-axis
# -1-->flipping he image both horizontally and vertically

#Cropping
cropped=img[200:400,300:400]
cv.imshow('Cropped image',cropped)
cv.waitKey(0)