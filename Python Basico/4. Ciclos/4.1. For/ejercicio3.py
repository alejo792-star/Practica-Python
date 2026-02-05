n1=int(input("Escriba rango1: "))
n2=int(input("Escriba rango2: "))

total=0
contar=0

for j in range(n1,n2+1):
    if(j%3==0):
        contar=contar + 1

print(contar)

