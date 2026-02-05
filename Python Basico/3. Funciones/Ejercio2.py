



def area_triang(x1,x2,x3,y1,y2,y3):
    a=(((x3-x2)**2)+((y3-y2)**2))**0.5
    b=(((x3-x1)**2)+((y3-y1)**2))**0.5
    c=(((x2-x1)**2)+((y2-y1)**2))**0.5
    Semi=(a+b+c)/2
    area=(Semi*((Semi-a)*(Semi-b)*(Semi-c)))
    return area



area_triang1=area_triang(2,2,3,4,5,6)
print(area_triang1)
