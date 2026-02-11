

personas = [
    {"nombre":"Maicol", "edad":23, "peso":90, "altura":1.9} , 
    {"nombre":"Stefania", "edad":30, "peso":76, "altura":1.6},  
    {"nombre":"Natalia", "edad":36, "peso":80, "altura":1.7},
    ]

# CALCULO PROMEDIO DE EDAD VER 1
# promedio = 0
# total_edad = 0

# for i in personas:
#     total_edad = total_edad + i["edad"]
    
# promedio = total_edad / len(personas)

# print(round(promedio,2))


# CALCULO PROMEDIO DE EDAD VER 2
# promedio = 0
# total_edad = 0

# for i in range(len(personas)):
#     total_edad += personas[i]["edad"]

# promedio = total_edad / len(personas)

# print(round(promedio,2))



# Maicol tiene un BMI de ___ y su clasificacion es ___
# Stefania tiene un BMI de ___ y su clasificacion es ___
# Natalia tiene un BMI de ___ y su clasificacion es ___






# for i in range(len(personas)):
#     bmi = ((personas[i]["peso"]) / personas[i]["altura"] **2)

#     if (bmi< 18.5):
#         print(f"{personas[i]["nombre"]} tiene un BMI de {bmi} y su clasificacion underweight")

#     elif (bmi>18.5 and bmi<25):
#         print(f"{personas[i]["nombre"]} tiene un BMI de {bmi} y su clasificacion normal")

#     elif (bmi>=25 and bmi < 30):
#         print(f"{personas[i]["nombre"]} tiene un BMI de {bmi} y su clasificacion overweigth")

#     elif (bmi >30 and bmi <34.9):
#         print(f"{personas[i]["nombre"]} tiene un BMI de {bmi}obse")

#     else:
#         print( f"{personas[i]["nombre"]} tiene un BMI de {bmi} y su clasificacion Extremly obese")

    




# Funcion recibe el peso y la altura, y retorna su clasificacion 
# el retorno es la palabra "underweight"....

def calculo_bmi (peso, alturta):
    bmi = ((peso) / (alturta ** 2))
    if (bmi< 18.5):
        return ["Underweight",bmi]
    
    elif (bmi>18.5 and bmi<25):
        return ["normal",bmi]
    
    elif (bmi>=25 and bmi < 30):
        return ["overweigth",bmi]
    
    elif (bmi >30 and bmi <34.9):
        return ["obese",bmi]
    
    else:
        return ["Extremly obese",bmi]


for i in range(len(personas)):
    resultados = calculo_bmi( personas[i]["peso"],  personas[i]["altura"])
    clasificacion = resultados[0]
    bmi = resultados[1]
    print( f"{personas[i]["nombre"]} tiene un BMI de {bmi} y su clasificacion es {clasificacion}")
