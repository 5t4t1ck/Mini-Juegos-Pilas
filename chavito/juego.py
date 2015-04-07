# -*- coding:utf-8 -*-
"""
Autor: @Statick_ds, Martin Cueva
Objetivo del Juego: Atrapar la mayor cantidad de pasteles que caen del cielo

"""
import pilasengine

pilas = pilasengine.iniciar()

puntaje = pilas.actores.Puntaje(-280, 200, color = pilas.colores.blanco)

class Chavo(pilasengine.actores.Actor):

    def iniciar(self):

        self.imagen = "data/chavo.png"
        self.y = -144
        self.escala = 0.9

    def actualizar(self):

        if pilas.control.izquierda:
            self.x -= 5
            self.espejado = True

        if self.x <= -280:
                self.x = -280

        if pilas.control.derecha:
            self.x += 5
            self.espejado = False

        if self.x >= 280:
                self.x = 280

class Aceituna(pilasengine.actores.Aceituna):

    def iniciar(self):
        self.imagen = "data/pastel.png"
        self.aprender(pilas.habilidades.PuedeExplotarConHumo)
        self.x = pilas.azar(-200, 200)
        self.y = 290
        self.velocidad = pilas.azar(10, 40)/10.0

    def actualizar(self):
        self.rotacion += 10
        self.y -= self.velocidad

        #Eliminar el objeto cuando sale de la pantalla.
        if self.y < -300:
            self.eliminar()

fondo = pilas.fondos.Galaxia(dy=-5)

enemigos = pilas.actores.Grupo()

def crear_enemigo():
    actor = Aceituna(pilas)
    enemigos.agreagar(actor)

pilas.tareas.siempre(0.5, crear_enemigo)

chavo = Chavo(pilas)

def choque(enemigos, chavo):
	enemigos.eliminar()

pilas.colisiones.agregar(chavo, enemigos, choque)

pilas.avisar(u"enemigas")

pilas.ejecutar()
