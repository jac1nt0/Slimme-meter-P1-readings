import serial
import time
import pyparsing

class DataPackage():
  

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)

for x in range(5):
  msg = []
  while True:
    msg.append(ser.readline()[:-2])
    if '!' in msg[-1]:
      for item in msg:
        print msg
      break

