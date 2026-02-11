import math

edades = [23,43,45,213,34]

sumador = 0
promedio = 0

for i in range( len(edades) ):
    sumador = sumador +   edades[i]
promedio = sumador/len(edades)

almacenador =0
for i in range(len(edades)):
    res1= (edades[i] - promedio)**2
    almacenador = almacenador + res1

almacenador=(len(edades) - 1/4)* almacenador
desviacion_estandar =math.sqrt(almacenador)

print(sumador)


