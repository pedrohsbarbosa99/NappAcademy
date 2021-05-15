import csv
from datetime import datetime

ano_atual = datetime.now().strftime('%Y')
primeira_eleicao = 1996


def abre_csv(file='candidatura.csv', ano_eleicao='1996'):
    for linha in open(file):
        if f'ELEICOES {ano_eleicao}' in linha:
            yield linha


for x in range(primeira_eleicao, int(ano_atual) - 4, 4):
    line = abre_csv(ano_eleicao=x)
    with open(f'leituras/eleicao_{x}.csv', 'w', newline='\n') as csvfile:
        while True:
            try:
                csvfile.write(next(line))
            except:
                del line
                break
