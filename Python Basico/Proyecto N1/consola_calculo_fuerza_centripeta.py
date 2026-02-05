import calculadora_fuerzas

masa=(float(input("Masa: ")))
velocidad=(float(input("Velocidad: ")))
radio=(float(input("Radio: ")))

Fcentripeda=calculadora_fuerzas.calcular_centripeta(masa,velocidad,radio)
print("El valor de la F Centripeda es:",Fcentripeda)
