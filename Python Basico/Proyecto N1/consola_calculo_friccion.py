import calculadora_fuerzas

masa= float(input("Ingrese el valor de la masa: "))
coeficiente_friccion =(float(input("Ingrese el valor del coeficioente: ")))

friccion1=calculadora_fuerzas.calcular_friccion(masa,coeficiente_friccion)
print("el resultado de la friccion es:",friccion1)