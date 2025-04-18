# allows to know distribution of pixel intensity

import cv2 as cv
import matplotlib.pyplot as plt 
img=cv.imread('/Users/Development/OpenCV/Photos/pexels-dana-tentis-118658-691114.jpg')
cv.imshow('Image',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
cv.waitKey(0)

gray_hist=cv.calcHist([img],[0],None,[256],[0,256])#images are list over here
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()
cv.waitKey(0)