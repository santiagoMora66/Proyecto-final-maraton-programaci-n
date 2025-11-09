try:#este try except es para correr el en local o desde el menu
    import Clases.Equipos.Equipo as Equipo
    from Clases.Utilidades.Guardar import Guardar
    from Clases.Utilidades.cargar import Cargar
except ImportError:
    from Equipo import Equipo
    from ..Utilidades.Guardar import Guardar
    from ..Utilidades.cargar import Cargar

class Equipos:
    """Clase para representar todos los equipos"""
    def __init__(self, nombre: str):
        self.equipos = [] #añadir logica para guardar en una base de datos

    def agregar_equipo(self, participante):
        """agrega un equipo a la lista"""
        self.participantes.append(participante)
