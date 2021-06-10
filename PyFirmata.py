# the library can be installed using pip install pyFirmata
# PyFirmata is a python libary that alllow python to communicate with arduino over USB using standard firmata protocol, standard firmata

# The standard firmata code has to be uploaded to the ardruino board

# After uploading the code the following python code can be used to controll the blinking of light

import time
from pyfirmata import Arduino

board = Arduino('/dev/ttyUSB0')

def blink():
  while True:
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)

blink()


# python-code to read an LDR with firmata protocols
import time 
from pyfirmata import Arduino, util

board = Arduino('/dev/ttyUSB0')

util.Iterator(board).start()
board.analog[0].enable_reporting()

while True:
  light_intensity = board.analog[0].read()
  print(light_intensity)
  time.sleep(1) 



