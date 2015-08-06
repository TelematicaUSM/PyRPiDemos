#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

from time import sleep
from RPi import GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

encendido = False
for i in range(10):
    if encendido:
        GPIO.output(4, 1)
        encendido = False
    else:
        GPIO.output(4, 0)
        encendido = True
    sleep(1)

GPIO.cleanup()
