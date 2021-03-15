lista_nomes = ['Ana', 'AnaMaria', 'Pedro', 'Elena', 'Helena', 'Elen']

for nome in lista_nomes:
    for letra in range(len(nome)):
        if letra == 0:
            print(' |', nome[letra], ' | ', end="")
        else:
            print('', nome[letra], ' | ', end="") 
    print()
