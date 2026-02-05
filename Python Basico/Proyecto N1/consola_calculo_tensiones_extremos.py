import calculadora_fuerzas

radio=float(input("Longitud de cuerda: "))
masa=float(input("Masa: "))

Tension_inferior=calculadora_fuerzas.calcular_tensiones_extremos(masa,radio)
print(Tension_inferior)

