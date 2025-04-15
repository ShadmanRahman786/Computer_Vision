import cv2 as cv
def rescaleFrame(frame,scale=0.2):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimension=(width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

img=cv.imread('/Users/Development/OpenCV/Photos/cat.jpeg')
cv.imshow('image',img)
resized_image=rescaleFrame(img)
cv.imshow('resized image',resized_image)
capture=cv.VideoCapture('/Users/Development/OpenCV/Videos/G-Eazy - I Mean It (Official Music Video) ft. Remo [CxnaPa8ohmM].mp4')

def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)
while True:
    isTrue,frame=capture.read()
    frame_resized=rescaleFrame(frame)
    cv.imshow('video',frame)
    cv.imshow('video resized',frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()

