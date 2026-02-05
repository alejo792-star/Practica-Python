# -*- coding: utf-8 -*-
"""
CupiTikTok:

@author: Cupi2
"""

import cupi_tiktok as tk


def mostrar_creador(creador: dict) -> None:
    """
    Muestra los datos de un creador de contenido en la consola.

    Parámetros:
    creador (dict): Los datos del creador de contenido.

    """
    nombre = creador["nombre"]
    pais = creador["pais"]
    categorias = creador["categorias"]
    likes = creador["likes"]
    vistas = creador["vistas"]
    seguidores = creador["seguidores"]
    fecha_ultima_publicacion = creador["fecha_ultima_publicacion"]
    print(
        "Nombre: {}\nPaís: {}\nCategoría: {}\nLikes: {}\nVistas: {}\nSeguidores: {}\nFecha de última publicación: {}".format(
            nombre,
            pais,
            categorias,
            likes,
            vistas,
            seguidores,
            fecha_ultima_publicacion,
        )
    )


def ejecutar_buscar_creador_por_nombre(c1: dict, c2: dict, c3: dict, c4: dict) -> None:
    """
    Función que ejecuta la opción de buscar un creador de contenido por nombre.

    Parámetros:
    c1 (dict): Diccionario con los datos del creador 1.
    c2 (dict): Diccionario con los datos del creador 2.
    c3 (dict): Diccionario con los datos del creador 3.
    c4 (dict): Diccionario con los datos del creador 4.

    Si el creador no existe, se debe mostrar el siguiente mensaje:
    "No se encontró un creador con el nombre ingresado."

    En cualquier otro caso, se debe mostrar los datos del creador.
    """

    nom = input("Escriba el nombre del creador de contenido: ")

    result = tk.buscar_creador_por_nombre(nom,c1,c2,c3,c4)

    if result == None:
        print("No se encontró un creador con el nombre ingresado.")
    else:
        mostrar_creador(result)

    


def ejecutar_filtrar_creadores_por_categoria(c1: dict, c2: dict, c3: dict, c4: dict) -> None:
    """
    Función que ejecuta la opción de buscar creadores de contenido por categoría.

    Parámetros:
    c1 (dict): Diccionario con los datos del creador 1.
    c2 (dict): Diccionario con los datos del creador 2.
    c3 (dict): Diccionario con los datos del creador 3.
    c4 (dict): Diccionario con los datos del creador 4.

    Si no se encuentran creadores con la categoría ingresada, se debe mostrar
    el siguiente mensaje:
    "No se encontraron creadores con la categoría {categoria}."

    En cualquier otro caso, se debe mostrar:
    "Creadores de contenido de la categoría {categoria}: {creadores}"
    """
    categoria = str(input("ingrese categoria"))
    resultado = tk.filtrar_creadores_por_categoria(categoria,c1,c2,c3,c4)
    print(resultado)


def ejecutar_calcular_promedio_vistas(c1: dict, c2: dict, c3: dict, c4: dict) -> None:
    """
    Función que ejecuta la opción de calcular el promedio de vistas de los creadores de contenido.

    Parámetros:
    c1 (dict): Diccionario con los datos del creador 1.
    c2 (dict): Diccionario con los datos del creador 2.
    c3 (dict): Diccionario con los datos del creador 3.
    c4 (dict): Diccionario con los datos del creador 4.

    """
    # TODO11: Implemente la función tal y como se describe en la documentación.
    pass


def ejecutar_filtrar_creadores_por_vistas(c1: dict, c2: dict, c3: dict, c4: dict) -> None:
    """
    Función que ejecuta la opción de buscar creadores de contenido con un mínimo de vistas.

    Parámetros:
    c1 (dict): Diccionario con los datos del creador 1.
    c2 (dict): Diccionario con los datos del creador 2.
    c3 (dict): Diccionario con los datos del creador 3.
    c4 (dict): Diccionario con los datos del creador 4.

    """
    # TODO12: Implemente la función tal y como se describe en la documentación.
    #        Solicite al usuario el valor requerido para invocar 
    #        correctamente a la función de la lógica.
    pass


def ejecutar_calcular_rating_creador(c1: dict, c2: dict, c3: dict, c4: dict) -> None:
    """
    Función que ejecuta la opción de calcular el rating de un creador de contenido.

    Parámetros:
    c1 (dict): Diccionario con los datos del creador 1.
    c2 (dict): Diccionario con los datos del creador 2.
    c3 (dict): Diccionario con los datos del creador 3.
    c4 (dict): Diccionario con los datos del creador 4.

    """
    # TODO13: Implemente la función tal y como se describe en la documentación.
    #        Solicite al usuario el valor requerido para invocar 
    #        correctamente a la función de la lógica.
    # TIP: En esta función se invoca a dos funciones de la lógica.
    pass


