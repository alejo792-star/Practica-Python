edades = { "Carlos":32 , "Stefania":45 , "Camilo":65 }



# Un almacenamiento para datos Llave - Valor   Key - Values


edad1 = int(input())
edad2 = int(input())


nueva_llave =  input()




persona1 = { 
    "nombre": "Ana", 
    "edad": edad1, 
    "email": "ana@example.com", 
    "telefono": "+34 600 123 456", 
    "activo": True,
    nueva_llave:56
}


persona2 = {
    "nombre": "Carlos",
    "edad": edad2,
    "email": "carlos.perez@example.com",
    "telefono": "+52 55 9876 5432",
    "activo": False,
    nueva_llave:54
}



if persona1 ["edad"] < persona2 ["edad"]:
    print(f"persona 2 mayor: {persona2['nombre']},{persona2['edad']},{persona2['email']}")
else:
    print(f"Persona 1 mayor: {persona1['nombre']}, {persona1['edad']}, {persona1['email']}")



