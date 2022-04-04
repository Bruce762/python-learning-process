from turtle import color
import mediapipe as mp
import cv2

cap = cv2.VideoCapture(0)
mpHands = mp.python.solutions.hands#選擇用的模型
hands = mpHands.Hands()#Hands是其中一個函式
mpDraw = mp.solutions.drawing_utils
handLmsStyle = mpDraw.DrawingSpec(color=(0, 0, 255), thickness=10)
handconStyle = mpDraw.DrawingSpec(color=(0, 255, 0), thickness=10)


while True:
    ret, img = cap.read()
    if ret:
        img = cv2.flip(img, 1)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(imgRGB)#把rgb圖片放進來，變成一個class
        imgHeight = img.shape[0]
        imgWidth = img.shape[1]
        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:#放入偵測到的每一隻手
                #print(type(handLms))
                mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS, handLmsStyle, handconStyle)
                for i, lm in enumerate(handLms.landmark):
                    #print(type(lm))
                    xPos = int(lm.x * imgWidth)
                    yPos = int(lm.y * imgHeight)
                    cv2.putText(img, str(i), (xPos-25, yPos+5),cv2.FONT_HERSHEY_COMPLEX, 0.4, (0,0,255), 2)
                    #print(i, xPos, yPos)
        cv2.imshow('img',img)


    if cv2.waitKey(1) == ord('q'):
        break