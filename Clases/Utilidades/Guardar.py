import pickle

class Guardar:
    
    @staticmethod
    def guardar_banco_problemas(banco_problemas):
        """Guarda todos los problemas del banco en un archivo de texto."""
        ruta = "datos/banco_problemas.pkl"
        with open(ruta, 'wb') as f:
            pickle.dump(banco_problemas, f)

    @staticmethod
    def guardar_id_problema_contador(contador):
        """Guarda el contador de IDs de problemas en un archivo."""
        ruta = "datos/id_problema_counter.pkl"
        with open(ruta, 'wb') as f:
            pickle.dump(contador, f)
    
    @staticmethod
    def guardar_id_participante_contador(counter):
        """Guarda el contador de IDs de cada participante"""
        ruta = "datos/id_participantes.pkl"
        with open(ruta, "wb") as f:
            pickle.dump(counter, f)
    
    @staticmethod
    def Guardar_participantes(Participantes):
        """guarda la lista de participantes en un archivo pkl"""
        ruta = "datos/participantes.pkl"
        with open(ruta, "wb") as f:
            pickle.dump(Participantes, f)
        
    
    @staticmethod
    def guardar_id_equipo_counter(counter):
        ruta = "datos/id_equipo_counter"
        """Guarda el contador de IDs de equipos en un archivo."""
        with open(ruta, 'wb') as f:
            pickle.dump(counter, f)

    
    