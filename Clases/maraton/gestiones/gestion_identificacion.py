class Gestion_identificacion:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    
    def cambiar_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion
    
    def mostrar_id(self):
        return self.id