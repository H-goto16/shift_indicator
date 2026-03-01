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
LED = Pin(25, Pin.OUT)

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
    "R": [1, 1, 1, 0, 1, 1, 1, 0],
    "L": [0, 0, 0, 1, 1, 1, 0, 0],
    "E": [1, 0, 0, 1, 1, 1, 1, 1],
    "S": [1, 0, 1, 1, 0, 1, 1, 1],
    "A": [1, 1, 1, 0, 1, 1, 1, 1],
    "V": [0, 1, 1, 1, 1, 1, 0, 1],
}

class SmartButton:
    def __init__(self, pin_func, threshold_ms=3000):
        self.get_value = pin_func
        self.threshold = threshold_ms
        self.start_time = None
        self.long_pressed = False
        self.clicked = False

    def check(self):
        is_pressed = self.get_value() == 1

        if is_pressed:
            if self.start_time is None:
                self.start_time = time.ticks_ms()
                self.long_pressed = False
                self.clicked = False
            else:
                elapsed = time.ticks_diff(time.ticks_ms(), self.start_time)
                if elapsed > self.threshold and not self.long_pressed:
                    self.long_pressed = True
                    return True
        else:
            if self.start_time is not None:
                if not self.long_pressed:
                    self.clicked = True

            self.start_time = None
            self.long_pressed = False

        return False

    def is_clicked(self):
        if self.clicked:
            self.clicked = False
            return True
        return False

def clear():
    for pin in pins:
        pin.value(1)

def DisplayNumber(number):
    map = digit_map[number]
    for index, pin in enumerate(pins):
        pin.value(not map[index])

def long_press(threshold):
    start_time = time.ticks_ms()
    while True:
        if time.ticks_ms() - start_time > threshold:
            return True
        else:
            return False

def calibration(button_obj):
    modes = [0, 1, 2, 3, 4, 5, "R"]
    current_idx = -1

    saved_values = {}

    DisplayNumber("L")
    print("Entered Calibration Mode")

    while True:
        is_long = button_obj.check()

        if is_long:
            print(f"Final Data Saved: {saved_values}")
            for char in ["S", "A", "V", "E"]:
                DisplayNumber(char)
                time.sleep(0.1)
            clear()
            break

        if button_obj.is_clicked():
            current_idx = (current_idx + 1) % len(modes)
            target_mode = modes[current_idx]
            DisplayNumber(target_mode)
            print(f"Mode: {target_mode} (Index: {current_idx})")

        time.sleep(0.01)

def initalization():
    clear()
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
    clear()

def main():
    print("Shift Indicator Booting...")
    initalization()

    start_time = None
    bootsel_botton = SmartButton(rp2.bootsel_button, 3000)

    print("Display Current Shift Pattern")
    while True:
        try:
            if bootsel_botton.check():
                print("Calibration")
                calibration(bootsel_botton)

        except Exception as e:
            DisplayNumber("E")
            print(e)


if __name__ == "__main__":
    main()