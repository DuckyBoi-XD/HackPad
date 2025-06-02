# HackPad Firmware Overview

This is an overview of the firmware for the Ducky DK macroboard, as implemented in [`firmware/KMK/main.py`](https://github.com/DuckyBoi-XD/HackPad/blob/main/firmware/KMK/main.py). The firmware is built using the [KMK firmware](https://github.com/KMKfw/kmk_firmware), a Python-based firmware for mechanical keyboards.

---

## Key Components

### 1. Hardware Configuration
- **Matrix Pins:**
  - **Rows:** GPIO2/SCK, GPIO29/ADC3/A3, GPIO0/TX
  - **Columns:** GPIO1/RX, GPIO6/SDA, GPIO7/SDA
  - **Diode Orientation:** COL2ROW (1N4148 diodes)
- **RGB LEDs:**
  - Uses 7 NeoPixel-compatible RGB LEDs connected to `board.A0`  pls check
  - All LEDs are set to full white at startup with adjustable brightness
- **Rotary Encoders:**
  - Two rotary encoders are supported
    - Encoder 1: Pins `board.A1`, `board.A2` pls check
    - Encoder 2: Pins `board.MISO`, `board.MOSI` pls check

### 2. Modules & Extensions
- **Media Keys:** Support for media key actions (volume, mute, etc.)
- **Macros:** Enables key macros for common shortcuts (e.g., copy, paste)
- **Encoder Handler:** Manages rotary encoder actions

### 3. LED Backlight Control
- Functions to:
  - Increase/decrease LED brightness
  - Toggle back-light on/off

### 4. Keymap & Layers
- **Single-layer keymap** (for now) with shortcuts:
  - **Row 0:** Save, Spotlight, Mission Control
  - **Row 1:** Copy, Paste, Cut
  - **Row 2:** New Tab, Undo, Escape

### 5. Encoder Mapping
- **Encoder 1:** Controls system audio (Volume Down, Volume Up, Mute)
- **Encoder 2:** Controls RGB LED brightness (decrease/increase/toggle)

### 6. Startup
- The keyboard is initialised and run with `keyboard.go()` in the standard Python entry point.

---

## References

- KMK Firmware Docs: [https://github.com/KMKfw/kmk_firmware/tree/main/docs/en](https://github.com/KMKfw/kmk_firmware/tree/main/docs/en)
- [Source code on GitHub](https://github.com/DuckyBoi-XD/HackPad/blob/main/firmware/KMK/main.py)
