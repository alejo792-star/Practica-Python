import math

edades = [23,43,45,213,34]

sumador = 0
promedio = 0

for uwu in range( len(edades) ):
    sumador = sumador +   edades[uwu]
promedio = sumador/len(edades)
sumador =sumador

almacenador =0
for i in range(len(edades)):
    res1= (edades[i] - promedio)**2
    almacenador = almacenador + res1

almacenador=(len(edades) - 1/4)* almacenador
resutadof =math.sqrt(almacenador)

print(sumador)


