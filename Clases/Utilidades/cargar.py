import pickle

class Cargar:
    @staticmethod
    def cargar_banco_problemas(archivo):
        """Carga todos los problemas del banco desde un archivo de texto."""
        try:
            with open(archivo, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []

    @staticmethod
    def cargar_id_problema_counter(archivo):
        """Carga el contador de IDs de problemas desde un archivo."""
        try:
            with open(archivo, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return 1  # Valor por defecto si no se encuentra el archivo

    @staticmethod
    def cargar_id_equipo_counter(archivo):
        """Carga el contador de IDs de equipos desde un archivo."""
        try:
            with open(archivo, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return 1  # Valor por defecto si no se encuentra el archivo