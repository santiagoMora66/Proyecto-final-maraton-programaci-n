from ..Utilidades.Guardar import Guardar
from ..Utilidades.cargar import Cargar

class Equipo():
    """clase para representar un equipo"""

    id_equipo_contador = Cargar.cargar_id_equipo_contador()

    def __init__(self, nombre):
        self.id = Equipo.id_equipo_contador
        Equipo.id_equipo_contador += 1
        Guardar.guardar_id_equipo_contador(Equipo.id_equipo_contador)
        self.nombre_equipo = nombre
        self.participantes = []

    def cambiar_nombre(self, nuevo_nombre):
        """Cambia el nombre del equipo."""
        self.nombre_equipo = nuevo_nombre
    
    def agregar_participante(self, participante):
        if len(self.participantes) >= 3:
            print("El equipo ya tiene el número máximo de participantes (3).")
            return False
        
        for p in self.participantes:
            if p.id == participante.id:
                print(f"El participante {participante.nombre} ya está en el equipo.")
                return False
        if not participante.disponible:
            print(f"El participante {participante.nombre} no está disponible para unirse al equipo.")
            return False
        else:
            participante.disponible = False
            self.participantes.append(participante)
            print(f"Participante {participante.nombre} agregado al equipo.")
            return True
            
    def eliminar_participante(self, participante):
        if self.participantes == []:
            print("El equipo no tiene participantes para eliminar.")
            return False
        if participante not in self.participantes:
            print(f"El participante {participante.nombre} no está en el equipo.")
            return False
        else:
            participante.disponible = True
            self.participantes.remove(participante)
            print(f"Participante {participante.nombre} eliminado del equipo.")
            return True
        
    def mostrar_participantes(self):
        if not self.participantes:
            print("No hay participantes en el equipo")
            return
        
        texto = ""
        for participante in self.participantes:
            if texto == "":  # Si es el primer participante
                texto = participante.nombre
            else:  # Si ya hay participantes agregados
                texto = texto + ", " + participante.nombre
            
        print(texto)        