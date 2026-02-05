


def distance (x0,x1,y0,y1):
    dist=(((x0-x1)**2)+((y0-y1)**2))**0.5
    return dist

dist1 = distance(2,5,2,6)
print("la distancia recorrida es:", dist1)
