#Construir un algoritmo que calcule la suma de lo
# números introducidas por el usuario, 
# el programa debe terminar cuando se  introduzca cero.

numero = float(input("ingrese numero a sumar: "))

total = 0

while numero != 0:
    total = total + numero
    numero=int(input("Escriba un numero: "))

print (f"El total de numeros sumados: {total}")
