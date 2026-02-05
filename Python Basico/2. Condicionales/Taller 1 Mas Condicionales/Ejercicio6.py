print("*** Menu pescados ***")
print("1.Pargo     ---> 9900")
print("2.Lebranche ---> 7500")
print("3.Sierra    ---> 12500")

producto=0
opcion=int(input("Ingrese una opcion:"))
cantidad=int(input("Ingrese cantidad a comprar:"))

match opcion:
    case 1:
        producto=9900
        descuento=0.15
    case 2:
        producto=7500
        descuento=0.25
    case 3:
        producto=12500
        descuento=0.10

if(cantidad>=10):
    Subtotal=cantidad*producto
    iva=Subtotal*descuento
    total=Subtotal-descuento
else:
    Subtotal=cantidad*producto
    iva=0
    total=Subtotal

print("Subtotal:", Subtotal)
print("iva:", iva)
print("total:", total)



