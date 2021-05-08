import csv



def find_start_subtring_credit_card(lista, parametro='303'):
    lista_nomes = []
    for item in lista:
        if item.get('credit_card').startswith(parametro):
            lista_nomes.append(item.get('name'))
    return lista_nomes

def find_subtring_credit_card(lista, parametro='322'):
    lista_nomes = []
    for item in lista:
        if item.get('credit_card').__contains__(parametro):
            lista_nomes.append(item.get('name'))
    return lista_nomes            


def carregar_arquivo(path):
    lista_local = []
    with open(path, newline='\n') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            lista_local.append(line)        
    return lista_local
            

if __name__ == "__main__":
    path = 'usernames.csv'
    lista = []
    lista = carregar_arquivo(path)
    print(find_subtring_credit_card(lista))
    print(find_subtring_credit_card(lista, '222'))
    print(find_start_subtring_credit_card(lista))
    print(find_start_subtring_credit_card(lista, '222'))