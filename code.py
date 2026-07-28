import time
import usb_hid
import adafruit_ducky
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS


keyboard = Keyboard(usb_hid.devices)

layout = KeyboardLayoutUS(keyboard)

duck = adafruit_ducky.Ducky(
    "payload.txt",
    keyboard,
    layout
)

time.sleep(1)

while True:
    result = duck.loop()
    if result is False:
        break
