class Gestion_problemas:
    def __init__(self, banco_problemas):
        banco = banco_problemas
        self.problemas_maraton = []
    
    def agregar_problema(self, problema):
        """Agrega un problema a la lista de problemas de la maratón."""
        self.problemas_maraton.append(problema)
    
    def eliminar_problema(self,problema):
        """Elimina un problema de la lista de problemas de la maratón."""
        self.problemas_maraton = [p for p in self.problemas_maraton if p.id != problema.id]
    
    def listar_problemas(self):
        """Devuelve la lista de problemas de la maratón."""
        return self.problemas_maraton

    # Métodos para gestionar problemas en la maratón
    # Por ejemplo: agregar_problema, eliminar_problema, listar_problemas, etc.