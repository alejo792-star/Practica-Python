# Los simbolos para hacer condioconales son

#   >    Mayor que
#   <    Menor que
#   >=   Mayor o igual que
#   <=   Menor o igual quel
#   ==   Igual que
#   !=   Diferente de


w= 90
h= 1.80
f=(w)/(h**2)

print("S8u IBM es: "+str(f))

if (f< 18.5):
    print("underweight")

else:
    if (f>18.5 and f<24.9):
        print("normal")

    else:
        if (f>=25 and f <=29.9):
            print("overweigth")

        else:
            if (f >30 and f <34.9):
                print("obse")

            else:
                print("Extremly obese")

