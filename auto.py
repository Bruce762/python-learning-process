import pyautogui
import cv2

img = pyautogui.screenshot(region=[0,0,100,100]) # x,y,w,h
img.save('screenshot.png')
#img = cv2.cvtColor(np.asarray(img),cv2.COLOR_RGB2BGR)
