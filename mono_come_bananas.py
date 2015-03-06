# -*- coding: utf-8 -*-

import pilasengine

'''
Create by: @Statick_ds
Nombre: Mono Come Bananas

Objetivo: El objetivo es que el actor mono coma bananas
y al colisionar con las bombas explote

'''
pilas = pilasengine.iniciar()

pilas.fondos.Selva()

mono = pilas.actores.Mono()
mono.x = 100
mono.y = 100 
bananas = pilas.actores.Banana()*30
bombas = pilas.actores.Bomba()*5

def mono_come_banana(mono, banana):
    mono.sonreir()
    banana.eliminar()
	
def bomba_mata_mono(mono, bomba):
    bomba.eliminar()
    mono.gritar()
    mono.eliminar()
	
mono.aprender(pilas.habilidades.Arrastrable)   

pilas.escena_actual().colisiones.agregar(mono, bananas, mono_come_banana)
pilas.escena_actual().colisiones.agregar(mono, bombas, bomba_mata_mono)

pilas.ejecutar()
