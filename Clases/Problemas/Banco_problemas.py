try: #arreglar este 
    from ..Utilidades.Guardar import Guardar
    from ..Utilidades.cargar import Cargar
    from .Problema import Problema, Facil, Medio, Dificil 
except ImportError:    
    from Clases.Utilidades.Guardar import Guardar
    from Clases.Utilidades.cargar import Cargar
    from Clases.Problemas.Problema import Problema, Facil, Medio, Dificil


class Banco_problemas():
    """clase que representa el Banco de problemas totales"""
    def __init__(self):
        self.problemas = Cargar.cargar_banco_problemas()    
    
    def agregar_problema(self, titulo: str, descripcion: str, dificultad: str):
        """Agrega problema creándolo según dificultad"""
        if dificultad == "facil":
            problema = Facil(titulo, descripcion)
        elif dificultad == "medio":
            problema = Medio(titulo, descripcion)
        elif dificultad == "dificil":
            problema = Dificil(titulo, descripcion)
            
        self.problemas.append(problema)
        Guardar.guardar_banco_problemas(self.problemas)

    def eliminar_problema(self, id_problema: int):
        """Elimina un problema del banco de problemas"""
        problema = self.obtener_problema_por_id(id_problema)
        if problema:
            self.problemas.remove(problema)
            Guardar.guardar_banco_problemas(self.problemas)
        else:
            raise ValueError("Índice de problema inválido.")

    def modificar_problema(self, id_problema, nuevo_titulo, nueva_descripcion, nueva_dificultad):
        
        """Modifica un problema en el banco de problemas"""
        problema = self.obtener_problema_por_id(id_problema)
        if problema:
            problema.titulo = nuevo_titulo
            problema.descripcion = nueva_descripcion
            problema.dificultad = nueva_dificultad
            Guardar.guardar_banco_problemas(self.problemas)
        else:
            raise ValueError("Índice de problema inválido.")
        
    def obtener_problema_por_id(self, id_problema: int):
        """Obtiene un problema del banco de problemas por su ID"""
        for problema in self.problemas:
            if problema.id_problema == id_problema:
                return problema
        return None

    def listar_problema(self):
        """Lista todos los problemas en el banco de problemas"""
        if not self.problemas:
            print("No hay problemas en el banco de problemas.")
            return
        
        for problema in self.problemas:
            if isinstance(problema, Facil):
                print(f"ID: {problema.id_problema} | Tipo: Fácil | Título: {problema.titulo} | Descripción: {problema.descripcion} | Puntos: {problema.puntos}")
            elif isinstance(problema, Medio):
                print(f"ID: {problema.id_problema} | Tipo: Medio | Título: {problema.titulo} | Descripción: {problema.descripcion} | Puntos: {problema.puntos}")
            elif isinstance(problema, Dificil):
                print(f"ID: {problema.id_problema} | Tipo: Difícil | Título: {problema.titulo} | Descripción: {problema.descripcion} | Puntos: {problema.puntos}")