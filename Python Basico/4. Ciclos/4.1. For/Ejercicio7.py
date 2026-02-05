n=int(input("Ingrese Valor N: "))

if (n < 1):
    print("Ingrese un numero mayor a 1")

m=(n + 1)//2
suma=0

for i in range (1, m+1):
    suma=(2 * i)/(2 *i-1)
print(suma)