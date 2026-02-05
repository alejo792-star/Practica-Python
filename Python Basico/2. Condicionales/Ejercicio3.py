impuesto=0
multa=0

venta=float(input("Escriba el valor de su compra; "))


if  venta<500:
    impuesto=venta*0.06
   
else:
    impuesto=venta*0.035
    if(impuesto>350):
        multa=impuesto*0.06
        
total=venta+impuesto+multa

print("Valor venta:", venta)
print("Valor impuesto:",impuesto)
print("Valor multa:", multa)
print("Total a pagar:", total)
    

