import serial
import time

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)
for x in range(10):
  print ser.readline()
  time.sleep(1)
