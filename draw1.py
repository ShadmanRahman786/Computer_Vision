import cv2 as cv
import numpy as np

# blank=np.zeros((500,500,3),dtype='uint8')
# cv.imshow('Blank',blank)
# #painting whole canvas
# blank[:]=255,255,255
# cv.imshow('Blank',blank)
# cv.waitKey(0)

# #painting certain portion
# blank[200:300,300:400]=255,255,0
# cv.imshow('Certain portion',blank)
# cv.waitKey(0)

# #drawing rectangle
# cv.rectangle(blank,(0,0),(255,500),(0,255,0),thickness=-1)
# cv.imshow('Rectangle',blank)
# cv.waitKey(0)

# #writing text
# cv.putText(blank,"Hello ima u r dad",(0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,0,0),2)
# cv.imshow('Text',blank)
# cv.waitKey(0)

# img=cv.imread('Photos/pexels-ferdie-drone-297619-13874296.jpg')
# cv.imshow('Image',img)
# cv.waitKey(0)

# #image gray scale
# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray scaled image',gray)
# cv.waitKey(0)

# #Gaussian blur
# blur=cv.GaussianBlur(img,(9,9),cv.BORDER_DEFAULT)
# cv.imshow('Blurred by gaussian',blur)
# cv.waitKey(0)

# #Edge Cascading
# canny=cv.Canny(blur,125,175)
# cv.imshow('Edge cascaded by canny',canny)
# cv.waitKey(0)

# #dilting the image
# dilated=cv.dilate(canny,(7,7),iterations=1)
# cv.imshow('Dialted canny image',dilated)
# cv.waitKey(0)


# #Eroding image
# erode=cv.erode(dilated,(7,7),iterations=1)
# cv.imshow('Eroded image',erode)
# cv.waitKey(0)

# #Resize
# resize=cv.resize(img,(600,450),interpolation=cv.INTER_AREA)
# cv.imshow('Resized image',resize)
# cv.waitKey(0)

# #Crop
# crop=img[200:300,300:400]
# cv.imshow('Cropped image',crop)
# cv.waitKey(0)

# def rescaleFrame(frame,scale=0.2):
#     width=int(frame.shape[1]*scale)
#     height=int(frame.shape[0]*scale)
#     dimension=(width,height)
#     return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

# img=cv.imread('/Users/Development/OpenCV/Photos/pexels-ferdie-drone-297619-13874296.jpg')
# cv.imshow('Image',img)
# cv.waitKey(0)
# resized_image=rescaleFrame(img)
# cv.imshow('Resized image',resized_image)
# cv.waitKey(0)
# capture=cv.VideoCapture(0)

# while True:
#     isTrue,frame=capture.read()
#     resized_frame=rescaleFrame(frame)
#     cv.imshow('Video Live',frame)
#     cv.imshow('Resized video',resized_frame)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()


# #gray scaling image

# gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray scaled image',gray)
# cv.waitKey(0)

# #Resizing image
# r_img=cv.resize(img,(600,400),interpolation=cv.INTER_AREA)
# cv.imshow('Resized image',r_img)
# cv.waitKey(0)

# #blurring
# #1. Gaussian blur

# gauss=cv.GaussianBlur(r_img,(11,11),0)
# cv.imshow("Gaussian blurred image",gauss)
# cv.waitKey(0)

# #2. Average blur
# average_blur=cv.blur(r_img,(11,11))
# cv.imshow('Average blur',average_blur)
# cv.waitKey(0)

# #3. Median blur
# median_blur=cv.medianBlur(r_img,11)
# cv.imshow('Median blur',median_blur)
# cv.waitKey(0)

# #Bilateral Blur
# bilateral_blur=cv.bilateralFilter(r_img,30,50,50)
# cv.imshow('Bilateralm blurred',bilateral_blur)
# cv.waitKey(0)

# #Edge cascading
# canny=cv.Canny(gauss,125,210)
# cv.imshow('Canny',canny)
# cv.waitKey(0)


# #dilating image
# dilate=cv.dilate(canny,(11,11),iterations=1)
# cv.imshow('Dilated image',dilate)
# cv.waitKey(0)

# #Eroded image

# erode=cv.erode(dilate,(11,11),iterations=1)
# cv.imshow('Eroded image',erode)
# cv.waitKey(0)

# capture=cv.VideoCapture(0)

# def rescaleFrame(frame,scale=0.5):
#     width=int(frame.shape[1]*scale)
#     height=int(frame.shape[0]*scale)
#     dimension=(width,height)
#     return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

# while True:
#     isTrue,frame=capture.read()
#     resized_frame=rescaleFrame(frame)
#     cv.imshow('video',frame)
#     cv.imshow('Resized Video',resized_frame)
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()

# blank=np.zeros((500,500,3),dtype='uint8')
# cv.imshow('Blank image',blank)
# cv.waitKey(0)

# blank[:]=255
# cv.imshow('White canvas',blank)
# cv.waitKey(0)

# blank[200:300,300:400]=255,0,255
# cv.imshow('Color portion',blank)
# cv.waitKey(0)

# #drawing rectangle
# rectangle=cv.rectangle(blank,(0,0),(255,255),(0,255,255),-1)
# cv.imshow('Rectangle',rectangle)
# cv.waitKey(0)


# #drawing circle
# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
# cv.imshow('Circle',blank)
# cv.waitKey(0)

# #text
# cv.putText(blank,"I am Shadman",(0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,0,0),3)
# cv.imshow('Text',blank)
# cv.waitKey(0)

img=cv.imread('/Users/Development/OpenCV/Photos/pexels-dana-tentis-118658-691114.jpg')

blank=np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('Blank Image',blank)
cv.waitKey(0)
mask=cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),1500,255,-1)
cv.imshow('Mask',mask)
cv.waitKey(0)

masked=cv.bitwise_and(img,img,mask=mask)
cv.imshow('Masked image',masked)
cv.waitKey(0)