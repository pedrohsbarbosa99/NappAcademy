def max_product(*args):
    lista_numeros = list(args)
    lista_numeros = [float(numero) for numero in lista_numeros]
    lista_numeros.sort()
    maior_valor = lista_numeros[-1]
    segundo_maior_valor = lista_numeros[-2]
    return maior_valor * segundo_maior_valor
