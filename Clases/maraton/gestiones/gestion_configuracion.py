class Gestion_configuracion:
    def __init__(self, dificultad):
        self.dificultad = dificultad

    def cambiar_dificultad(self, nueva_dificultad):
        if nueva_dificultad in ["fácil", "media", "difícil"]:
            self.dificultad = nueva_dificultad
        else:
            print("Dificultad no válida. Las opciones son: 'fácil', 'media', 'difícil'.")
    
    def mostrar_dificultad(self):
        return self.dificultad