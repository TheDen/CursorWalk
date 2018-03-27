#!/usr/bin/env python3

import random
import pyautogui
import time
import argparse
pyautogui.FAILSAFE =  False

parser = argparse.ArgumentParser()
parser.add_argument('-s', '--stepsize', default=10, type=int, help="pixel stepsize")
parser.add_argument('-r', '--ratespeed', default=0.2, type=float, help="seconds between each pixel move")
parser.add_argument('-t', '--timeout', default=0, type=float, help="timeout for idle mouse to start random walk (seconds)")

args = parser.parse_args()

stepsize = abs(args.stepsize)
speed =  abs(args.ratespeed)
timeout =  abs(args.timeout)

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

def main():
  while True:
    x = pyautogui.position()[0]
    y = pyautogui.position()[1]
    time.sleep(timeout)
    if x == pyautogui.position()[0] and pyautogui.position()[1]:
      startwalk(stepsize,speed)

if __name__ == "__main__":
  main()
