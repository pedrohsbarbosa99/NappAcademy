lista_nomes = ['Ana', 'Maria', 'Jose', 'Pedro', 'Elena', 'Helena', 'Elen']
vogais = ['A', 'E', 'I', 'O', 'U']

for nome in lista_nomes:
    primeira_letra = nome[0]
    for letra in vogais:
        if primeira_letra.upper() in letra:
            print(nome)
