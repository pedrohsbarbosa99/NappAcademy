def extrair_novos_registros(lista_antiga, lista_nova):  
    lista_novos_registros = []  
    for registro in lista_nova:
        if registro not in lista_antiga:
            lista_novos_registros.append(registro)
    return lista_novos_registros


lista_antiga = [('Pessoa1', 20), ('Pessoa 2', 21), ('Pessoa 3', 22)]
lista_nova   = [('Pessoa1', 20), ('Pessoa 2', 21), ('Pessoa 3', 22), ('Pessoa 4', 23), ('Pessoa 5', 24)]

lista_novos_registros = extrair_novos_registros(lista_antiga, lista_nova)
print(lista_novos_registros)