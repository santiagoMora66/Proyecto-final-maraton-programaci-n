from ..Utilidades.Guardar import Guardar
from ..Utilidades.cargar import Cargar

class Participante:
    """clase creada para representar participantes"""
    
    id_participantes_contador = Cargar.cargar_id_participante_contador()

    def __init__(self, nombre: str, edad: int, email: str):
        self.id = Participante.id_participantes_contador
        Participante.id_participantes_contador += 1
        Guardar.guardar_id_participante_contador(Participante.id_participantes_contador)
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.disponible = True

    def __str__(self):
        return self.nombre
