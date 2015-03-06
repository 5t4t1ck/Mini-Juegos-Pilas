# -*- coding: utf-8 -*-
import pilas

#creo la clase actores para que las demas clases donde hayan sprites, hereden esta clase para minimizar codigo
class Actores(pilas.actores.Actor):
    
    def __init__(self,imagen):
        pilas.actores.Actor.__init__(self,imagen)
        
#creo la clase nave, osea el jugador principal
class Nave(Actores):
    
    def iniciar(self):
        self.x=-200
        self.y=-260
        self.escala=0.5
        self.radio_de_colision=35
   
#controles del movimiento de la nave, debe cambiarse...
    def actualizar(self):
        if pilas.escena_actual().control.izquierda:
            self.x -= 7
            self.espejado=True
        if pilas.escena_actual().control.derecha:
            self.x += 7
            self.espejado=False
        if self.x < -380:
            self.x = -380
        if self.x > 380:
            self.x = 380
    
 
class Rectangulo(Actores):
    
    def iniciar(self):
        self.y=250
        
    #fisica... deberia cambiar por colisones o por area...
    def colision(self):
        self.rectangulo=pilas.fisica.Rectangulo(x=self.x, y=250, ancho=self.ancho, alto=self.alto, dinamica=False)
        self.imitar(self.rectangulo)


    def desparramar(self):
        pass
    

class Pelota(pilas.actores.Actor):
    
    #no entiendo bien por que pero, si no ponia el self.dy =2 en el __init___() no me funcionaba la funcion actualizar correctamente...
    def __init__(self,imagen, sonido):
        pilas.actores.Actor.__init__(self,imagen)
        self.dy= 5
        self.dx= 5
        self.sonido= sonido

        
    def actualizar(self):
        
        self.y += self.dy
        if self.arriba > 300 or self.abajo < -300:
            self.dy= -self.dy
        self.x +=self.dx
        if self.izquierda <-450 or self.derecha >450:
            self.dx = -self.dx
        
        #SONIDO DE LA PELOTA AL TOCAR LOS BORDES, ARREGLAR EL DELAY DEL SONIDO
        self.sx = 450
        self.sy = 300
        if self.izquierda <-self.sx or self.derecha > self.sx:
            self.sonido.reproducir()
        if self.arriba > self.sy or self.abajo < -self.sy:        
            self.sonido.reproducir()


    def colision(self):
        self.radio_de_colision=10

        

    
def colisionnave(s1, s2):
    s2.dy= -s2.dy
    s2.dx= -s2.dx
    print "colisiono"
        
        
#no funca por que el rec tiene fisica
def colisionrec(s2,s3):
    s3.eliminar()
    print "colisiono"
        
        
def main():
    pilas.iniciar(900,600, rendimiento=100)
    
    #NAVE
    nave= Nave("cosas/frutas.png")
    nave.iniciar()
    nave.actualizar()
    
    #Rectangulos de arriba
    rectangulo= Rectangulo("cosas/rojo.png")
    rectangulo.iniciar()
    rectangulo.desparramar()
    rectangulo.colision()
    grupo_r=pilas.grupo.Grupo()

    #Pelotica
    tic=pilas.sonidos.cargar("cosas/tic.wav")
    pelotica= Pelota("cosas/pelotica.png",tic)

    #pelotica.pelotica()
    pelotica.actualizar()
    pelotica.colision()
    
    pilas.escena_actual().colisiones.agregar(nave,pelotica,colisionnave)

    pilas.fondos.Color(pilas.colores.negro)
    pilas.ejecutar()
    
main()