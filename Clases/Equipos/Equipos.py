try:
    from ..Utilidades.Gestor_entidades_base import Gestor_entidades_base
    from ..Utilidades.Guardar import Guardar
    from ..Utilidades.cargar import Cargar
    from Equipo import Equipo
except ImportError:
    from Clases.Utilidades.Gestor_entidades_base import Gestor_entidades_base
    from Clases.Utilidades.Guardar import Guardar
    from Clases.Utilidades.cargar import Cargar
    from Clases.Equipos.Equipo import Equipo
    
class Equipos(Gestor_entidades_base):
    """Clase para representar todos los equipos"""
    def __init__(self):
        super().__init__()
        self.lista_equipos = Cargar.cargar_equipos()

    def crear_equipo(self, nombre_equipo: str):
        """agrega un equipo a la lista"""
        equipo = Equipo(nombre_equipo)    
        self.agregar(equipo)

    def eliminar_equipo(self, id):
        """elimina un equipo de la lista"""
        if not self.obtener_equipo_por_id(id):
            print(f"No se encontró ningún equipo con ID {id}.")
            return False
        self.eliminar(id)


    def listar_equipos(self):
        self.listar()
    
    def editar_equipo(self, id_equipo, nuevo_nombre=None, participante_agregar=None, participante_eliminar=None):
        """Edita un equipo - maneja nombre, agregar y eliminar participantes"""
        equipo = self.obtener_equipo_por_id(id_equipo)
        if not equipo:
            return False
        
        if nuevo_nombre:
            equipo.nombre_equipo = nuevo_nombre
        
        if participante_agregar:
            equipo.agregar_participante(participante_agregar)
        
        if participante_eliminar:
            equipo.eliminar_participante(participante_eliminar)
        
        self._guardar()
        return True
        
    def obtener_equipo_por_id(self, id_equipo: int):
        """Obtiene un problema del banco de problemas por su ID"""
        return self.obtener_por_id(id_equipo)
    
    
    def _guardar(self):
        Guardar.Guardar_equipos(self.lista_equipos)
        
    def _obtener_lista(self):
        return self.lista_equipos
    
    def _obtener_id_entidad(self,equipo):
        return equipo.id

    def _mostrar_entidad(self, equipo):            
        participantes_str = ', '.join([str(p) for p in equipo.participantes]) if equipo.participantes else 'Sin participantes'
        
        print(f"ID: {equipo.id} | Nombre equipo: {equipo.nombre_equipo} | Participantes: {participantes_str}")       

    def listar(self):
        """Lista todos los equipos"""
        lista = self._obtener_lista()
        if not lista:
            print(f"No hay equipos registrados.")
            return None
        for entidad in lista:
            self._mostrar_entidad(entidad)
        
        
        
