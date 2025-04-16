import os
import numpy as np
import cv2 as cv

people=['Ana_de_armas','Megan_fox']
p=[]
for i in os.listdir(r'/Users/Development/OpenCV/Faces/train'):
    p.append(i)

print(p)

DIR=r'/Users/Development/OpenCV/Faces/train'
haar_cascade=cv.CascadeClassifier('/Users/Development/OpenCV/haar_face.xml')
features=[]
labels=[]

def create_train():
    for person in people:
        path=os.path.join(DIR,person)
        label=people.index(person)
        for img in os.listdir(path):
            img_path=os.path.join(path,img)
            img_array=cv.imread(img_path)
            gray=cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)

            faces_rect= haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
            for (x,y,w,h) in faces_rect:
                faces_roi=gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)
                

create_train()
print('Training done---------')
print(f'Length of the features = {len(features)}')
print(f'Length of labels = {len(labels)}')

features=np.array(features,dtype='object')
labels=np.array(labels)

face_recognizer=cv.face.LBPHFaceRecognizer_create()
#Train the recognizer on the features list and the labels list
face_recognizer.train(features,labels)
face_recognizer.save('face_train.yml')
np.save('features.npy',features)
np.save('labels.npy',labels)