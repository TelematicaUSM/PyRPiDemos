---
author: Cristóbal Ganter
lang: spanish
title: 'Contenidos'
...

Esta clase está basada en:

    -   <https://www.raspberrypi.org/documentation/usage/python/>
    -   <https://www.raspberrypi.org/documentation/usage/python/more.md>
    -   <https://www.raspberrypi.org/documentation/usage/gpio-plus-and-raspi2/README.md>

Mas información:

    -   <https://docs.python.org>

1.  Demo

<!-- 2.  ¿Donde se usa python?
    a.  Desarrollo de software
    b.  Arte
    c.  Negocios
    d.  Educación
    e.  Gobierno
    f.  Ciencia
    g.  Ingeniería

    h.  Google
    i.  Youtube
    j.  Reddit
    k.  Nasa
    l.  Yahoo
    m.  Cern -->

<!-- 3.  IDLE
    a.  Python 2 y 3
    b.  Calculadora -->

<!-- 4.  Hello World -->

5.  Indentación

    for i in range(2):
        print("A")
        print("B")

<!-- 6.  Variables (no tienen un tipo determinado) -->

<!-- 7.  Comentarios

8.  Listas

9.  Iteración
    a.  Iterables
        -   Listas
        -   Strings

10. Range
    a.  Los enteros no son iterables.
    b.  Limites -->
<!--
11. Len

12. If (== != < > <= >=) -->

13. Archivos
    <!-- -   IDLE -->
    -   Consola

<!-- 14. help() -->

15. Bibliotecas
    a.  ¿Qué es una biblioteca?
    b.  Bibliotecas estandar
        -   datetime
        -   re
        -   os
        -   sqlite3
        -   json
        -   random
        -   infinitos otros ...
    c.  Otras Bibliotecas (<https://pypi.python.org>)
        -   Pillow
        -   Scrapy
        -   Matplotlib
        -   PyGame
        -   NumPy
        -   ScyPy
        -   Tornado
        -   DJango
        -   PyOpenCV
        -   infinitos otros ...
    d.  Instalar Bibliotecas
        <!-- i.  apt

            sudo apt-get install python-picamera -->

        ii. pip

            sudo apt-get install python3-pip
            sudo pip-3.2 install tornado RPi.GPIO

    e.  imports

16. Armar circuito

17. GPIO

    from RPi import GPIO
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(22, GPIO.IN)

    print(GPIO.input(22))
    GPIO.output(4, 1)

    GPIO.cleanup()

18. If

    if not encender and apagar:
        GPIO.output(4, 0)

19. for

    for i in range(5):
        print('hola')

20. sleep

    from time import sleep
    sleep(3)

21. if, for, sleep

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

22. Funciones
    explicar globales

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)

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

23. try

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

24. Objetos
    -   agrupaciones de variables y funciones
    -   funcionan como una abstracción de un objeto real
    -   en python todo es un objeto

        >>> 'Hola'.upper()
        'HOLA'
        >>> 'Hola'.lower()
        'hola'

    -   Cada objeto tiene un tipo que determina su comportamiento
    -   clases
        -   es como el molde para crear

25. Ejemplo perros

26. Demo final.
