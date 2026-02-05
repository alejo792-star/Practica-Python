### funciones.


def calcular_peso(masa: float) -> float:
    """
    Calcula el peso de una caja teniendoen cuenta su masa y la gravedad de la tierra (9.8 m/s2)

    Params:
        masa: float 
            Es la masa del objeto

    Return
        float
            El calculo del peso que es la mult......
    """
    peso=masa*9.8
    return peso


def calcular_friccion(masa: float,coeficiente_friccion: float) -> float:
    peso=calcular_peso(masa)
    friccion=coeficiente_friccion*peso
    return friccion


def calcular_aceleracion_arrastre(masa,coeficiente_friccion,tension):
    fuerza_friccion=calcular_friccion(masa,coeficiente_friccion)
    Aceleracion=(tension-fuerza_friccion)/masa
    return Aceleracion


def calcular_centripeta(masa,velocidad,radio):
    Fcentripeta=(masa*velocidad**2)/radio
    return Fcentripeta


def calcular_velocidad_superior(radio):
    Vsuperior=(9.8*radio)**0.5
    return Vsuperior


def calcular_tensiones_extremos(masa: float, radio: float)  ->  str:
    peso=calcular_peso(masa)
    Tension_inferior = masa * (9.8)
    Tension_superior = Tension_inferior - 6*peso
    resultado = "Las tensiones en los puntos inferior y superior de la trayectoria son, respectivamente:" + str(Tension_inferior) + "y" + str(Tension_superior) + "N"
    resultado = f"Las tensiones en los puntos inferior y superior de la trayectoria son, respectivamente: {Tension_inferior} y {Tension_superior} N"
    return resultado

    



