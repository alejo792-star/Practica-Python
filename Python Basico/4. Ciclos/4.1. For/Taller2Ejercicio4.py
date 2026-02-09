

#Escriba  un  programa  que  simule  una  alcanc ́ıa.   El  programa  solicitar ́aprimero una cantidad, que ser ́a 
# la cantidad final de dinero que queremosahorrar.  A continuaci ́on, el programa solicitar ́a una y otra vez las canti-dades
#  que se ir ́an ahorrando, hasta que el total ahorrado iguale o supereal objetivo.  El programa solo acepta cantidades 
# positivas


meta = float(input("Ingrese la cantidad que desea ahorrar: "))
ahorros = 0

while ahorros < meta:
    cantidad = float(input("Ingrese una cantidad a ahorrar: "))
    
    if cantidad > 0:
        ahorros += cantidad
        
    else:
        print("Solo se aceptan cantidades positivas.")

print("¡Meta alcanzada!")
print("Total ahorrado:", ahorros)
    
    

    
