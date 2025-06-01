# DuckyDK Pad 7K2R

<img width="561" alt="Screenshot 2025-06-01 at 11 32 51 PM" src="https://github.com/user-attachments/assets/9705c22d-86f7-453a-9897-639602a7339f" />

## Features
- 7 Switches including 1 2.00u and 6 1.00u
- 2 Rotary knobs 
- 7 LEDs as backlight for switches

## Specifications
BOM:
- 7x Cherry MX Switches
- 6x Blank DSA 1.00u keycaps, 1x Blank DSA 2.00u keycap (with stabaliser slot)
- 7x SK6812 Neopixels
- 2x EC11 Rotary Encoder - RotaryEncoder_Switch
- 2x Rotary knob
- 1x XIAO RP2040
- 4x M3x5mx4mm heatset insert
- 4x M3x16mm screws
(Sadly, no stabilisers :c)

## Inspiration
This is my first time using electrical engineering to create a working macropad, which I have always wanted to try to make. I've always been interested in electrical engineering (I've made a simple lamp post model), and I wanted to continue my hobby. I use the Hackpad guide and people on Slack to help me understand and get used to the software. I wanted to used 8 keys and 2 Rotary Encoder, but I wasn't able to use 10 inputs with the Xiao RP2040 for it, so I learnt how to use a matrix and use 7 Keys and 2 Rotary encoder for my project. This is also why it's called the 7K2R - 7 Key and 2 Rotary encoders, (The DuckyDk refers to my username DuckyBoi_XD and DK for Drum Kit or Duck again)

## Firmware Overview  

The firmware of this macropad was made by QinCai and contains:

- 7 Keys which linked to macro key which can be changed
- 2 Rotary encoders,
  - 1 adjusting volume and a switch muting the volume
  - 1 adjusting mic volume and muting mic
- 7 LEDs under switches which we have as a single colour

### Schematics

<img width="250" alt="Screenshot 2025-06-02 at 10 05 05 AM" src="https://github.com/user-attachments/assets/70fbdcc0-8e3d-4209-bb58-b46020b64cd5" />

### PCB

<img width="250" alt="Screenshot 2025-06-02 at 10 05 43 AM" src="https://github.com/user-attachments/assets/4b7dda9d-7eed-4fc3-8c11-62f5fe9a9ab4" />

### Case

<img width="250" alt="Screenshot 2025-06-02 at 10 13 05 AM" src="https://github.com/user-attachments/assets/e890e0fb-b4a2-4df7-9757-06d4bdc7a7de" />

## Credit
I'd like to give credit to everyone who has helped in this project,

- [@Person20020 (Koji)](https://hackclub.slack.com/team/U07QNKS5SKA), for answering almost every question I had while making the pad, and pretty much telling me what to do because I had no clue. I'm thankful that Person20020 is an expert in Kicad and Fusion because without them, I wouldn't have been able to finish
- [@QinCai](https://hackclub.slack.com/team/U07BNRCEARM), for being my irl friend, introducing me to Hackclub, supporting me, giving me tips, helping with this repo, and making my firmware (I can't code)
- [@StrawberryPuding](https://hackclub.slack.com/team/U08290982KU), for answering my question when Person wasn't online and helping me understand Rotary encoders
- [@alexren](https://hackclub.slack.com/team/U06PR6B8D37) and [@acon](https://hackclub.slack.com/team/U04KEK4TS72), for being amazing organisers and often helping people like me with details and questions
- The entire Slack community, for answers to all my strange questions about Hackclub, Hackpad and electrical engineering in general

## Extra Information

The Fusion model contains a derived version of my case, which contains my bottom case and top case as well as the PCB export. I have the main version plus the models I derived from it, but it contains switches, stabilisers, rotary encoders and Xiao MCU models. I read the guide, and it says just to add a single file for the case so I did. If the person reviewing thing project needs the main file for the case, try to message me.
