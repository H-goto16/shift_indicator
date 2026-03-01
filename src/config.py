from machine import Pin

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
LED = Pin(25, Pin.OUT)

PINS = [TOP, RIGHT_TOP, RIGHT_BOTTOM, BOTTOM, LEFT_BOTTOM, LEFT_TOP, CENTER, DECIMAL]

DIGIT_MAP = {
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
    "R": [1, 1, 1, 0, 1, 1, 1, 0],
    "L": [0, 0, 0, 1, 1, 1, 0, 0],
    "E": [1, 0, 0, 1, 1, 1, 1, 1],
    "S": [1, 0, 1, 1, 0, 1, 1, 1],
    "A": [1, 1, 1, 0, 1, 1, 1, 1],
    "V": [0, 1, 1, 1, 1, 1, 0, 1],
}

