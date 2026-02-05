print("*** Seleccione producto**")
print("1. A100 ----- 24.05")
print("2. T247 ----- 105.00")
print("3. EC16 ----- 10.35")
print("4. k240 ----- 16.00")

producto=int(input("Escoja el producto a comprar"))
cantidad=(int(input("Escriba la cantidad a comprar.")))

match producto:
    case 1:
        producto=24.05
    case 2:
        producto=105.00
    case 3:
        producto=10.35
    case 4:
        producto=16.00

if 