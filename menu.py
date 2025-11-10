import os
from Clases.Problemas.Banco_problemas import Banco_problemas
from Clases.Problemas.Problema import Problema, Facil, Medio, Dificil 
from Clases.Utilidades.Entradas import Entradas
from Clases.Utilidades.validar import Validar
from Clases.Participantes.participantes import Participantes

def limpiar_pantalla():
    """Limpia la pantalla"""
    os.system("cls")

def pausar_pantalla():
    """Pausa la pantalla"""
    os.system("pause")
    
def mostrar_menu_principal():
    """Muestra el menú principal del sistema de gestión de maratones y maneja la selección de opciones."""
    
    while True:
        limpiar_pantalla()
        print("_"*100 + "\n")
        print(" SISTEMA DE GESTIÓN DE MARATONES")
        print("_"*100)
        print("1. Gestión de Maratones")
        print("2. Gestión de Problemas") 
        print("3. Gestión de Grupos")
        print("4. Gestión de Participantes")
        print("5. Resultados de Maratones")
        print("6. Salir")
        print("_"*100)

        opcion = input("Seleccione una opción (1-6): ").strip()
        
        match opcion:
            case '1':
                pass #mostrar_gestion_maratones()
            case '2':
                mostrar_gestion_problemas(banco_problemas)
            case '3':
                pass #gestion_grupos()
            case '4':
                mostrar_gestion_participantes(participantes)
            case '5':
                pass #resultados_maratones()
            case '6':
                limpiar_pantalla()
                print("¡Hasta pronto!")
                pausar_pantalla()
                limpiar_pantalla()
                break
            case _:
                limpiar_pantalla()
                print("Opcion invalida. Por favor, seleccione 1-6.")
                pausar_pantalla()
                limpiar_pantalla()

def mostrar_gestion_problemas(banco_problemas : Banco_problemas):
    """Muestra el menú de gestión de problemas."""
    while True:
        limpiar_pantalla()
        print("_"*100 + "\n")
        print(" GESTIÓN DE PROBLEMAS")
        print("_"*100)
        print("1. Agregar problema")
        print("2. Editar problema")
        print("3. Eliminar problema")
        print("4. Ver banco de problemas")
        print("5. Volver al menú principal")
        print("_"*100)

        opcion = input("Seleccione una opción (1-5): ").strip()

        match opcion:
            case '1':
                limpiar_pantalla()
                titulo, descripcion, dificultad = Entradas.pedir_problema()    
                banco_problemas.agregar_problema(titulo, descripcion, dificultad)
                print("Problema agregado exitosamente.")
                pausar_pantalla()
            case '2':
                limpiar_pantalla()
                id_problema = Entradas.pedir_id()
                if Validar.validar_problema_exista(id_problema, banco_problemas):   
                    print("Ingrese los nuevos datos del problema:")
                    nuevo_titulo, nueva_descripcion, nueva_dificultad = Entradas.pedir_problema()
                    banco_problemas.modificar_problema(id_problema, nuevo_titulo, nueva_descripcion, nueva_dificultad)
                    print("Problema modificado exitosamente.")
                else:
                    print("El problema no existe.")
                
                pausar_pantalla()
            case '3':
                limpiar_pantalla()
                id_problema = Entradas.pedir_id()
                if Validar.validar_problema_exista(id_problema, banco_problemas):
                    banco_problemas.eliminar_problema(id_problema)
                    print("Problema eliminado exitosamente.")
                else:
                    print("El problema no existe.")
                pausar_pantalla()
            case '4': 
                limpiar_pantalla()
                banco_problemas.listar_problema()
                pausar_pantalla()
            case '5':
                limpiar_pantalla()
                break
            case _:
                limpiar_pantalla()
                print("Opcion invalida. Por favor, seleccione 1-5.")
                pausar_pantalla()
                limpiar_pantalla()

def mostrar_gestion_participantes(participantes : Participantes):
    """Muestra el menú de gestión de participantes."""
    while True:
        limpiar_pantalla()
        print("_"*100 + "\n")
        print(" GESTIÓN DE PARTICIPANTES")
        print("_"*100)
        print("1. Agregar participante")
        print("2. Editar participante")
        print("3. Eliminar participante")
        print("4. Ver lista de participantes")
        print("5. Volver al menú principal")
        print("_"*100)

        opcion = input("Seleccione una opción (1-5): ").strip()

        match opcion:
            case '1':
                limpiar_pantalla()
                nombre, edad, email = Entradas.pedir_datos_participante(participantes)
                participantes.agregar_participante(nombre, edad, email)
                print("Participante agregado exitosamente.")
                pausar_pantalla()
            case '2':
                limpiar_pantalla()
                id = Entradas.pedir_id_participante(participantes)
                if id:
                    nombre, edad, email = Entradas.pedir_cambio_datos_participante(participantes)
                    if nombre is None and edad is None and email is None:
                        print("no se ha editado nada")
                    else:
                        participantes.editar_participante(id, nombre, edad, email )
                        print("participante editado correctamente")
                else:
                    print("no se encontro al participante")
                pausar_pantalla()          
            case '3':
                limpiar_pantalla()
                id = Entradas.pedir_id_participante(participantes)
                if id:
                    participantes.eliminar_participante(id)
                    print("participante eliminado correctamente")
                else:
                    print("no se encontro al participante")
                pausar_pantalla()
            case '4':
                limpiar_pantalla()
                participantes.listar_participantes()
                pausar_pantalla()
            case '5':
                limpiar_pantalla()
                break
            case _:
                limpiar_pantalla()
                print("Opcion invalida. Por favor, seleccione 1-5.")
                pausar_pantalla()
                limpiar_pantalla()


if __name__ == "__main__":
    banco_problemas = Banco_problemas()
    participantes = Participantes()
    mostrar_menu_principal()