"""
Ejercicio nivel 2: Cupi58: La mejor calle de la ciudad 
Modulo de interacción por consola.

Temas:
* Variables.
* Tipos de datos.
* Expresiones aritméticas.
* Instrucciones básicas y consola.
* Dividir y conquistar: funciones y paso de párametros.
* Especificacion y documentacion.
* Instrucciones condicionales.
* Diccionarios.
@author: Cupi2

"""
import cupi58 as c58

def mostrar_establecimiento(establecimiento: dict) -> None:
    nombre = establecimiento["nombre"]
    hora_apertura = establecimiento["hora_de_apertura"]
    hora_cierre = establecimiento["hora_de_cierre"]
    tipo = establecimiento["tipo"]
    generos = establecimiento["generos_musicales"]
    aforo = establecimiento["aforo"]
    clientes_promedio = establecimiento["clientes_promedio"]
    precio_bebida_mas_cara = establecimiento["precio_bebida_mas_cara"]
    precio_bebida_mas_barata = establecimiento["precio_bebida_mas_barata"]
    dias_apertura = c58.mostrar_dias_apertura_establecimiento(establecimiento)
    cadena_dias = "|L|M|I|J|V|S|D|\n|"
    for dia in dias_apertura:
        if dias_apertura[dia]:
            cadena_dias+="X|"
        else:
            cadena_dias+=" |"

    print("Nombre: " + nombre +
          "\n\nHora de apertura: " + str(hora_apertura) +
          "\n\nHora de cierre: " + str(hora_cierre) +
          "\n\nDías de apertura:\n\n" + cadena_dias +
          "\n\nTipo de establecimiento: " + tipo +
          "\n\nGéneros del establecimiento: " + generos +
          "\n\nAforo del establecimiento: " + str(aforo) +
          "\n\nClientes promedio: " + str(clientes_promedio) +
          "\n\nPrecio bebida más cara: " + "$" + str(precio_bebida_mas_cara) +
          "\n\nPrecio bebida más barata: " +
          "$" + str(precio_bebida_mas_barata)
          )


