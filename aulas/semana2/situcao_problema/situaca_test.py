from massa_dados_situacao_teste import lista_pessoas

pedaco = slice(0, 10)

# * Forma #1:

for item in lista_pessoas[pedaco]:
    if type(item[4]) is tuple:
        print(item[0], item[4])
    else:
        print(item[0], item[5])

pedaco = slice(0,2)

def lista_simples(lista_pessoas):
    lista = []
    for item in lista_pessoas:
        if type(item[4]) is tuple:
            lista.append((item[0], item[4]))
        else:
            lista.append((item[0], item[5]))
    return lista

saida_esperada = [('daniellemosley',('33.93113', '-117.54866')),('rhodesrichard',('39.00622', '-77.4286'))]
saida = lista_simples(lista_pessoas[pedaco])

assert(saida == saida_esperada)

# * Forma #2:
pedaco = slice(0,2)
def lista_simples2(lista_pessoas):
    lista = []
    for item in lista_pessoas:
        lista.append((item[0], item[-1]))
    return lista


saida_esperada = [('daniellemosley',('33.93113', '-117.54866')),('rhodesrichard',('39.00622', '-77.4286'))]
saida = lista_simples2(lista_pessoas[pedaco])

assert(saida == saida_esperada)