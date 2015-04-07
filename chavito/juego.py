import pilasengine

pilas = pilasengine.iniciar()

puntaje = pilas.actores.Puntaje(-280, 200, color = pilas.colores.blanco)

class Chavo(pilasengine.actores.Actor):
    
    def iniciar(self):
        
        self.imagen = "chavo.png"
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
                
pato = Chavo(pilas)

pilas.ejecutar()
