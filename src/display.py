import time
from save import save
from config import (
    BOTTOM,
    DECIMAL,
    LEFT_BOTTOM,
    LEFT_TOP,
    PINS,
    RIGHT_BOTTOM,
    RIGHT_TOP,
    TOP,
    DIGIT_MAP,
)


def clear():
    for pin in PINS:
        pin.value(1)


def DisplayNumber(number):
    mapping = DIGIT_MAP[number]
    for index, pin in enumerate(PINS):
        pin.value(not mapping[index])


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
            save(saved_values)
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
    for _ in range(10):
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

