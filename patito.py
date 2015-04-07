import pilasengine

pilas = pilasengine.iniciar()

puntaje = pilas.actores.Puntaje(-280, 200, color = pilas.colores.blanco)

class Pato(pilasengine.actores.Actor):
    
    def iniciar(self):
        
        self.imagen = "patito.png"
        self.y = -180
           
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
                
class AceitunaEnemiga(pilasengine.actores.Aceituna):

    def iniciar(self):
        self.imagen = "aceituna.png"
        self.aprender( pilas.habilidades.PuedeExplotarConHumo )
        self.x = pilas.azar(-200, 200)
        self.y = 290
        self.velocidad = pilas.azar(10, 40) / 10.0
            
    def actualizar(self):
        
        if self.y <= 300:
            self.eliminar()

pato = Pato(pilas)

aceituna = AceitunaEnemiga(pilas)
pilas.ejecutar()