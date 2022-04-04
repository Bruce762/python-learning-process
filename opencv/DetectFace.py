import cv2
from cv2 import imshow

img = cv2.imread('C:/python/kd.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades +'C:/python/opencv/faceDetect.xml')
faceRect = faceCascade.detectMultiScale(gray, 1.1, 3)#(gray, 縮小倍數, 偵測次數)回傳正方形
print(len(faceRect))
for (x, y, w, h) in faceRect:
    cv2.rectangle(img, (x, y), (x+w ,y+h), (0,255,0), 2)
imshow('img',img)
cv2.waitKey(0)