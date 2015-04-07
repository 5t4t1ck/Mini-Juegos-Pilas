#!/usr/bin/env python
#!-*- coding:utf-8 -*-
'''
Create by @Statick_ds
Nombre: Asteroide
Objetivo: Crear una nave espacial que ataque 
rocas espaciales al momento de disparar con la
barra espaciadora, destruir las rocas con las
que tengan contacto dichos disparos.
'''
import pilasengine

pilas = pilasengine.iniciar()
nave = pilas.actores.Nave()
asteroides = pilas.actores.Piedra() * 10
nave.x = 100
nave.y = 100
nave.definir_enemigos(asteroides)

pilas.fondos.Espacio()
pilas.ejecutar()
