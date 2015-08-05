from time import sleep
from RPi import GPIO

def blink(veces, tiempo):
    encendido = False

    for i in range(veces):
        if encendido:
            GPIO.output(4, 1)
            encendido = False
        else:
            GPIO.output(4, 0)
            encendido = True
        sleep(tiempo)

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)
    blink(50, 0.1)
    blink(5, 1)
    blink(10, 0.5)

except KeyboardInterrupt:
    exit()

finally:
    GPIO.cleanup()
