import cv2 as cv

#Gray scaling
img=cv.imread('/Users/Development/OpenCV/Photos/cat.jpeg')
cv.imshow('cat',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
cv.waitKey(0)

#Gaussian blur
blur=cv.GaussianBlur(img,(115,115),cv.BORDER_DEFAULT)#kernal size have to be pair of odd number
cv.imshow('Blur',blur)
cv.waitKey(0)

#Edge cascade
canny=cv.Canny(blur,125,175) #reduced edges by blurring
cv.imshow('Canny',canny)
cv.waitKey(0)

#Dilating the image
dilated=cv.dilate(canny,(7,7),iterations=1) 
cv.imshow('Dialated',dilated)
cv.waitKey(0)

#Eroding
eroded=cv.erode(dilated,(3,3),iterations=1)
cv.imshow('Eroded',eroded)
cv.waitKey(0)

#Resize
resized=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)
cv.waitKey(0)

#Cropping
cropped=img[50:200,200:400]
cv.imshow('Cropped',cropped)
cv.waitKey(0)