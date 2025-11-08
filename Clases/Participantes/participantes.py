try:
    from Clases.Participantes.participante import Participante
except ModuleNotFoundError:
    from participante import Participante
    
class Participantes:
    def __init__(self):
        self.lista_participantes = []

    def agregar_participante(self, nombre: str, edad: int, email: str):
        participante = Participante(nombre, edad, email)
        self.lista_participantes.append(participante)

    def listar_participantes(self):
        if not self.lista_participantes:
            print("No hay participantes registrados.")
            return
        for p in self.lista_participantes:
            print(f"Nombre: {p.nombre}, Edad: {p.edad}, Email: {p.email}")

    def eliminar_participante(self, correo_participante: int):
        if 0 <= correo_participante < len(self.lista_participantes):
            Participante = self.obtener_participante(correo_participante)
            del self.lista_participantes[Participante]
        else:
            return False
        
    def obtener_participante(self, correo_electronico: str):
        for p in self.lista_participantes:
            if p.correo == correo_electronico:
                return p
        print("Participante no encontrado.")
        return None
