
#Construir un algoritmo que multiplicar los números introducidos por el usuario 
# que estén en  el  rango  (1,10).  Terminar  cuando  el  usuario  introduzca  un  número  fuera  del  rango  y mostrar el resultado.


numero = int(input("Digite un numero: "))
total = 1

while numero <= 10 and numero >= 1:
    total= total * numero
    numero = int(input("Ingrese un numero: "))

print(f"el resultado de las multiplicaciones es {total}")

