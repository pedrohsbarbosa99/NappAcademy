lista_frases = ['Eu gosto de batatas', 'Eu estava andando de moto']
lista_frases += ['Ele estava comendo no restaurante']
lista_frases += ['O cachorro está passeando pelo parque']

sufix = ['ando', 'endo', 'indo']

for frase in lista_frases:
    frase = frase.split(' ')
    for palavra in frase:
        for s in sufix:
            if palavra.__contains__(s):
                print(palavra)

