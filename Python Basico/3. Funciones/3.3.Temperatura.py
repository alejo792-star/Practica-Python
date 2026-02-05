

# Funcion que reciba un numero que representa grados celsius
# La funcion debe retornar los grados fahrenheit

def convercion(grados: int):
    f=((grados*9)/5)+32
    return f



f1=convercion(20) + convercion(30) / convercion(10)
f2=convercion(20)
f3= convercion(30) 

print("conversion 1",f1)
print("conversion 2", f2)
print("conversion 3", f3)

