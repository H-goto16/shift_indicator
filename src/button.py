import time


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


def long_press(threshold):
    start_time = time.ticks_ms()
    while True:
        if time.ticks_ms() - start_time > threshold:
            return True
        else:
            return False

