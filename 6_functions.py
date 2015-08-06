#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

from time import sleep
from RPi import GPIO

def blink(veces, tiempo):
    encendido = False
    GPIO.output(4, 0)

    for i in range(2*veces):
        if encendido:
            GPIO.output(4, 0)
            encendido = False
        else:
            GPIO.output(4, 1)
            encendido = True
        sleep(tiempo)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

blink(100, 0.05)
blink(50, 0.1)
blink(5, 1)
blink(10, 0.5)

GPIO.cleanup()
