import calculadora_fuerzas

masa =(float(input("Escriva el valor de masa:")))
Aceleracion = (float(input("Aceleracion de arrastre:")))
coeficiente = (float(input("Coeficiente de friccion")))

friccion=calculadora_fuerzas.calcular_aceleracion_arrastre(masa,Aceleracion,coeficiente)

print("El valor de la friccion es: ", friccion)