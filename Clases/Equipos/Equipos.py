try:
    import Clases.Equipos.Equipos as Equipos
    from Clases.Utilidades.Guardar import Guardar
    from Clases.Utilidades.cargar import Cargar
except ImportError:
    from Equipos import Equipos
    from ..Utilidades.Guardar import Guardar
    from ..Utilidades.cargar import Cargar

class Equipos:
    """Clase para representar un equipo de trabajo."""
    def __init__(self, nombre: str):
        self.nombre_equipo = nombre
        self.participantes = []
        self.id_equipo = Cargar.cargar_id_equipo_counter('id_equipo_counter.pkl')
        Guardar.guardar_id_equipo_counter(self.id_equipo, 'id_equipo_counter.pkl')

    def agregar_participante(self, participante):
        self.participantes.append(participante)
