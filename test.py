from shutil import move
from turtle import Turtle
import pythoncom
import pyautogui
import time
import pydirectinput
import pynput
import mouse
import Xlib 
import autoit
import scipy.interpolate
import numpy as np
import ctypes
#from pywinauto import application,findwindows,mouse 
import pywinauto 
import win32api 
import keyboard
ispress=True
while True:
    if(keyboard.is_pressed("a") & ispress):
        ispress=False
    elif(keyboard.is_pressed("a")):
        ispress=True
    
    if(ispress): 
        print("sucess")
    else:
        print("nothing is pressed")
    if(keyboard.is_pressed("q")):
        break