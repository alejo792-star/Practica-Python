
def distance (x0,x1,y0,y1):
    dist=(((x0-x1)**2)+((y0-y1)**2))**0.5
    return dist

def area_triang(x1,x2,x3,y1,y2,y3):
    a=distance(x3,x2,y3,y2)
    b=distance(x3,x1,y3,y1)
    c=distance(x2,x1,y2,y1)
    Semi=(a+b+c)/2
    area=(Semi*((Semi-a)*(Semi-b)*(Semi-c)))
    return area


def



def



def



def