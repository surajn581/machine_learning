import numpy as np
import cv2

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
fist_cascade = cv2.CascadeClassifier('fist.xml')
#palm_cascade1 = cv2.CascadeClassifier('aGest.xml')
#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
palm_cascade = cv2.CascadeClassifier('Hand_haar_cascade.xml')

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(cv2.CAP_DSHOW)

while 1:
    ret, img = cap.read()
    img = cv2.flip(img,1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    fists = fist_cascade.detectMultiScale(gray, 1.3, 5)
    #print(fists)
    for (x,y,w,h) in fists:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        #roi_gray = gray[y:y+h, x:x+w]
        #roi_color = img[y:y+h, x:x+w]
        
    palms = palm_cascade.detectMultiScale(gray, 1.3, 5)
    #palms1= palm_cascade1.detectMultiScale(gray,1.3, 5)
    #print(palms)
    for (ex,ey,ew,eh) in palms:
        cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (fx,fy,fw,fh) in faces:
        cv2.rectangle(img,(fx,fy),(fx+fw,fy+fh),(0,0,255),2)

    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()