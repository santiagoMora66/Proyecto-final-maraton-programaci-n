try:
    from Clases.Participante.participante import Participante
except ModuleNotFoundError:
    from participante import Participante
    
class Participantes:
    def __init__(self):
        self.lista_participantes = []

    def agregar_participante(self, nombre: str, edad: int, email: str):
        participante = Participante(nombre, edad, email)
        self.lista_participantes.append(participante)

    def listar_participantes(self):
        return self.lista_participantes