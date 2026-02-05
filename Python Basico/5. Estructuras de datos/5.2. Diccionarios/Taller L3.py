


def crear_libro(nom: str, cod: str, autor: str, adp: int, cant: int, pdv: float, cpu: float)   -> dict :
    dic_libro = {
        "nombre": nom,
        "codigo": cod,
        "autor": autor,
        "añoPublicacion": adp,
        "cantidad": cant,
        "precio": pdv,
        "costoProduccion": cpu
    }

    return dic_libro


libro1 = crear_libro("Harry Potter y la piedra filosofal", "HPJK1997", "J.K. Rowling", 1997, 200, 25000, 9000)
libro2 = crear_libro("Los Juegos del Hambre", "JHSC2008", "Suzanne Collins", 2008, 100, 27000, 12000)
libro3 = crear_libro("El Hobbit", "EHJR1937", "J.R.R tolkien", 1937, 50, 35000, 15000)
libro4 = crear_libro("Hamlet", "HWS1589", "William Shakespeare", 1589, 20, 26000, 13000)
libro5  = crear_libro("Cien Años de Soledad", "CAGS1967", "Gabriel García Márquez", 1967, 80, 30000, 14000)
libro6  = crear_libro("Don Quijote de la Mancha", "DQCM1605", "Miguel de Cervantes", 1605, 40, 35000, 18000)
libro7  = crear_libro("1984", "ORWL1949", "George Orwell", 1949, 120, 28000, 13000)
libro8  = crear_libro("Crónica de una Muerte Anunciada", "CMAG1981", "Gabriel García Márquez", 1981, 60, 24000, 11000)
libro9  = crear_libro("La Metamorfosis", "KAFK1915", "Franz Kafka", 1915, 70, 22000, 10000)
libro10 = crear_libro("El Principito", "STEX1943", "Antoine de Saint-Exupéry", 1943, 150, 20000, 9000)
libro11 = crear_libro("Fahrenheit 451", "BRAD1953", "Ray Bradbury", 1953, 90, 26000, 12000)
libro12 = crear_libro("La Odisea", "HOME0800", "Homero", -800, 30, 40000, 20000)
libro13 = crear_libro("Orgullo y Prejuicio", "AUST1813", "Jane Austen", 1813, 55, 23000, 10500)
libro14 = crear_libro("El Nombre de la Rosa", "ECOR1980", "Umberto Eco", 1980, 65, 29000, 13500)


libros=[libro1,libro2,libro3,libro4,libro5,libro6,libro7,libro8,libro9,libro10,libro11,libro12,libro13,libro14]

########################################################################
def mayor_ganancia(libros):
    mayor=libros[0]
    ganancia_mayor= mayor["precio"] - mayor["costoProduccion"]
    for libro in libros:
        ganancia = libro["precio"] - libro["costoProduccion"]
        if ganancia > ganancia_mayor:
            mayor = libro
            ganancia_mayor =ganancia
    return mayor

resulado = mayor_ganancia (libros)

print(resulado)


########################################################################


# def hacer_pedido(libros):
#     faltantes = []
    
#     for libro in libros:
#         if libro['cantidad'] <=50:
#             faltantes.append(libro)
#     return faltantes


# faltantes = hacer_pedido(libros)
# print("LIBROS QUE NECESITAN REPOSICIÓN\n")

# for libro in faltantes:
#     print(f"Nombre: {libro['nombre']}")
#     print(f"Código: {libro['codigo']}")
#     print(f"Autor: {libro['autor']}")
#     print(f"Año de publicación: {libro['añoPublicacion']}")
#     print(f"Cantidad disponible: {libro['cantidad']}")
#     print(f"Precio: ${libro['precio']}")
#     print(f"Costo de producción: ${libro['costoProduccion']}")
#     print("-" * 40)
    
########################################################################

# def publicacion_venta_anio(libros,x):
#     rango = []
#     for libro in libros:
#         if libro['añoPublicacion'] <= x:
#             rango.append(libro)
#     return rango

# x = int(input("Ingrese Año: "))
# rango = publicacion_venta_anio(libros,x)
# print("***** Lista Solicitada *********\n")
# for libro in rango:
#     print(f"Nombre: {libro["nombre"]}")
#     print(f"Año de publicacion: {libro["añoPublicacion"]}")
#     print("_"*40)

####################################################################

# def ganancia_venta(libros,unidad,cant_unidad):
#     for libro in libros:
#         if libro["nombre"].lower() == unidad.lower():
#             ganancia_unitaria = libro["precio"] - libro["costoProduccion"]
#             ganancia_venta=cant_unidad*ganancia_unitaria
#             return {
#                 "Nombre": libro["nombre"],
#                 "Ganancia": ganancia_venta
#             }

#     return None


# unidad = input("Ingrese el nombre del libro: ")
# cant_unidad = int(input("Ingrese la cantidad a vender: "))

# ganancias = ganancia_venta(libros,unidad,cant_unidad)
    
# print(ganancias)

##################################################################


def venta_por_mayor(libros,unidad,cantidad):
    
    if cantidad <=0:
        return None
    
    for libro in libros:
        if libro["nombre"].low() == unidad.low():
            inventario = libro["cantidad"]

            if inventario < cantidad:
                return None
            porcentaje = cantidad / inventario
            descuento = 0.0

            if porcentaje > 0.75:
                descuento = 0.30
            elif porcentaje > 0.50:
                descuento = 0.20
            elif porcentaje > 0.75:
                descuento = 0.10
            
            subtotal = cantidad * libro["precio"]
            valor_descuento = subtotal * descuento
            total = subtotal - descuento

            return {
                "Nombre":libro["nombre"],
                "cantidad": cantidad,
                'descuento_porcentaje': descuento,
                'Descuento_valor': valor_descuento,
                "total": total
            }
    return None

        









    