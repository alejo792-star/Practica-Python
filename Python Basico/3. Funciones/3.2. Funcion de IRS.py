



def calculo_del_irs(  edad  ):
    if (edad > 18):
        irs = edad ** 0.16
        return irs
    else:
        irs = edad ** 0.08
        return irs
#########################################################


result_irs1 = calculo_del_irs(10)
result_irs2 = calculo_del_irs(20)
result_irs3 = calculo_del_irs(31)
result_irs4 = calculo_del_irs(19)
result_irs5 = calculo_del_irs(65)

print("El resultado del irs1 es",result_irs1)
print("El resultado del irs2 es",result_irs2)
print("El resultado del irs3 es",result_irs3)
print("El resultado del irs4 es",result_irs4)
print("El resultado del irs5 es",result_irs5)
