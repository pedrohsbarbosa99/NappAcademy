from massa_dados_situacao_teste import lista_pessoas

# * Test 2:
pedaco = slice(0,2)
def lista_simples(lista_pessoas):
    lista = []
    for item in lista_pessoas:
        if lista_pessoas != type(str):
            lista.append((item[0], item[-1]))
        else:
            lista = []
    return lista


entrada = 'string'
saida_esperada = []
saida = lista_simples(entrada)
print(saida)
assert(saida == saida_esperada)