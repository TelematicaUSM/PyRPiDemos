#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

from time import sleep
from RPi import GPIO


def blink(veces, tiempo):
    cambios = 2 * veces
    encendido = False
    GPIO.output(4, 0)

    for i in range(cambios):
        if encendido:
            GPIO.output(4, 0)
            encendido = False
        else:
            GPIO.output(4, 1)
            encendido = True
        sleep(tiempo / cambios)

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)

    blink(10, 5)
    blink(20, 5)
    blink(40, 5)

except KeyboardInterrupt:
    exit()

finally:
    GPIO.cleanup()
