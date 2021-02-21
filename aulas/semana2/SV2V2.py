"""
* S2V2 - Funções

"""

def imc_1(peso, altura):
    return peso / (altura*altura)

"""imc1 = round(imc_1(65, 1.72), 2)
print(imc1)"""

def imc_2(peso, altura):
    return round(peso / (altura*altura), 2) 

"""imc2 = imc_2(65, 1.72)
print(imc2)"""

def imc_3(peso, altura):
    try:
        imc = round(peso / (altura*altura), 2)
    except:
        print('ERRO ! valor nao numerico!')
        return None
    return imc

"""imc3 = imc_3(65, '1.72')
print(imc3)"""

def imc_4(peso, altura):
    try:
        imc = round(peso / (altura*altura), 2)
    except TypeError:
        raise TypeError ('valor nao numerico')
    return imc

"""imc4 = imc_4(65, '1.72')
print(imc4)"""

def imc_5(peso, altura):
    try:
        if altura <= 0 or altura > 2.30:
            raise Exception('altura invalida!')
        if peso < 30 or peso > 260:
            raise Exception('peso invalido!')
        imc = round(peso / (altura*altura), 2)
    except TypeError:
        raise TypeError('valor nao numerico')
    return imc

"""imc5 = imc_5(40, 2.31)   
print(imc5)"""