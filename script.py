import serial
import time

ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)

while True:
  print ser.readline()
