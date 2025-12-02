from Clases.maraton.gestiones.gestion_equipos import Equipos

class Gestion_equipos(Equipos):
    def __init__(self):
        super().__init__(Equipos)
        self.equipos = []  # Lista para almacenar los equipos de la maratón
    
    def agregar_equipo(self, equipo):
        """Agrega un equipo a la lista de equipos."""
        self.equipos.append(equipo)
    
    def eliminar_equipo(self,id):
        """Elimina un equipo de la lista de equipos por su ID."""
        self.equipos = [equipo for equipo in self.equipos if equipo.id != id]
    
    def mostrar_equipos(self):
        """Devuelve la lista de equipos."""
        return self.equipos