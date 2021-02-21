"""
* S2V1 - Tuplas, ranges e a instrução try:

"""
# * Tuplas

print('tuplas\n')
tupla = (1,2,3,1,4,1)
tupla.count(1)
registro = ('Pedro Henrique', 'pedro.barbosa@nappsolutions.com', 21)
registro[0]
nome, email, idade = registro
print(nome)
print(idade)
print(email)

# * tuplas em listas
print('\n\ntuplas em listas\n')
lista_registros = []
registro1 = ('Produto 1', 100, 150.55)
registro2 = ('Produto 2', 200, 247.25)
lista_registros.append(registro1)
lista_registros.append(registro2)
print(lista_registros)
print(lista_registros[0])
print(lista_registros[0][0])

soma = 0
for item in lista_registros:
    soma += item[1]

print(soma)

# * range
print('\n\nRANGE\n')
intervalo = range(0, 10, 2)
print(type(intervalo))
print(list(intervalo))
for item in list(intervalo):
    print(item)

produto3 = ('Produto 3', 250, 75.90)
lista_registros.append(produto3)
print(lista_registros)
intervalo = range(0, len(lista_registros), 2)

for produto in list(intervalo):
    print(lista_registros[produto])

# * instrução try
print('\n\ninstrução try\n')
lista_registros.append(('Produto 4', 400, '23.45'))
lista_registros.append(('Produto 5', 500, 'Sem valor'))
soma = 0

for item in lista_registros:
    try:
        soma += item[-1]
    except TypeError:
        print('Nao foi possivel somar: ' + item[-1])

print(soma)