#!/usr/bin/python

import serial
import time
import pyparsing
import logging

logging.basicConfig(filename='example.log',level=logging.DEBUG)

def meter():
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
      

