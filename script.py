import serial
import time

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)

for x in range(5):
  msg = []
  while True:
    line = ser.readline()
    print line
    msg.append(line)
    if '!' in line:
      print msg
      break
