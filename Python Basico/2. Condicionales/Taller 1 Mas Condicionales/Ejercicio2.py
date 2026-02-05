


year=int(input("Ingrese el año que desea Consultar: "))


if(year%4==0 and year%100==0):
    print("El año ingresado NO es Bifiesto.")
elif(year%400==0):
    print("El año ingresado SI es Bifiesto.")
else:
    print("El año ingresado es bifiesto")
