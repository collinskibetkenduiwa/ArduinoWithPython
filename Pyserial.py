
# 1)pyserial
# python library that enables the access and control of Serial port 
# can be installed using pip install pyserial

# The adruino code used to  control the builtin light emitting diode

int led = 13;

void setup(){
    pinMode(led, OUTPUT);
    Serial.begin(9600);
}

void loop(){
  if (Serial.available()){
      char command = Serial.read();
      if (command=='o'){
        digitalWrite(led, HIGH);
      }
      else{
        digitalWrite(led, LOW);
      }
  }
}


# Python code to blind the LED

import time  
from serial import Serial

arduino_board = Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)

def blink():
  while True:
    arduino.write(b'o')
    time.sleep(1)
    arduino.write(b'f')
    time.sleep(1)

blink()

# Signal can also be read from sensors  connected to the ardruino board
# Eg.The light intentisy and LDR connected to the arduino pin A0 can be read using the  following code

int ldr = A0;

void setup(){
  pinMode(ldr, INPUT);
  Serial.begin(115200);
}

void loop(){
  int intensity = analogRead(ldr);
  if (Serial.available()){
    char command = Serial.read();
    if (command=='r') Serial.println(intensity);
  } 
}
# Python code to read the sensor signal sent by arduino
from serial import Serial

arduino = Serial('/dev/ttyUSB1', baudrate=115200, timeout=1)
arduino.flush

while True:
    arduino.write(b'r')
    light_intensity = arduino.readline().decode()
    print(light_intensity)
