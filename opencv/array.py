import numpy as np
import cv2
import random

img = cv2.imread('D:\workfile\python\opencv\dogg.jpg')
#img = np.empty((300高, 300寬, 3), np.uint8)
img = cv2.resize(img,(0,0),fx=0.5,fy=0.5)#cv2.resize(img,實際pt,倍數,倍數)
for row in range(100):
    for col in range(img.shape[1]):
        img[row][col]=[random.randint(0,255),random.randint(0,255),random.randint(0,255)]#G B R
newimg = img[100:200,100:1000]#擷取
cv2.imshow('newimg',newimg)#cv2.imshow('WebaPageName',物件名子)
cv2.imshow('img',img)
print(img.shape)
cv2.waitKey(0)
