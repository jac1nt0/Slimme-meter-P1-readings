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
      break

for item in msg:
    if ": 0.2.8" in item:
        version = int(item[-3: -1])/10
    elif ": 1.0.0" in item:
        time_stamp = time.strptime(item[-14:-2], "%y%m%d%H%M%S")
    elif "0-0: 96.1.1" in item:
        elec_identifier = item[-23:-1]
    elif ": 1.8.1" in item:
        t1_received = (item[-17:-6] ,item[-4:-1])
    elif ": 1.8.2" in item:
        t2_received = (item[-17:-6] ,item[-4:-1])
    elif ": 2.8.1" in item:
        t1_sent = (item[-17:-6] ,item[-4:-1])
    elif ": 2.8.2" in item:
        t2_sent = (item[-17:-6] ,item[-4:-1])
    elif ": 96.14.0" in item:
        tarif = item[-4:-1]
    elif ": 1.7.0" in item:
        pass
        
    else:
        print(item)