def ejecutar_buscar_establecimiento_con_mayor_aforo(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Función que ejecuta la opción de buscar el establecimiento con mayor aforo.

    Parámetros
    ----------
    e1 : dict
        Diccionario con la información del primer establecimiento.
    e2 : dict
        Diccionario con la información del segundo establecimiento.
    e3 : dict
        Diccionario con la información del tercer establecimiento.
    e4 : dict
        Diccionario con la información del cuarto establecimiento.

    El programa debe mostrar: "El establecimiento X es el establecimiento con
    mayor aforo con Y personas." En el cual X es el nombre del establecimiento 
    y Y el número de personas.

    """
    #TODO: Completar
    pass

def ejecutar_calcular_horas_totales_apertura_establecimiento(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Función que ejecuta la opción de calcular cuántas horas está
    abierto un establecimiento por semana.

    Parámetros
    ----------
    e1 : dict
        Diccionario con la información del primer establecimiento.
    e2 : dict
        Diccionario con la información del segundo establecimiento.
    e3 : dict
        Diccionario con la información del tercer establecimiento.
    e4 : dict
        Diccionario con la información del cuarto establecimiento.

    El programa debe mostrar: "El establecimiento está abierto X
    horas a la semanas." En el cual X es el número de horas, redondeado a dos decimales. 
    En caso de que no se ingrese un nombre válido de establecimiento debe
    mostrar un mensaje que lo notifique (ver PDF)

    """
    #TODO: Completar
    pass

def ejecutar_mostrar_establecimientos_con_genero_musical(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Función que ejecuta la opción de mostrar cuáles establecimientos
    tienen un género musical.

    Parámetros
    ----------
    e1 : dict
        Diccionario con la información del primer establecimiento.
    e2 : dict
        Diccionario con la información del segundo establecimiento.
    e3 : dict
        Diccionario con la información del tercer establecimiento.
    e4 : dict
        Diccionario con la información del cuarto establecimiento.

    """
    #TODO: Completar
    pass

def ejecutar_calcular_puntaje_establecimiento(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Función que ejecuta la opción de calcular el puntaje de un
    establecimiento de acuerdo con el sistema de puntuación.

    Parámetros
    ----------
    e1 : dict
        Diccionario con la información del primer establecimiento.
    e2 : dict
        Diccionario con la información del segundo establecimiento.
    e3 : dict
        Diccionario con la información del tercer establecimiento.
    e4 : dict
        Diccionario con la información del cuarto establecimiento.

    El programa debe mostrar: "El establecimiento tiene X puntos".
    En el cual X es la cantidad de puntos obtenidos. En caso de que
    no se ingrese un nombre válido de establecimiento debe mostrar
    un mensaje que lo notifique.

    """
    #TODO: Completar
    pass

def ejecutar_contar_establecimientos_segun_tipo(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    """
    Función que ejecuta la opción de contar cuántos establecimientos
    son de un tipo.

    Parámetros
    ----------
    e1 : dict
        Diccionario con la información del primer establecimiento.
    e2 : dict
        Diccionario con la información del segundo establecimiento.
    e3 : dict
        Diccionario con la información del tercer establecimiento.
    e4 : dict
        Diccionario con la información del cuarto establecimiento.

    """
    #TODO: Completar
    pass

def iniciar_aplicacion() -> None:
    establecimiento1 = c58.crear_establecimiento(
        "El simio bribón", 1900, 400, 1111111, "Bar", "Rock, Pop, Varios", 200, 500, 300000, 5000)
    establecimiento2 = c58.crear_establecimiento(
        "El chulo", 1900, 300, 111, "Bar", "Mexicano, Ranchera, Mariachi", 1000, 500, 800000, 10000)
    establecimiento3 = c58.crear_establecimiento(
        "Morenita", 2000, 400, 1111, "Discoteca", "Reggaeton", 800, 500, 500000, 12000)
    establecimiento4 = c58.crear_establecimiento(
        "Desarmando", 1200, 500, 1001111, "Discoteca", "Rock, Reggaeton, Pop, Varios", 2000, 500, 850000, 4000)
    ejecutando = True
    while ejecutando:
        print("\nEstablecimientos de la Cupi58\n" + ("-"*50))
        print("Establecimiento 1\n")
        mostrar_establecimiento(establecimiento1)
        print("-"*50)

        print("Establecimiento 2\n")
        mostrar_establecimiento(establecimiento2)
        print("-"*50)

        print("Establecimiento 3\n")
        mostrar_establecimiento(establecimiento3)
        print("-"*50)

        print("Establecimiento 4\n")
        mostrar_establecimiento(establecimiento4)
        print("-"*50)

        ejecutando = mostrar_menu_aplicacion(
            establecimiento1, establecimiento2, establecimiento3, establecimiento4)

        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")


def mostrar_menu_aplicacion(e1: dict, e2: dict, e3: dict, e4: dict) -> bool:
    print("Menu de opciones")
    print(" 1 - Buscar establecimiento con mayor aforo")
    print(" 2 - Calcular horas totales de apertura en una semana de un establecimiento")
    print(" 3 - Determinar establecimientos con un género musical determinado")
    print(" 4 - Determinar puntaje de un establecimiento")
    print(" 5 - Contar establecimientos según tipo")
    print(" 6 - Salir de la aplicación")

    opcion_elegida = input("Ingrese la opción que desea ejecutar: ").strip()

    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_buscar_establecimiento_con_mayor_aforo(e1, e2, e3, e4)
    elif opcion_elegida == "2":
        ejecutar_calcular_horas_totales_apertura_establecimiento(e1, e2, e3, e4)
    elif opcion_elegida == "3":
        ejecutar_mostrar_establecimientos_con_genero_musical(e1, e2, e3, e4)
    elif opcion_elegida == "4":
        ejecutar_calcular_puntaje_establecimiento(e1, e2, e3, e4)
    elif opcion_elegida == "5":
        ejecutar_contar_establecimientos_segun_tipo(e1, e2, e3, e4)
    elif opcion_elegida == "6":
        continuar_ejecutando = False
    else:
        print("La opción " + opcion_elegida + " no es una opción válida.")

    return continuar_ejecutando


iniciar_aplicacion()
