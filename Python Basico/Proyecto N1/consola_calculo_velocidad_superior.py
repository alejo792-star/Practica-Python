import calculadora_fuerzas

gravedad=(float(input("gravedad: ")))
radio=(float(input("Radio: ")))

Vsuperior=calculadora_fuerzas.calcular_velocidad_superior(gravedad,radio)
print("El calculo de la velocidad superior es ", Vsuperior)
