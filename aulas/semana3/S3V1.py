"""
* S3V1 - Dicionários

* O tipo dict não é só amplamente usado em
* nossos programas como também é parte
* fundamental da implementação de Python.
* Namespaces de módulos, atributos de
* classes e de instâncias e argumentos
* nomeados de funções são algumas das
* construções básicas em que os dicionários
* são implementados.
"""

a = dict(one=1, two=2, three=3)
b = {'one':1, 'two': 2, 'three':3 }
c = dict(zip(['one','two','three'], [1,2,3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two':2})
a == b == c == d == e

lista_telefonica = {}
lista_telefonica['Orlando'] = ['Orlando','Rio Claro']
lista_telefonica['ana'] = ['Ana','Araras']
lista_telefonica['Lucas'] = ['Lucas','Leme']
lista_telefonica['xyz'] = 'Teste'
lista_telefonica['xy'] = 15
lista_telefonica.pop('xyz')
print('Ana' in list(lista_telefonica))
print('ana' in list(lista_telefonica))

"""
* O tipo set e seu irmão imutável frozenset
* apareceram inicialmente em um módulo de
* python 2.3 e foram promovidos a tipos
* embutidos em Python 2.6
* Um conjunto é uma coleção de objetos
* conjuntos é a remoção de objetos duplicados:
"""

lista = [1,2,3,4,1,2,3]
lista = list(set(lista))
a = set(list(range(1,8)))
b = set(list(range(5,13)))
c = {4,5}
a.union(b)
a.intersection(b)
a.difference(b)
c.issubset(b)
c.issubset(a)