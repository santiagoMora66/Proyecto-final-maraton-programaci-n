try: #try creado para que se defina una ruta local o global
    from Clases.Participantes.participante import Participante
    from Clases.Utilidades.Guardar import Guardar
    from Clases.Utilidades.cargar import Cargar
except ModuleNotFoundError:
    from participante import Participante
    
class Participantes:
    """clase representada para almacenar todos los participantes y realizar interracciones"""
    
    def __init__(self):
        self.lista_participantes = Cargar.cargar_participantes()

    def agregar_participante(self, nombre: str, edad: int, email: str):
        """metodo que permite agregar participantes a l a lista"""
        participante = Participante(nombre, edad, email)
        self.lista_participantes.append(participante)
        Guardar.Guardar_participantes(self.lista_participantes)
        
    def listar_participantes(self):
        """metodo que muestra todos los participantes de la lista"""
        if not self.lista_participantes:
            print("No hay participantes registrados.")
            return
        for p in self.lista_participantes:
            print(f"ID:{p.id} Nombre: {p.nombre}, Edad: {p.edad}, Email: {p.email}")

    def editar_participante(self, correo_participante: str):
        """metodo para modificar los datos de un participantes"""
        Participante = self.obtener_participante(correo_participante)
        if Participante:   
            Participante.nombre = None
            Participante.edad = None
            Participante.email = None

    def eliminar_participante(self, id: int):
        """metodo para eliminar todos los participantes"""
        Participante = self.obtener_participante(id)
        if Participante:   
            self.lista_participantes.remove(Participante)
        Guardar.Guardar_participantes(self.lista_participantes)
                            
    def obtener_participante(self, id: int):
        """metodo par obtener y devolver un participante en especificio """
        for p in self.lista_participantes:
            if p.id == id:
                return p
        print("Participante no encontrado.")
        return None
