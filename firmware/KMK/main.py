################################################################################
#                 Mozilla Public License Version 2.0                           #
#                                                                              #
#     This Source Code Form is subject to the terms of the Mozilla Public      #
#     License, v. 2.0. If a copy of the MPL was not distributed with this      #
#     file, You can obtain one at http://mozilla.org/MPL/2.0/.                 #
#                                                                              #
#         .d88b.  d888888b d8b   db  .o88b.  .d8b.  d888888b                   #
#        .8P  Y8.   `88'   888o  88 d8P  Y8 d8' `8b   `88'                     #
#        88    88    88    88V8o 88 8P      88ooo88    88                      #
#        88    88    88    88 V8o88 8b      88~~~88    88                      #
#        `8P  d8'   .88.   88  V888 Y8b  d8 88   88   .88.                     #
#         `Y88'Y8 Y888888P VP   V8P  `Y88P' YP   YP Y888888P                   # 
#                     Made with love by Raymont Qin                            #
#             https://qincai.xyz    github.com/QinCai-rui                      #
#                                                                              #
#      - You are free to use, share, and modify this code.                     #
#      - If you change the code and share it, you must keep it open.           #
#      - The full license text is here: http://mozilla.org/MPL/2.0/            #
#                                                                              #
#      In simple terms:                                                        #
#        - You can use this for personal or commercial projects.               #
#        - If you improve or change the code and share it,                     #
#          you must share your changes under the same license.                 #
#        - You do NOT have to share your whole project, just the changes       #
#          to this file.                                                       #
################################################################################


################################################################################
# VERY USEFUL: https://github.com/KMKfw/kmk_firmware/tree/main/docs/en         #
################################################################################

import board
import busio
from digitalio import DigitalInOut, Direction, Pull

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.macros import Macros
from kmk.modules.encoder import EncoderHandler

import neopixel

# Number of RGB LEDs in the keyboard
NUM_PIXELS = 7

# Initialise keyboard
keyboard = KMKKeyboard()

# Configure diode orientation - 1N4148 diodes
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Matrix pins
# ROW pins are connected to GPIO0/TX (ROW 2), GPI29/A3 (ROW 1), and GPIO2/SCK (ROW 0)
keyboard.row_pins = (board.SCK, board.A3, board.TX)  # ROW 0, ROW 1, ROW 2

# COL pins are connected to GPIO7/SCL (COL 2), GPIO6/SDA (COL 1), and GPIO1/RX (COL 0)
keyboard.col_pins = (board.RX, board.SDA, board.SCL)  # COL 0, COL 1, COL 2

# Initialise modules
macros = Macros()
media_keys = MediaKeys()

rgb_pin = board.A0

# set the RGB LEDs to full white
pixels = neopixel.NeoPixel(rgb_pin, NUM_PIXELS, brightness=1.0, auto_write=True)
pixels.fill((255, 255, 255))  # Set all LEDs to full white

# Add a variable to keep track of brightness
led_brightness = 1.0

# Custom functions to change LED brightness
def increase_led_brightness():
    global led_brightness
    led_brightness = min(1.0, led_brightness + 0.05)
    pixels.brightness = led_brightness

def decrease_led_brightness():
    global led_brightness
    led_brightness = max(0.0, led_brightness - 0.05)
    pixels.brightness = led_brightness

def toggle_led_backlight():
    global led_brightness
    if led_brightness > 0:
        led_brightness = 0
    elif led_brightness == 0:
        led_brightness = 1.0
    pixels.brightness = led_brightness

# Initialise encoder handler for two rotary encoders
encoder_handler = EncoderHandler()

# Configure encoder pins:
# Encoder 1: ROT2-A (GPIO4/MISO), ROT2-B (GPIO3/MOSI)
# Encoder 2: ROT1-A (GPIO27/ADC1), ROT1-B (GPIO28/ADC2)
keyboard.encoder_pins = [
    (board.MISO, board.MOSI), # Encoder 1 (A and B)
    (board.A1, board.A2),     # Encoder 2 (A and B)
]

# Common macros
COPY = KC.LGUI(KC.C)  # Command+C for macOS
PASTE = KC.LGUI(KC.V)  # Command+V ''
CUT = KC.LGUI(KC.X)    # Command+X ''
UNDO = KC.LGUI(KC.Z)   # Command+Z ''
SAVE = KC.LGUI(KC.S)   # Command+S ''
SPOTLIGHT = KC.LGUI(KC.SPACE)  # Command+Space for Spotlight
MISSION = KC.LGUI(KC.UP)  # Command+Up for Mission Control

# Add extensions and modules to the keyboard
keyboard.extensions.append(media_keys)
keyboard.modules.append(macros)
keyboard.modules.append(encoder_handler)

# Define keyboard layout - single layer (for now) with most useful functions
keyboard.keymap = [
    [
        # ROW 0
        SAVE,            SPOTLIGHT,   MISSION,
        # ROW 1
        COPY,            PASTE,       CUT,
        # ROW 2
        KC.LGUI(KC.TAB), UNDO,        KC.ESC
    ]
]

# Configure encoders
# Encoder 1: Volume control with mute
# Encoder 2: LED Brightness control with mute
encoder_handler.map = (
    (KC.VOLD, KC.VOLU, KC.MUTE),
    (decrease_led_brightness, increase_led_brightness, toggle_led_backlight),
)

if __name__ == "__main__":
    keyboard.go()
