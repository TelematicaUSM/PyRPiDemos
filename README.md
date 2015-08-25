# PyRPiDemos

Este repositorio contiene una colección de programas de
ejemplo, diseñada para introducir a la programación a niños
de educación básica y media. Los ejemplos están escritos en
Python (versión 3.2) y están pensados para ser ejecutados en
una Raspberry Pi B+.

Estos ejemplos no pretenden ser una introducción formal y
detallada a la programación, mas bien buscan mostrar el
potencial de esta disciplina y entusiasmar a los alumnos a
aprender más. Además, los ejemplos están ordenados de manera
incremental. De esta forma en cada uno de ellos se agregan
nuevos elementos. El ejemplo final combina los elementos de
todos los ejemplos anteriores.

Para ejecutar los ejemplos se deben instalar los paquetes
especificados en el archivo `requirements.txt`. Una forma
fácil de hacerlo en la Raspberry es ejecutando el comando
`make` en la carpeta que contiene los ejemplos. Esto
instalará los paquetes en un ambiente virtual dentro de la
carpeta `env`. Una vez hecho esto, se pueden ejecutar los
ejemplos con el comando `make <nombre_del_ejemplo>`. En
donde `<nombre_del_ejemplo>` es el nombre del archivo sin la
extensión `.py`. Por ejemplo, para ejecutar el primer
programa, se debe escribir el siguiente comando:

    make 1_indentation
