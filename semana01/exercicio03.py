lista_nomes = ['Ana', 'Maria', 'Jose', 'Pedro', 'Elena', 'Helena', 'Elen']
lista_nomes = lista_nomes + ['Mario', 'Arnaldo', 'Lucas', 'Maria Vitoria']
lista_nomes = lista_nomes + ['Vitor', 'Ana Paula', 'Maria Aparecida']

for nome in lista_nomes:
    name = nome.split(' ')
    if len(name) > 1:
        print(nome)