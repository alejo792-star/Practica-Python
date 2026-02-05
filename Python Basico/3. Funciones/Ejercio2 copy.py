
def distance (x0,x1,y0,y1):
    dist=(((x0-x1)**2)+((y0-y1)**2))**0.5
    return dist


def area_triang(x1:float,x2:float,x3:float,y1:float,y2:float,y3:float) -> float:
    a=distance(x3,x2,y3,y2)
    b=distance(x3,x1,y3,y1)
    c=distance(x2,x1,y2,y1)
    Semi=(a+b+c)/2
    area=(Semi*((Semi-a)*(Semi-b)*(Semi-c)))
    return area



area_triang1=area_triang(2,2,3,4,5,6)
print(area_triang1)
