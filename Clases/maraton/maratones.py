
class Maratones:
    def __init__(self):
        self.maratones = []  # Lista para almacenar las maratones

    def agregar_maraton(self, maraton):
        self.maratones.append(maraton)

    def obtener_maratones(self):
        return self.maratones