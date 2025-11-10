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

    @staticmethod
    def pedir_datos_participante(participantes: Participantes):
        nombre = Entradas.pedir_nombre()
        edad = Entradas.pedir_edad()
        correo = Entradas.pedir_correo(participantes)
        return nombre, int(edad), correo

    @staticmethod
    def pedir_correo(participantes : Participantes):
        correo = input("Ingrese el correo del participante: ")
       
        while not Validar.validar_email(correo, participantes):
            print("Email inválido. Intente nuevamente.")
            correo = input("Ingrese el email del participante: ")
        return correo

    @staticmethod
    def pedir_nombre():
        nombre = input("Ingrese el nombre del participante: ")
        while not Validar.validar_nombre(nombre):
                print("Nombre inválido. Intente nuevamente.")
                nombre = input("Ingrese el nombre del participante: ")
        return nombre

    @staticmethod
    def pedir_edad():
        edad = input("Ingrese la edad del participante: ")
        
        while not Validar.validar_edad(edad):
            print("Edad inválida. Intente nuevamente.")
            edad = input("Ingrese la edad del participante: ")
        return edad
    
    
            
    @staticmethod
    def pedir_cambio_datos_participante(participantes: Participantes):
        print("Presiona enter si quieres mantener los datos originales")
        
        nombre = Entradas.pedir_nombre_opcional()
        edad = Entradas.pedir_edad_opcional()
        email = Entradas.pedir_email_opcional(participantes)
            
        return nombre, edad, email

    @staticmethod
    def pedir_nombre_opcional():
        nombre = input("Ingrese el nombre del participante: ")
        if nombre != "":
            while not Validar.validar_nombre(nombre):
                print("Nombre inválido. Intente nuevamente.")
                nombre = input("Ingrese el nombre del participante: ")
        else:
            nombre = None
        return nombre

    @staticmethod
    def pedir_edad_opcional():
        edad = input("Ingrese la edad del participante: ")
        if edad != "":
            while not Validar.validar_edad(edad):
                print("Edad inválida. Intente nuevamente.")
                edad = input("Ingrese la edad del participante: ")
            edad = int(edad)
        else:
            edad = None
        return edad

    @staticmethod
    def pedir_email_opcional(participantes):
        while True:
                email = input("Ingrese el email del participante: ")
                
                if email == "":
                    return None  
                
                if Validar.validar_email(email, participantes):
                    return email  
                
                print("Email inválido. Intente nuevamente.")
    
    def pedir_correo_participante(participantes: Participantes):
        email = input("Ingrese el email del participante: ")
        if Validar.email_ya_existe(email, participantes):
            return email
        else:
            return False
    
    def pedir_id_participante(participantes : Participantes):
        """pide el id del participante"""
        id = int(input("Ingresa el Id del participante: "))            
        if Validar.id_existe(id, participantes):
            return int(id)
        else:
            return None
            
    