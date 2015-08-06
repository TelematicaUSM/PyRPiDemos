#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

from RPi import GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(22, GPIO.IN)

print(GPIO.input(22))
GPIO.output(4, 1)

GPIO.cleanup()
