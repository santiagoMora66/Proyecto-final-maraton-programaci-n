try: #try creado para que se defina una ruta local o global
    from Clases.Participantes.participante import Participante
    from Clases.Utilidades.Guardar import Guardar
    from Clases.Utilidades.cargar import Cargar
    from ..Utilidades.Gestor_entidades_base import Gestor_entidades_base

except ModuleNotFoundError:
    from participante import Participante
    
class Participantes(Gestor_entidades_base):
    """clase representada para almacenar todos los participantes y realizar interracciones"""
    
    def __init__(self):
        super().__init__()
        self.lista_participantes = Cargar.cargar_participantes()

    def agregar_participante(self, nombre: str, edad: int, email: str):
        """metodo que permite agregar participantes a l a lista"""
        participante = Participante(nombre, edad, email)
        self.agregar(participante)

    def eliminar_participante(self, id: int):
        """metodo para eliminar todos los participantes"""
        self.eliminar(id)
             
    def listar_participantes(self):
        """metodo que muestra todos los participantes de la lista"""
        self.listar()

    def editar_participante(self, id:str, nombre: str, edad: str, email:str):
        """metodo para modificar los datos de un participantes"""
        Participante = self.obtener_participante(id)
        if Participante:
            if nombre is not None:
                Participante.nombre = nombre
            if edad is not None:
                Participante.edad = edad
            if email is not None:
                Participante.email = email
            self._guardar()

      
    def obtener_participante(self, id: int):
        """metodo par obtener y devolver un participante en especificio """
        for p in self.lista_participantes:
            if p.id == id:
                return p
        print("Participante no encontrado.")
        return None

    def _guardar(self):
        Guardar.Guardar_participantes(self.lista_participantes)

    def _obtener_lista(self):
        """Cada clase hija devuelve su lista específica"""
        return self.lista_participantes

    def _obtener_id_entidad(self,participante):
        return participante.id

    def _mostrar_entidad(self, participante: Participante):
        if participante.disponible:
            disponible_str = "Sí"
        else:
            disponible_str = "No"
        print(f"ID: {participante.id} | Nombre: {participante.nombre} | Edad: {participante.edad} | Email: {participante.email} | Disponible: {disponible_str}")

