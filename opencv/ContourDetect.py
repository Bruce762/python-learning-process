import cv2

img = cv2.imread('C:\python\opencv\shape.jpg')
img = cv2.resize(img,(0,0), fx=0.5, fy=0.5)
imgContour = img.copy()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(img, 150, 200)
contours, hierarchy= cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)#(canny, 外輪廓, 近似方法)
#會回傳兩個數值第一個是邊框數值
for cnt in contours:
    cv2.drawContours(imgContour, cnt, -1, (255,0,0), 4)#(要畫的圖片, 數值, -1(全塗滿), 顏色, 線條粗度)
    print(cv2.contourArea(cnt))
    #print(cv2.arcLength(cnt, True))#邊長cv2.arcLength(cnt, 是否閉合)
    area = cv2.contourArea(cnt)
    if area > 500:
        peri = cv2.arcLength(cnt, True)
        vertices = cv2.approxPolyDP(cnt, peri*0.025, True)#幾邊形(,近似值(越大邊越少),是否閉合)
        print(len(vertices))
        coners = len(vertices)
        x, y, w, h =cv2.boundingRect((vertices))#傳座標
        cv2.rectangle(imgContour, (x, y), (x+w, y+h), (0,255,0), 4)#(imgContour, 座標, 座標, 顏色, 邊粗細)
        if coners== 3:
            cv2.putText(imgContour, 'triangle', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 255),1)
        if coners== 4:
            cv2.putText(imgContour, 'rectangle', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 255),1)
        if coners== 5:
            cv2.putText(imgContour, 'pentagon', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 255),1)
        if coners>= 6:
            cv2.putText(imgContour, 'circle', (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0, 0, 255),1)
        
cv2.imshow('img',img)
cv2.imshow('canny',canny)
cv2.imshow('imgcontour',imgContour)
cv2.waitKey(0)