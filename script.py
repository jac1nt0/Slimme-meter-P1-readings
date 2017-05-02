#!/usr/bin/python

import serial
import time
import pyparsing
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
fh = logging.FileHandler(filename='example.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
log.addHandler(fh)


class meter():
  defaults = {
    'baudrate' : 115200,
    'bytesize': serial.SEVENBITS,
    'parity': serial.PARITY_EVEN,
    'stopbits': serial.STOPBITS_ONE,
    'xonxoff': False,
    'timeout': 10,
  }
  
  def __init__(self, port='/dev/ttyUSB0', **kwargs):
    config = {}
    config.update(self.defaults)
    config.update(kwargs)
    
    log.debug('Open serial connect to {} with: {}'.format(port, ', '.join('{}={}'.format(key, value) for key, value in config.items())))

    try:
      self.serial = serial.Serial(port, **config)
    except (serial.SerialException,OSError) as e:
      raise SmartMeterError(e)
    else:
      self.serial.setRTS(False)
      self.port = self.serial.name

    log.info('New serial connection opened to %s', self.port)

  def connect(self):
    if not self.serial.isOpen():
      log.info('Opening connection to `%s`', self.serial.name)
      self.serial.open()
      self.serial.setRTS(False)
    else:
      log.debug('`%s` was already open.', self.serial.name)


  def disconnect(self):
    if self.serial.isOpen():
      log.info('Closing connection to `%s`.', self.serial.name)
      self.serial.close()
    else:
      log.debug('`%s` was already closed.', self.serial.name)


  def connected(self):
    return self.serial.isOpen()
  
  def read_one_packet(self):
    datagram = b''
    lines_read = 0
    startFound = False
    endFound = False
    max_lines = 35 #largest known telegram has 35 lines

    log.info('Start reading lines')

    while not startFound or not endFound:
      print startFound, endFound
      try:
        line = self.serial.readline()
        log.debug('>> %s', line.decode('ascii').rstrip())
      except Exception as e:
        log.error(e)
        log.error('Read a total of %d lines', lines_read)
        raise SmartMeterError(e)

        lines_read += 1

        if '/' in line:
          startFound = True
          endFound = False
          datagram = line.lstrip()
        elif '!' in line:
          endFound = True
          datagram = datagram + line
        else:
          datagram = datagram + line

        # TODO: build in some protection for infinite loops

    log.info('Done reading one packet (containing %d lines)' % len(datagram.splitlines()))
    log.debug('Total lines read from serial port: %d', lines_read)
    log.debug('Constructing P1Packet from raw data')

    return P1Packet(datagram)
      

if __name__=='__main__':
  a = meter()
  print a.read_one_packet()
