

for uwu in range(4):
    w= float(input("Ingrese su peso: "))
    h= float(input("Ingrese su altura: "))
    f=(w)/(h**2)

    print("S8u IBM es: "+str(f))

    if (f< 18.5):
        print("underweight")

    elif (f>18.5 and f<24.9):
        print("normal")

    elif (f>=25 and f <=29.9):
        print("overweigth")

    elif (f >30 and f <34.9):
        print("obse")

    else:
        print("Extremly obese")


