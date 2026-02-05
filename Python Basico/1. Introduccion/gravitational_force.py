import sys

if len(sys.argv) !=4:
    print("Uso: Python3 gravitational_force.py m1 m2 r1")
    sys.exit(1)
m1 = float(sys.argv[1])
m2 = float(sys.argv[2])
r1 = float(sys.argv[3])

gravedad= 6.674 * 10**-11

force= gravedad*(m1*m2)/(r1**2)

print(force)


