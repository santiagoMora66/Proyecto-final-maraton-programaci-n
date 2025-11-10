try:
    from ..Participantes.participantes import Participantes
except ModuleNotFoundError:
    from Clases.Participantes.participantes import Participantes


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

    def pedir_datos_participante(participantes: Participantes):
        nombre = input("Ingrese el nombre del participante: ")

        while not Validar.validar_nombre(nombre):
                print("Nombre inválido. Intente nuevamente.")
                nombre = input("Ingrese el nombre del participante: ")
        
        edad = input("Ingrese la edad del participante: ")
        
        while not Validar.validar_edad(edad):
            print("Edad inválida. Intente nuevamente.")
            edad = input("Ingrese la edad del participante: ")

        email = input("Ingrese el email del participante: ")
       
        while not Validar.validar_email(email, participantes):
            print("Email inválido. Intente nuevamente.")
            email = input("Ingrese el email del participante: ")    
            
        return nombre, int(edad), email

    def pedir_cambio_datos_participante(participantes: Participantes):
        print("presiona enter si quieres mantener los datos originales")
        nombre = input("Ingrese el nombre del participante: ")

        if nombre != "":
            while not Validar.validar_nombre(nombre):
                print("Nombre inválido. Intente nuevamente.")
                nombre = input("Ingrese el nombre del participante: ")
        else:
            nombre = None
        
        edad = input("Ingrese la edad del participante: ")
        
        if edad != "":
            while not Validar.validar_edad(edad):
                print("Edad inválida. Intente nuevamente.")
                edad = input("Ingrese la edad del participante: ")
        else:
            edad = None
            
        email = input("Ingrese el email del participante: ")
       
        if email != "":
            while not Validar.validar_email(email, participantes):
                print("Email inválido. Intente nuevamente.")
                email = input("Ingrese el email del participante: ")    
        else:
            email = None
            
        return nombre, int(edad), email

    def pedir_correo_participante(participantes: Participantes):
        email = input("Ingrese el email del participante: ")
        if Validar.email_ya_existe(email, participantes):
            return email
        else:
            return False
    
    def pedir_id_participante(participantes : Participantes):
        id = int(input("Ingresa el Id del participante: "))            
        if Validar.id_existe(id, participantes):
            return int(id)
        else:
            return False
            
    