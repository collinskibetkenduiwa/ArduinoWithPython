# The library can be installed using $ pip install arduino-python3

# Arduino-python3 A light-weight Python library that provides a serial bridge for communicating with Arduino microcontroller boards, It is written using a custom protocol, similar to Firmata.

# To get strated the prototype protocoal code has to be uploaded to the adruino

# Code to Blink an LED with Arduino command API 

import time
from Arduino import Arduino

board = Arduino()
board.pinMode(13, "OUTPUT")

while True:
    board.digitalWrite(13, "HIGH")
    time.sleep(1)
    board.digitalWrite(13, "LOW")
    time.sleep(1)

    #  arduino code to read signal from LDR using custom protocol

    import time
from Arduino import Arduino

board = Arduino()

while True:
    light_intensity = board.analogRead(0)
    print(light_intensity)
    time.sleep(0.1)

    