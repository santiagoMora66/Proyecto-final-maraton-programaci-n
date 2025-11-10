from ..Utilidades.Guardar import Guardar
from ..Utilidades.cargar import Cargar
from abc import ABC, abstractmethod

class Problema():
    """Clase base para representar un problema de programación."""
    id_problema_counter = Cargar.cargar_id_problema_contador()

    def __init__(self, titulo, descripcion):
        self.id_problema = Problema.id_problema_counter
        Problema.id_problema_counter += 1
        Guardar.guardar_id_problema_contador(Problema.id_problema_counter)
        self.titulo = titulo
        self.descripcion = descripcion
        self.dificultad = self.obtener_dificultad()
        self.puntos = self.obtener_puntos()
        self.resuelto = False
        
        @abstractmethod
        def obtener_dificultad(self):
            """cada clase hijo define su dificultad"""
            pass

        @abstractmethod
        def obtener_puntos(self):
            """Cada dificultad define sus puntos"""
            pass

class Facil(Problema):
    """Clase para representar un problema fácil."""
    def __init__(self, titulo, descripcion):
        super().__init__(titulo, descripcion)

    def obtener_dificultad(self):
        return "facil"

    @abstractmethod
    def obtener_puntos(self):
        return 2        

class Medio(Problema):
    """Clase para representar un problema de dificultad media."""
    def __init__(self, titulo, descripcion):
        super().__init__(titulo, descripcion)

    def obtener_dificultad(self):
        return "medio"

    @abstractmethod
    def obtener_puntos(self):
        return 5

class Dificil(Problema):
    """Clase para representar un problema difícil."""
    def __init__(self, titulo, descripcion):
        super().__init__(titulo, descripcion)

    def obtener_dificultad(self):
        return "dificil"

    @abstractmethod
    def obtener_puntos(self):
        return 10


