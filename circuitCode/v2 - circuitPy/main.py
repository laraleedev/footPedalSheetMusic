# Trinket M0: https://adafruit.com/product/3500
# Modified default Circuitpy code
# Default code is here:
# https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino/circuitpython
# This code belongs in the CIRCUITPY root folder next to all the other default files
# from the Trinket Default Zip Install: 
# https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino/circuitpython#trinket-default-zip-install-6-15

import board
from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import adafruit_dotstar as dotstar

# One pixel connected internally!
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)

# Digital input with pullup on D2
button = DigitalInOut(board.D2)
button.direction = Direction.INPUT
button.pull = Pull.UP

# Used if we do HID output, see below
kbd = Keyboard()

######################### HELPERS ##############################

# Helper to give us a nice color swirl
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0):
        return (0, 0, 0)
    if (pos > 255):
        return (0, 0, 0)
    if (pos < 85):
        return (int(pos * 3), int(255 - (pos*3)), 0)
    elif (pos < 170):
        pos -= 85
        return (int(255 - pos*3), 0, int(pos*3))
    else:
        pos -= 170
        return (0, int(pos*3), int(255 - pos*3))

######################### MAIN LOOP ##############################

i = 0
while True:
    # spin internal LED around! autoshow is on
    dot[0] = wheel(i & 255)

    if not button.value:
        kbd.press(Keycode.N)
    else:
        kbd.release_all()

    i = (i+1) % 256  # run from 0 to 255