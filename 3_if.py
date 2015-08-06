#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

from RPi import GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(22, GPIO.IN)

entrada = GPIO.input(22)

if entrada:
    GPIO.output(4, 1)
else:
    GPIO.output(4, 0)

GPIO.cleanup()
