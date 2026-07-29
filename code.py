import time
import usb_hid
import adafruit_ducky
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)

layout = KeyboardLayoutUS(keyboard)

duck = adafruit_ducky.Ducky(
    "payload.txt",
    keyboard,
    layout
)

time.sleep(1)

i = 0
while i < 60:
    keyboard.press(Keycode.F1)
    keyboard.release_all()
    time.sleep(0.5)
    i += 1



keyboard.press(Keycode.ENTER)
keyboard.release_all()

while True:
    result = duck.loop()
    if result is False:
        keyboard.press(Keycode.KEYPAD_PLUS)
        keyboard.release_all()
        keyboard.press(Keycode.F10)
        keyboard.release_all()
        break
