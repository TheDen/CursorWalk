#!/usr/bin/env python

import random
import pyautogui

x = pyautogui.position()[0]
y = pyautogui.position()[1]
step = random.randrange(5)
speed =  0.1
while True:
 step = random.randrange(5)
 if step == 0:
   pyautogui.moveTo(x+1, y, duration=speed)
 elif step == 1:
   pyautogui.moveTo(x-1, y, duration=speed)
 elif step == 2:
   pyautogui.moveTo(x, y+1, duration=speed)
 elif step == 3:
   pyautogui.moveTo(x, y-1, duration=speed)
