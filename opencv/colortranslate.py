from tkinter import N
import cv2
from cv2 import dilate
from cv2 import erode
import numpy as np

kernel = np.ones((3, 3),np.uint8)
kernel1 = np.ones((3, 3),np.uint8)

img = cv2.imread('D:\workfile\python\opencv\dogg.jpg')
img = cv2.resize(img,(300,300))

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#變灰色
blur = cv2.GaussianBlur(img, (5,5), 0)#變模糊cv2.GaussianBlur(img, 數字都要是奇數, 標準差)
canny = cv2.Canny(img, 200,225)
Dilate = cv2.dilate(canny,kernel, iterations=1)#邊緣變粗dilate(canny,kernel陣列越大線條越粗, iterations=1變粗幾次)
Erode = cv2.erode(Dilate,kernel1, iterations=2)#邊緣變細dilate(canny,kernel陣列越大線條越細, iterations=1變細幾次)
'''
cv2.imshow('img',img)
cv2.imshow('blur',blur)
cv2.imshow('gray',gray)
'''
cv2.imshow('dilate',Dilate)
cv2.imshow('canny',canny)
cv2.imshow('Erode',Erode)
cv2.waitKey(0)