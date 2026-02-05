n1=float(input("Ingrese nota 1: "))
n2=float(input("Ingrese nota 2: "))
n3=float(input("Ingrese nota 3: "))
n4=float(input("Ingrese nota 4: "))

menor=n1

if n2<menor:
    menor=n2
if n3<menor:
    menor=n3
if n4<menor:
    menor=n4

Suma_mejores=(n1+n2+n3+n4)-menor
promedio=Suma_mejores/3

print("El promedio de su nota es;",promedio)


