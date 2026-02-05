import math

radio = float(input('ingrese Radio: '))
angulo = float(input('ingrese Angulo: '))

radianes=math.radians(angulo)
#simpre se deben coinvertir los grados a radianes.

x = radio * (math.cos(radianes))
y = radio * (math.sin(radianes))


print(f"x= {x} y y= {y}")




