try:
    from Clases.maraton.gestiones.gestion_identificacion import Gestion_identificacion
    from Clases.maraton.gestiones.gestion_configuracion import Gestion_configuracion
    from Clases.maraton.gestiones.gestion_estado import Gestion_estado
    from Clases.maraton.gestiones.gestion_equipos import Gestion_equipos
    from Clases.maraton.gestiones.gestion_problemas import Gestion_problemas
    from Clases.Utilidades.cargar import Cargar
    from Clases.Utilidades.Guardar import Guardar
    

except ImportError:
    from gestiones.gestion_identificacion import Gestion_identificacion
    from gestiones.gestion_configuracion import Gestion_configuracion
    from gestiones.gestion_estado import Gestion_estado
    from ..Utilidades.cargar import Cargar
    from ..Utilidades.Guardar import Guardar    

class Maraton:
    id_maraton_contador = Cargar.cargar_id_maraton_contador()
    def __init__(self, nombre,descripcion, dificultad,banco_problemas, equipos):
        identificacion = Gestion_identificacion(Maraton.id_maraton_contador, nombre, descripcion)
        Maraton.id_maraton_contador += 1
        Guardar.guardar_id_maraton_contador(Maraton.id_maraton_contador)
        configuracion = Gestion_configuracion(dificultad)
        estado = Gestion_estado()
        equipos = Gestion_equipos(equipos)
        problemas = Gestion_problemas(banco_problemas)
        #estadisticas = Estadisticas()