import pilasengine

pilas = pilasengine.iniciar()

grilla = pilas.imagenes.cargar_grilla ("data/protagonista.png",6)

class Vampiro(pilasengine.actores.Actor):
    pass

    def iniciar(self):
        self.imagen = grilla

vampiro = Vampiro(pilas)

pilas.ejecutar()
