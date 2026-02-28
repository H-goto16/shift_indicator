from os import GRND_NONBLOCK
from machine import Pin
import time

## GP0 decimal
## GP1 right bottom
## GP2 bottom
## GP3 left bottom
## GP4 right top
## GP5 top
## GP6 left top
## GP7 center middle
## GP8 off

## = 7 Segments LED =
##      -- GP5 --
##  GP6|         |GP4
##      -- GP7 --
##  GP3|         |GP1
##      -- GP2 --  .GP0
##         VSYS


## = 7 Segments Pin assign =
## RT RT OFF TOP RT
##       8.
## LB BM INPUT RB DECIMAL

## Raspico Pin assign
# GP0 VBUS
# GP1 VSYS
# GND GND
# GP2
# GP3
# GP4
# GP5
# GND
# GP6
# GP7
# GP8


DECIMAL = Pin(0, Pin.OUT)
RIGHT_BOTTOM = Pin(1, Pin.OUT)
BOTTOM = Pin(2, Pin.OUT)
LEFT_BOTTOM = Pin(3, Pin.OUT)
RIGHT_TOP = Pin(4, Pin.OUT)
TOP = Pin(5, Pin.OUT)
LEFT_TOP = Pin(6, Pin.OUT)
CENTER = Pin(7, Pin.OUT)
OFF = Pin(8, Pin.OUT)

pins = [TOP, RIGHT_TOP, RIGHT_BOTTOM, BOTTOM, LEFT_BOTTOM, LEFT_TOP, CENTER, DECIMAL]

digit_map = {
    # TOP, RT, RB, BT, LB, LT, CENTER, DECIMAL
    0: [1, 1, 1, 1, 1, 1, 0, 0],
    1: [0, 1, 1, 0, 0, 0, 0, 0],
    2: [1, 1, 0, 1, 1, 0, 1, 0],
    3: [1, 1, 1, 1, 0, 0, 1, 0],
    4: [0, 1, 1, 0, 0, 1, 1, 0],
    5: [1, 0, 1, 1, 0, 1, 1, 0],
    6: [1, 0, 1, 1, 1, 1, 1, 0],
    7: [1, 1, 1, 0, 0, 1, 0, 0],
    8: [1, 1, 1, 1, 1, 1, 1, 0],
    9: [1, 1, 0, 1, 1, 1, 1, 0],
    "R": [1, 1, 1, 0, 1, 1, 1, 0]
}

def DisplayNumber(number):
    map = digit_map[number]
    for index, pin in enumerate(pins):
        pin.value(not map[index])

def initalization():
    for pin in pins:
        pin.value(1)

    for i in range(10):
        duration = 0.01
        DECIMAL.value(0)
        BOTTOM.value(0)
        time.sleep(duration)
        BOTTOM.value(1)
        LEFT_BOTTOM.value(0)
        time.sleep(duration)
        LEFT_BOTTOM.value(1)
        LEFT_TOP.value(0)
        time.sleep(duration)
        LEFT_TOP.value(1)
        TOP.value(0)
        DECIMAL.value(1)
        time.sleep(duration)
        TOP.value(1)
        RIGHT_TOP.value(0)
        time.sleep(duration)
        RIGHT_TOP.value(1)
        RIGHT_BOTTOM.value(0)
        time.sleep(duration)
        RIGHT_BOTTOM.value(1)

def main():
    initalization()
    for i in range(6):
        DisplayNumber(i)
        time.sleep(0.5)

    DisplayNumber("R")



if __name__ == "__main__":
    main()