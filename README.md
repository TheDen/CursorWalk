# cursorwalk
Random walk implementation on the mouse cursor, as a screensaver! (https://en.wikipedia.org/wiki/Random_walk)

## Dependencies

pyautogui (https://github.com/asweigart/pyautogui)

`pip install pyautogui`

#### For Linux

Install the packages `python3-Xlib` (or `python-Xlib` for python2), and `python-tk` before installing `pyautogui`.

#### For macOS

OS X needs the `pyobjc-core` and `pyobjc` modules installed (in that order).

####For Windows

Windows does not need any dependecies for `pyautogui`

## Run

``./cursorwalk.py``

Runs with default options: `stepsize = 10` `ratespeed = 0.2` `timeout = 0`

#### Options

```
-s STEPSIZE, --stepsize STEPSIZE

                        pixel stepsize

-r RATESPEED, --ratespeed RATESPEED

                        seconds between each pixel move
                        
-t TIMEOUT, --timeout TIMEOUT

                        timeout for idle mouse to start random walk (seconds)

```

Cursorwalk can be run as a screensaver-type service, i.e., with the timeout `-t` option. The random walk won't start until the mouse is idle for the amount of seconds given. If the mouse is moved by the user (greater than the stepsize distance), the timeout will restart.

#### Example
Run cursorwalk to move 20 pixels, with 0.2 seconds between each pixel, with a timeout of 15 minutes.

`$ ./cursorwalk.py -s 20 -r 0.2 -t 900`
