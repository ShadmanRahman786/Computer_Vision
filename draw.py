import cv2 as cv
import numpy as np


blank=np.zeros((500,500,3),dtype='uint8') #image dtype
cv.imshow('Blank',blank)
img=cv.imread('/Users/Development/OpenCV/Photos/cat.jpeg')
cv.imshow('Cat',img)
#Paint the image certain color
blank[:]=0,255,0 #[:] selects all portion in the array and paints it with red
cv.imshow('Green',blank)
cv.waitKey(0)
 
#We can paint certain portions of the blank image
blank[200:300,300:400]=0,255,0
cv.imshow('Certain portion',blank)
cv.waitKey(0)

#Drawing rectangle
cv.rectangle(blank,(0,0),(255,500),(0,255,0),thickness=-1)
cv.imshow('Rectangle',blank)
cv.waitKey(0)

cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0),thickness=-1)
cv.imshow('Rectangle',blank)
cv.waitKey(0)

#Drawing circle
cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
cv.imshow('Circle',blank)
cv.waitKey(0)

#Draw a line
cv.line(blank,(100,250),(300,400),(255,255,255),thickness=3)
cv.imshow('Line',blank)
cv.waitKey(0)
# Writing text 
cv.putText(blank,'Hello my name is Shadman',(0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(255,255,255),3)
cv.imshow('Text',blank)
cv.waitKey(0)