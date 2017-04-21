import serial
import time

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)

for x in range(5):
  msg = []
  while True:
    msg.append(ser.readline())
    if '!' in msg[-1]:
      print msg
      break
