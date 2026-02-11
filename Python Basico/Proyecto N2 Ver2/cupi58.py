"""
Ejercicio nivel 2: Cupi58: La mejor calle de la ciudad 
Modulo de cálculos.

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


def crear_establecimiento(nombre: str, hora_apertura: int, hora_cierre: int,
                          dias_apertura: int, tipo: str, generos: str, aforo: int,
                          clientes_promedio: int, precio_bebida_mas_cara: float,
                          precio_bebida_mas_barata: float) -> dict:
    """
    Función para crear un establecimiento en la plataforma.

    Parámetros
    ----------
    nombre : str
        Nombre del establecimiento.
    hora_apertura : int
        Hora de apertura del establecimiento representado como entero en el
        formato HHMM.
    hora_cierre : int
        Hora de cierre del establecimiento representado como entero en el
        formato HHMM.
    dias_apertura : int
        Días de apertura del establecimiento representado como entero de máximo
        siete cifras. Un establecimiento que abre todos los días de la semana
        se representa como 1111111, mientras que uno que no abre ningún día se
        representa como 0. El último dígito del número corresponde a los 
        domingos, mientras que, en caso de que el número contenga siete cifras,
        el primer dígito corresponde al lunes.
    tipo : str
        Tipo del establecimiento. 
    generos : str
        Géneros musicales del establecimiento separados por comas.
    aforo : int
        Aforo máximo del establecimiento.
    clientes_promedio : int
        Clientes promedio que asisten al establecimiento.
    precio_bebida_mas_cara : float
        Precio de la bebida más cara del establecimiento.
    precio_bebida_mas_barata : float
        Precio de la bebida más barata del establecimiento.

    Retorno
    -------
    dict
        Diccionario del establecimiento con su información.

    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return None


def buscar_establecimiento_por_nombre(nombre: str, e1: dict, e2: dict, e3: dict,
                                      e4: dict) -> dict:
    """
    Busca el establecimiento con el nombre pasado por parámetro.
    En caso de no haber coincidencia se retorna None.

    Parámetros
    ----------
    nombre : str
        Nombre del establecimiento que se desea buscar.
    e1 : dict
        Diccionario con la información del primer establecimiento.
    e2 : dict
        Diccionario con la información del segundo establecimiento.
    e3 : dict
        Diccionario con la información del tercer establecimiento.
    e4 : dict
        Diccionario con la información del cuarto establecimiento.

    Retorno
    -------
    dict
        Diccionario del establecimiento con el nombre pasado por parámetro.
        Retorna None si no lo encuentra.

    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return None


def buscar_establecimiento_con_mayor_aforo(e1: dict, e2: dict, e3: dict,
                                           e4: dict) -> str:
    """
    Determina cuál es el establecimiento con mayor aforo en la aplicación.

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

    Retorno
    -------
    str
        Una cadena con el nombre del establecimiento con mayor aforo y el número
        de personas admitidas, con el formato: "El establecimiento X es el establecimiento con
        mayor aforo con Y personas." En el cual X es el nombre del establecimiento 
        y Y el número de personas.

    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return None

def determinar_dias_apertura_establecimiento(establecimiento: dict) -> dict:
    """
    Retorna en un diccionario los días de apertura de un establecimiento.

    Parámetros
    ----------
    establecimiento : dict
        Diccionario del establecimiento del cual se quiere determinar sus días de
        apertura.

    Retorno
    -------
    dict
        Un diccionario donde las llaves son cadenas con los días de la semana así:
            "L", "M", "I", "J", "V", "S", "D"
        Y las llaves son valores booleanos que indican si el establecimiento abre o no
        en ese día.
        Un ejemplo de respuesta podría ser:
        {"L":True, "M":False, "I":False, "J":True, "V":True, "S":True, "D":True}

    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return None

def calcular_horas_totales_apertura_establecimiento(establecimiento: dict) -> float:
    """
    Determina cuántas horas está abierto un establecimiento por semana.

    Parámetros
    ----------
    establecimiento : dict
        Diccionario con la información del establecimiento.

    Retorno
    -------
    float
        Un número decimal con la cantidad de horas que está abierto el
        establecimiento.

    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return None

def mostrar_establecimientos_con_genero_musical(e1: dict, e2: dict, e3: dict, e4: dict, genero: str) -> str:
    """
    Determina cuáles establecimientos tienen un género musical.

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
    genero : str
        Cadena de texto con el género musical de interés

    Retorno
    -------
    str
        Una cadena de texto incluyendo los nombres de todos los
        establecimientos que tienen el género musical separados por
        comas y un espacio (ej. "A, B, C"). En caso de que ningún 
        establecimiento tenga el género, se debe retornar un mensaje
        de la forma:
            "Ningún establecimiento tiene el género musical X."

    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return None

def calcular_puntaje_establecimiento(establecimiento: dict) -> float:
    """
    Determina el puntaje de un establecimiento de acuerdo con el
    sistema de puntuación.

    Parámetros
    ----------
    establecimiento : dict
        Diccionario con la información del establecimiento.

    Retorno
    -------
    float
        Un número decimal con el puntaje calculado redondeado
        a 2 decimales.

    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return None

def contar_establecimientos_segun_tipo(e1: dict, e2: dict, e3: dict, e4: dict, tipo: str) -> int:
    """
    Determina cuántos establecimientos son de un tipo.

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
    tipo : str
        Cadena de texto con el tipo de establecimiento de interés.

    Retorno
    -------
    int
        La cantidad de establecimientosdel tipo indicado por parámetro

    """
    # TODO: completar y remplazar la siguiente linea por el resultado correcto
    return None