import cv2 as cv
img=cv.imread('/Users/Development/OpenCV/Photos/cat.jpeg')
cv.imshow('Cat',img)
cv.waitKey(0)

capture=cv.VideoCapture('/Users/Development/OpenCV/Videos/G-Eazy - I Mean It (Official Music Video) ft. Remo [CxnaPa8ohmM].mp4')
while True:
    isTrue,frame=capture.read()
    cv.imshow('Video',frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
