import pickle

class Guardar:
    
    @staticmethod
    def guardar_banco_problemas(banco_problemas, archivo):
        """Guarda todos los problemas del banco en un archivo de texto."""
        with open(archivo, 'wb') as f:
            pickle.dump(banco_problemas, f)

    @staticmethod
    def guardar_id_problema_counter(counter, archivo):
        """Guarda el contador de IDs de problemas en un archivo."""
        with open(archivo, 'wb') as f:
            pickle.dump(counter, f)