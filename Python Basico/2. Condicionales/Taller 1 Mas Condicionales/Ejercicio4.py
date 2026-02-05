num1=int(input("Escriba el numero 1: "))
num2=int(input("Escriba el numero 2: "))
num3=int(input("Escriba el numero 2: "))

mayor=max(num1,num2,num3)
menor=min(num1,num2,num3)
if (num1==num2 or num2==num3 or num1==num3):
    iguales="Si Numeros repetidos"
else:
    iguales="no hay numeros iguales."

print("El numero mayor es ",  mayor, "y el numero menor es ", menor)
print(iguales)

