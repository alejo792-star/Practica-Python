valor = int(input("Ingrese valor N: "))
resultado = 0 

for i in range(1, valor + 1):
    if i % 2 == 0:
        resultado -= i/i
        print(resultado)
    else:
        resultado += 1/i
        print(resultado)


print(resultado)