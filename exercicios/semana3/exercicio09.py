import csv


class FinElements:
    
    def find_start_subtring_credit_card(self, lista, parametro='303'):
        lista_nomes = []
        for item in lista:
            if item.get('credit_card').startswith(parametro):
                lista_nomes.append(item.get('name'))
        return lista_nomes

    def find_subtring_credit_card(self, lista, parametro='322'):
        lista_nomes = []
        for item in lista:
            if item.get('credit_card').__contains__(parametro):
                lista_nomes.append(item.get('name'))
        return lista_nomes            


    def carregar_arquivo(self, path):
        lista_local = []
        with open(path, newline='\n') as csvfile:
            reader = csv.DictReader(csvfile)
            for line in reader:
                lista_local.append(line)        
        return lista_local


if __name__ == "__main__":
    arquivo = FinElements()
    path = 'usernames.csv' 
    lista = []
    lista = arquivo.carregar_arquivo(path) 
    print(arquivo.find_start_subtring_credit_card(lista, parametro='222'))
    print(arquivo.find_subtring_credit_card(lista))