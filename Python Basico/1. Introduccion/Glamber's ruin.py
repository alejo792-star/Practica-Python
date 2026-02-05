n1 = int(input("Ingrese N1: "))
n2 = int(input("Ingrese N2: "))
p0 = float(input("Ingrese P1: "))
q0 =1 - p0

p1=((1-(p0/q0)**n2)/(1-(p0/q0)**(n1+n2)))
p2=((1 - (q0 / p0)**n1)/(1-(q0 /p0)**(n1+n2)))

print(f"Probabilidad player 1 {p1}, probabilidad player 2 {p2}")
