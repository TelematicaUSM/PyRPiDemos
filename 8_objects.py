#! /usr/bin/env python3
# -*- coding: UTF-8 -*-


class Perro(object):
    hambre = 2

    def comer(self):
        if self.hambre > 0:
            print('Nom nom nom nom!')
            self.hambre = self.hambre - 1
        else:
            print('No gracias, ya estoy satisfecho!')

    def caminar(self):
        print(':D')
        self.hambre = self.hambre + 1


toby = Perro()
pluto = Perro()

toby.caminar()
pluto.comer()
pluto.comer()
pluto.comer()
toby.comer()
