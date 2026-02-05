# 1/1 +  1/3 + 1/5..... 1/X

n1=int(input("Ingrese N: "))
total = 0
contadora = 0

for j in range(1 , n1 + 1):
    residuo = j % 2
    if residuo == 1:
        total=total + 1/j
        contadora = contadora + 1

print(total)

