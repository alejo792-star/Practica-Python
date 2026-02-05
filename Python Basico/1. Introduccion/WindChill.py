import sys

temperature=float(sys.argv[1])
wind_speed=float(sys.argv[2])

w= 35.74+(0.6215*temperature)+((0.4275*temperature)-35.75)**0.16

print(w)