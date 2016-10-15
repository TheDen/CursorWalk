#!/usr/bin/env python

import random
import pyautogui
import time
import argparse
pyautogui.FAILSAFE =  False

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--stepsize', default=10, type=int, help="pixel stepsize")
parser.add_argument('-s', '--speed', default=0.1, type=float, help="secons to move between pixels")
parser.add_argument('-t', '--timeout', default=0, type=float, help="timeout for idle mouse to start random walk")

args = parser.parse_args()

stepsize = args.stepsize
speed =  args.speed
timeout =  args.timeout

def startwalk(stepsize, speed):
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
  if x-pyautogui.position()[0] > stepsize or y-pyautogui.position()[1] > stepsize:
   break

while True:
  x = pyautogui.position()[0]
  y = pyautogui.position()[1]
  time.sleep(timeout)
  if x == pyautogui.position()[0] and pyautogui.position()[1]:
   startwalk(stepsize,speed)
