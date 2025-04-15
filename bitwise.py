# There are 4 basic bitwise operator
# AND, OR, XOR and NOR

import cv2 as cv
import numpy as np
blank=np.zeros((400,400),dtype='uint8')
rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)
cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)
cv.waitKey(0)

#bitwise And(Intersecting region)
bitwise_and=cv.bitwise_and(rectangle,circle)
cv.imshow('And operation',bitwise_and)
cv.waitKey(0)

#bitwise Or(Non-intersecting and intersecting region)
bitwise_or=cv.bitwise_or(rectangle,circle)
cv.imshow('Or operation',bitwise_or)
cv.waitKey(0)

#bitwise xor(Non-intersecting region)
bitwise_xor=cv.bitwise_xor(rectangle,circle)
cv.imshow('Xor operation',bitwise_xor)
cv.waitKey(0)

#bitwise not(mainly inverts binary color)
bitwise_not=cv.bitwise_not(rectangle)
cv.imshow('Not operation',bitwise_not)
cv.waitKey(0)