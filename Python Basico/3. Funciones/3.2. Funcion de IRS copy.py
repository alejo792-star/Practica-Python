



def calculo_del_irs(  edad , expo  ):
    if (edad > 18):
        irs = edad ** expo
        return irs
    else:
        irs = edad ** expo
        return irs
#########################################################


ed = int(input())
ex = int(input())

result_irs1 = calculo_del_irs(ed,ex)




result_irs2 = calculo_del_irs(20,0.17)
result_irs3 = calculo_del_irs(31,0.05)
result_irs4 = calculo_del_irs(19,0.78)
result_irs5 = calculo_del_irs(65,0)

print("El resultado del irs1 es",result_irs1)
print("El resultado del irs2 es",result_irs2)
print("El resultado del irs3 es",result_irs3)
print("El resultado del irs4 es",result_irs4)
print("El resultado del irs5 es",result_irs5)
