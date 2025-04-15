import cv2 as cv
img=cv.imread('/Users/Development/OpenCV/Ana de armas/gettyimages-850026184-612x612.jpg')
cv.imshow('Person',img)
cv.waitKey(0)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person',gray)
cv.waitKey(0)

haar_cascade=cv.CascadeClassifier('/Users/Development/OpenCV/haar_face.xml')

faces_rect= haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3) #1.1 is slow but accurate, 1.4 fast but missing tend, 3 is for use 3 rectangle to detect it's what I want

print(f'Number of faces found ={len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2) #x & y top left corner, w & h is width and height,0,255,0=green , x+w,y+h for bottom right corner
cv.imshow('Detected faces',img)


cv.waitKey(0)