def ejecutar_buscar_creador_favorito(c1: dict, c2: dict, c3: dict, c4: dict) -> None:
    """
    Función que ejecuta la opción de recomendar un creador de contenido favorito.

    Parámetros:
    c1 (dict): Diccionario con los datos del creador 1.
    c2 (dict): Diccionario con los datos del creador 2.
    c3 (dict): Diccionario con los datos del creador 3.
    c4 (dict): Diccionario con los datos del creador 4.

    """
    # TODO14: Implemente la función tal y como se describe en la documentación.
    #        Solicite al usuario los valores requeridos para invocar 
    #        correctamente a la función de la lógica.
    pass


def ejecutar_buscar_creador_inactivo(c1: dict, c2: dict, c3: dict, c4: dict) -> None:
    """
    Función que ejecuta la opción de buscar el creador de contenido más inactivo.

    Parámetros:
    c1 (dict): Diccionario con los datos del creador 1.
    c2 (dict): Diccionario con los datos del creador 2.
    c3 (dict): Diccionario con los datos del creador 3.
    c4 (dict): Diccionario con los datos del creador 4.

    Si la fecha de referencia es menor a la fecha de la última publicación de
    todos los creadores, se debe mostrar el siguiente mensaje:

    "No se puede viajar en el tiempo."

    En cualquier otro caso, imprime el siguiente mensaje:

    "El creador de contenido que lleva más tiempo sin publicar es {nombre} con
    {anios} años {meses} meses y {dias} días."
    """
    # TODO15: Implemente la función tal y como se describe en la documentación.
    #        Solicite al usuario el valor requerido para invocar 
    #        correctamente a la función de la lógica.
    pass


# Función principal
def iniciar_aplicacion() -> None:

    creador1 = tk.construir_creador(
        nombre="BORREGO",
        pais="Colombia",
        categorias="Comedia,Educación",
        likes=986000000,
        vistas=6570000000,
        seguidores=31900000,
        fecha_ultima_publicacion=20240819,
    )

    creador2 = tk.construir_creador(
        nombre="Zach King",
        pais="Estados Unidos",
        categorias="Comedia",
        likes=1200000000,
        vistas=8000000000,
        seguidores=82200000,
        fecha_ultima_publicacion=20240810,
    )

    creador3 = tk.construir_creador(
        nombre="robegrill",
        pais="México",
        categorias="Cocina,Educación",
        likes=350000000,
        vistas=2300000000,
        seguidores=16000000,
        fecha_ultima_publicacion=20240820,
    )

    creador4 = tk.construir_creador(
        nombre="Michael Le",
        pais="Estados Unidos",
        categorias="Baile",
        likes=1400000000,
        vistas=9300000000,
        seguidores=51400000,
        fecha_ultima_publicacion=20240810,
    )

    ejecutando = True

    while ejecutando:
        print("Creadores existentes\n")
        print("Creador 1\n")
        mostrar_creador(creador1)
        print("-" * 50)

        print("Creador 2\n")
        mostrar_creador(creador2)
        print("-" * 50)

        print("Creador 3\n")
        mostrar_creador(creador3)
        print("-" * 50)

        print("Creador 4\n")
        mostrar_creador(creador4)
        print("-" * 50)

        ejecutando = mostrar_menu_aplicacion(creador1, creador2, creador3, creador4)

        if ejecutando:
            input("Presione cualquier tecla para continuar...")


def mostrar_menu_aplicacion(
    creador1: dict, creador2: dict, creador3: dict, creador4: dict
) -> bool:
    print("Menú de opciones")
    print(" 1 - Buscar creador por nombre")
    print(" 2 - Buscar creadores por categoría")
    print(" 3 - Calcular promedio de vistas")
    print(" 4 - Buscar creadores con mínimo de vistas")
    print(" 5 - Calcular rating de un creador")
    print(" 6 - Recomendar creador favorito")
    print(" 7 - Buscar creador con más días sin publicar")
    print(" 8 - Salir de la aplicación")

    opcion_elegida = input("Ingrese la opción que desea ejecutar: ").strip()

    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_buscar_creador_por_nombre(creador1, creador2, creador3, creador4)
    elif opcion_elegida == "2":
        ejecutar_filtrar_creadores_por_categoria(creador1, creador2, creador3, creador4)
    elif opcion_elegida == "3":
        ejecutar_calcular_promedio_vistas(creador1, creador2, creador3, creador4)
    elif opcion_elegida == "4":
        ejecutar_filtrar_creadores_por_vistas(creador1, creador2, creador3, creador4)
    elif opcion_elegida == "5":
        ejecutar_calcular_rating_creador(creador1, creador2, creador3, creador4)
    elif opcion_elegida == "6":
        ejecutar_buscar_creador_favorito(creador1, creador2, creador3, creador4)
    elif opcion_elegida == "7":
        ejecutar_buscar_creador_inactivo(creador1, creador2, creador3, creador4)
    elif opcion_elegida == "8":
        continuar_ejecutando = False
    else:
        print("Opción no válida, por favor intente de nuevo")

    return continuar_ejecutando


if __name__ == "__main__":
    iniciar_aplicacion()
