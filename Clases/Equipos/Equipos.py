try:
    from ..Utilidades.Gestor_entidades_base import Gestor_entidades_base
    from ..Utilidades.Guardar import Guardar
    from ..Utilidades.cargar import Cargar
except ImportError:
    from Clases.Utilidades.Gestor_entidades_base import Gestor_entidades_base
    from Clases.Utilidades.Guardar import Guardar
    from Clases.Utilidades.cargar import Cargar

class Equipos(Gestor_entidades_base):
    """Clase para representar todos los equipos"""
    def __init__(self, nombre: str):
        super().__init__()
        self.equipos = [] #añadir logica para guardar en una base de datos

    def agregar_equipo(self, participante):
        """agrega un equipo a la lista"""
        self.agregar(participante)
