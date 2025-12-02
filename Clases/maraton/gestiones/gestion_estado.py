class Gestion_estado():
    def __init__(self):
        self.estado = "inactiva"  # Estado inicial de la maratón
    
    def cambiar_estado(self, nuevo_estado):
        """Cambia el estado de la maratón."""
        if nuevo_estado in ["activa", "inactiva", "finalizada"]:
            self.estado = nuevo_estado
        else:
            raise ValueError("Estado no válido. Los estados permitidos son: 'activa', 'inactiva', 'finalizada'.")
