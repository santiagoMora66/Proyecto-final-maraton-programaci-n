try:
    from ..Utilidades.Gestor_entidades_base import Gestor_entidades_base
    from ..Utilidades.Guardar import Guardar
    from ..Utilidades.cargar import Cargar
    from .Problema import Problema, Facil, Medio, Dificil
except ImportError:
    from Clases.Utilidades.Gestor_entidades_base import Gestor_entidades_base
    from Clases.Utilidades.Guardar import Guardar
    from Clases.Utilidades.cargar import Cargar
    from Clases.Problemas.Problema import Problema, Facil, Medio, Dificil


class Banco_problemas(Gestor_entidades_base):
    """clase que representa el Banco de problemas totales heredando la clase base """ 
    def __init__(self):
        super().__init__()
        self.banco_problemas = Cargar.cargar_banco_problemas()
    
    def agregar_problema(self, titulo: str, descripcion: str, dificultad: str):
        """Agrega problema creándolo según dificultad"""
        if dificultad == "facil":
            problema = Facil(titulo, descripcion)
        elif dificultad == "medio":
            problema = Medio(titulo, descripcion)
        elif dificultad == "dificil":
            problema = Dificil(titulo, descripcion)        
        self.agregar(problema)

    def eliminar_problema(self, id_problema: int):
        """Elimina un problema del banco de problemas"""
        self.eliminar(id_problema)
    
    def modificar_problema(self, id_problema, nuevo_titulo, nueva_descripcion, nueva_dificultad):  
        """Modifica un problema en el banco de problemas"""
        problema = self.obtener_por_id(id_problema)
        if problema:
            problema.titulo = nuevo_titulo
            problema.descripcion = nueva_descripcion
            problema.dificultad = nueva_dificultad
            self._guardar()
               
    def obtener_problema_por_id(self, id_problema: int):
        """Obtiene un problema del banco de problemas por su ID"""
        return self.obtener_por_id(id_problema)

    def listar_problema(self):
        """Lista todos los problemas en el banco de problemas"""
        self.listar()

    def _guardar(self):
        Guardar.guardar_banco_problemas(self.banco_problemas)
    
    def _obtener_lista(self):
        """Cada clase hija devuelve su lista específica"""
        return self.banco_problemas
        
    def _obtener_id_entidad(self,problema):
        return problema.id_problema

    def _mostrar_entidad(self, problema):
        """Muestra un problema de manera específica según su dificultad"""
        if isinstance(problema, Facil):
            tipo = "facil"
        elif isinstance(problema, Medio):
            tipo = "medio"
        elif isinstance(problema, Dificil):
            tipo = "dificil"

        print(f"ID: {problema.id_problema} | Tipo: {tipo} | Título: {problema.titulo} | Descripción: {problema.descripcion} | Puntos: {problema.puntos}")
                
            