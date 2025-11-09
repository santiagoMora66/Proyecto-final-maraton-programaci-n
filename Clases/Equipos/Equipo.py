class Equipo:
    """clase para representar un equipo"""
    def __init__(self, nombre):
        self.id = id #aqui se pondra una logica para guardar el ultimo id 
        self.nombre_equipo = nombre
        self.participantes = []
    