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
NUM_PIXELS = 8    # i think

# Initialise keyboard
keyboard = KMKKeyboard()

# Configure diode orientation - 1N4148 diodes
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Matrix pins
# ROW pins are connected to GPIO0/TX (ROW 2), GPIO1/RX (ROW 1), and GPIO2/SCK (ROW 0)
keyboard.row_pins = (board.SCK, board.RX, board.TX)  # ROW 0, ROW 1, ROW 2

# COL pins are connected to GPIO6/SDA (COL 2), GPIO7/SCL (COL 1), and GPIO29/ADC3 (COL 0)
keyboard.col_pins = (board.A3, board.SCL, board.SDA)  # COL 0, COL 1, COL 2

# Initialise modules
macros = Macros()
media_keys = MediaKeys()

rgb_pin = board.A0

# set the RGB LEDs to full white
pixels = neopixel.NeoPixel(rgb_pin, NUM_PIXELS, brightness=1.0, auto_write=True)
pixels.fill((255, 255, 255))  # Set all LEDs to full white

# Initialise encoder handler for two rotary encoders
encoder_handler = EncoderHandler()

# Configure encoder pins:
# Encoder 1: ROT1-A (GPIO27/ADC1), ROT1-B (GPIO28/ADC2)
# Encoder 2: ROT2-A (GPIO4/MISO), ROT2-B (GPIO3/MOSI)
encoder_handler.pins = (
    (board.A1, board.A2, KC.MUTE),  # Encoder 1 (SW2) - Volume control with mute
    (board.MISO, board.MOSI, KC.MUTE)  # Encoder 2 (SW1) - Brightness control with mute (idk what to change it to)
)

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
# Encoder 2: Brightness control with mute (idk what to change it to)
encoder_handler.map = (
    ((KC.VOLD, KC.VOLU, KC.MUTE), (KC.BRID, KC.BRIU, KC.MUTE)),
)

if __name__ == "__main__":
    keyboard.go()
