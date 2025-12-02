import pickle

class Cargar:
    @staticmethod
    def cargar_banco_problemas():
        """Carga todos los problemas del banco desde un archivo de texto."""
        ruta = "datos/banco_problemas.pkl"
        try:
            with open(ruta, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []

    @staticmethod
    def cargar_id_problema_contador():
        """Carga el contador de IDs de problemas desde un archivo."""
        ruta = "datos/id_problema_counter.pkl"
        try:
            with open(ruta, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return 1  # Valor por defecto si no se encuentra el archivo

    @staticmethod
    def cargar_id_participante_contador():
        """carga el contador de IDs de equipos desde un archivo"""
        ruta = "datos/id_participantes.pkl"
        try:
            with open(ruta, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return 1   
             
    @staticmethod
    def cargar_participantes():
        """carga la lista de participantes"""
        ruta = "datos/participantes.pkl"
        try:
            with open(ruta, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []
        
    @staticmethod
    def cargar_id_equipo_contador():
        """Carga el contador de IDs de equipos desde un archivo."""
        ruta = "datos/id_equipo_contador"
        try:  
            with open(ruta, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return 1  # Valor por defecto si no se encuentra el archivo

    @staticmethod
    def cargar_equipos():
        """carga la lista de participantes"""
        ruta = "datos/equipos.pkl"
        try:
            with open(ruta, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []
    
    @staticmethod
    def cargar_id_maraton_contador():
        """Carga el contador de IDs de maratones desde un archivo."""
        ruta = "datos/maraton/id_maraton_contador.pkl"
        try:
            with open(ruta, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return 1  # Valor por defecto si no se encuentra el archivo
