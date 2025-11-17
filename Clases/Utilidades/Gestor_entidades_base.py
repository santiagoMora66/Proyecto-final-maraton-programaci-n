from abc import ABC, abstractmethod

class Gestor_entidades_base(ABC):
    """Clase base abstracta para gestores de entidades con operaciones CRUD (el modificar lo hace cada clase)"""
    
    def __init__(self):
        pass

    def agregar(self, entidad: list):
        """Agrega una entidad a la lista"""
        lista = self._obtener_lista()  # ← Pide la lista a la clase hija
        lista.append(entidad)
        self._guardar()
                
    def eliminar(self, id_entidad: int):
        """Elimina una entidad por ID"""
        entidad = self.obtener_por_id(id_entidad)
        if entidad:
            lista = self._obtener_lista()
            lista.remove(entidad)
            self._guardar()
        
    def obtener_por_id(self, id_entidad: int) :
        """Obtiene una entidad por su ID"""
        lista = self._obtener_lista()
        for entidad in lista:
            if self._obtener_id_entidad(entidad) == id_entidad:
                return entidad
        return None
    
    def listar(self):
        """Lista todas las entidades"""
        lista = self._obtener_lista()
        if not lista:
            print(f"No hay entidades registradas.")
            return None
        for entidad in lista:
            self._mostrar_entidad(entidad)

    @abstractmethod
    def _guardar(self):
        """cada clase hija guarda de una manera especifica"""
        pass
    
    @abstractmethod
    def _obtener_lista(self):
        """Cada clase hija devuelve su lista específica"""
        pass
    
    @abstractmethod
    def _obtener_id_entidad(self, entidad):
        """cada clase hija obtiene el id de una forma"""
        pass
    
    @abstractmethod
    def _mostrar_entidad(self,entidad):
        """cada clase hija muestra cada entidad de una manera especifica"""
        pass
    
    
    
    