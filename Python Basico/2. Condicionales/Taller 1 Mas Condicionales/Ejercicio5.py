x1=int(input("Numero1: "))
x2=int(input("Numero2: "))
x3=int(input("Numero3: "))
x4=int(input("Numero4: "))
x5=int(input("Numero5: "))

print("****Menu Operaciones****")
print("A.Media Arismetica:")
print("G.Media geometrica:")
print("H.Media Armonica:")
opcion=(str(input("Ingrese una opcion.").lower()))
n=5
match opcion:
    case "a":
        a=(x1+x2+x3+x4+x5)/n
        print(a)
    case "g":
        g=(x1*x2*x3*x4+x5)**(1/n)
        print(g)
    case "h":
        h=n/(1/x1+1/x2+1/x4+1/x5)
        print(h)
print("****** FIN ******")

