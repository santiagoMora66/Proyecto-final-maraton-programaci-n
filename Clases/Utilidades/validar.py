from Clases.Participantes.participantes import Participantes
from Clases.Problemas.Banco_problemas import Banco_problemas

class Validar:
    @staticmethod
    def validar_dificultad(dificultad: str):
        if not dificultad in ["facil", "medio", "dificil"]:
            return False
        return True
    
    @staticmethod
    def validar_titulo(titulo: str):
        if len(titulo) == 0:
            return False
        if type(titulo) != str:
            return False
        return True

    @staticmethod
    def validar_descripcion(descripcion: str):
        if len(descripcion) == 0:
            return False
        if type(descripcion) != str:
            return False
        return True

    @staticmethod
    def validar_id(id_input: str):
        """Valida que el ID sea un número entero positivo"""
        return id_input.isdigit() and int(id_input) > 0
    
    @staticmethod
    def validar_problema_exista(id_problema: int, banco_problemas: Banco_problemas):
        """Valida que el problema exista en el banco de problemas"""
        return banco_problemas.obtener_problema_por_id(id_problema) is not None
    
    @staticmethod
    def validar_nombre(nombre: str):
        if len(nombre) == 0:
            return False
        if type(nombre) != str:
            return False
        return True
    @staticmethod
    def validar_edad(edad: str):
        if not edad.isdigit() or int(edad) <= 0:
            return False
        return True
    
    @staticmethod
    def validar_email(correo: str, Participantes: Participantes):      # cambiar esto
        if "@" not in correo and correo not in Participantes.lista_participantes:
            return False
        return True
        
    
    @staticmethod
    def validar_participante_exista(email: str, participantes: Participantes):
        """Valida que el participante exista en la lista de participantes"""
        return participantes.obtener_participante(email) is not None
    