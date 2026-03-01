import rp2

from button import SmartButton
from display import DisplayNumber, calibration, initalization
from save import load


def main():
    print("Shift Indicator Booting...")
    initalization()
    saved_data = load()

    print(saved_data)

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
