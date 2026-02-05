
inicio = int(input("ingrese numero menor:"))
fin = int(input("Ingrese numero mayor"))

numero = inicio

while numero <= fin:
    if numero % 3 == 0:
        print(numero)
    numero += 1


