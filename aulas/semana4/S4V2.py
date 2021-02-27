"""
* S4V2 - Testes

"""
def max_product(*args):
    lista_numeros = list(args)
    lista_numeros = [float(numero) for numero in lista_numeros]
    lista_numeros.sort()
    maior_valor = lista_numeros[-1]
    segundo_maior_valor = lista_numeros[-2]
    return maior_valor * segundo_maior_valor


assert max_product(1,2,3,4,5) == 20
assert max_product(1,5,0,2) == 10
assert max_product(1,5,0,2,20,10) == 200
assert max_product(1,10,0,2,20,3) == 200