try:
    from validar import Validar
except ModuleNotFoundError:
    from Clases.Utilidades.validar import Validar
    
class Entradas:
    
    def pedir_problema():
        titulo = input("Ingrese el título del problema: ")
        
        while not Validar.validar_titulo(titulo):
            print("Título inválido. Intente nuevamente.")
            titulo = input("Ingrese el título del problema: ")
        
        descripcion = input("Ingrese la descripción: ")
        while not Validar.validar_descripcion(descripcion):
            print("Descripción inválida. Intente nuevamente.")
            descripcion = input("Ingrese la descripción: ")

        dificultad = input("Ingrese la dificultad (facil/medio/dificil): ")
        while not Validar.validar_dificultad(dificultad):
            print("Dificultad inválida. Intente nuevamente.")
            dificultad = input("Ingrese la dificultad (facil/medio/dificil): ")

        return titulo, descripcion, dificultad
    
        
    def pedir_id():
        """Pide al usuario un ID de problema"""
        id_input = input("Ingrese el ID del problema: ")
        while not Validar.validar_id(id_input):
            print("ID inválido. Intente nuevamente.")
            id_input = input("Ingrese el ID del problema: ")
        return int(id_input)