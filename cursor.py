#!/usr/bin/env python

import random
import pyautogui

x = pyautogui.position()[0]
y = pyautogui.position()[1]
step = random.randrange(5)
stepsize = 10
speed =  0.01
while True:
 x = pyautogui.position()[0]
 y = pyautogui.position()[1]
 step = random.randrange(5)
 if step == 0:
   pyautogui.moveTo(x+stepsize, y, duration=speed)
 elif step == 1:
   pyautogui.moveTo(x-stepsize, y, duration=speed)
 elif step == 2:
   pyautogui.moveTo(x, y+stepsize, duration=speed)
 elif step == 3:
   pyautogui.moveTo(x, y-stepsize, duration=speed)
