
sueldo = int(input("Escriba el sueldo: "))
a=0.03
b=0.05
c=0.09


if (sueldo >200000 and sueldo <400000):
    descuento=sueldo*a
    total=sueldo-descuento
    print("sueldo", sueldo)
    print("descuento", descuento)
    print("tipo de descuento A")
    print("Total a pagar", total)
elif(sueldo>=400000 and sueldo<=1000000):
    descuento=sueldo*b
    total=sueldo-descuento
    print("sueldo", sueldo)
    print("descuento", descuento)
    print("tipo de descuento B")
    print("Total a pagar", total)
elif(sueldo>1000000):
    descuento=sueldo*c
    total=sueldo-descuento
    print("sueldo", sueldo)
    print("descuento", descuento)
    print("tipo de descuento C")
    print("Total a pagar", total)

    
    





