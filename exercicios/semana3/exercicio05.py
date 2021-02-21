import csv


def find_born_in_month_and_gender(lista, paramether='03', gender='F'):
    """
    Função que recebe a lista com todos os registros carregados de um
    arquivo CSV via Reader e busca os clientes nascidos no mês 'paramether'
    E pelo gênero gender.

    Args:
        lista (List): Lista de tuplas
        paramether (str, optional): Mês de nascimento com dois caracteres
        janeiro = '01', Fevereiro = '02' . Padrão '03'.
        gender (str, optional): Gênero ( M ou F) com um caracter. Padrão 'F'.

    Returns:
        List: Lista com os nomes de pessoas que nasceram no mês informado
        e com gênero informado.
    """
    lista_nomes = []
    for item in lista:
        birthdate = item[-2]
        mes_nasc = birthdate[5:7]
        genero = item[-1]
        if mes_nasc == paramether and genero == gender:
            lista_nomes.append(item[0])
    return lista_nomes


def carregar_arquivo(path):
    """
    Função que recebe a string com o arquivo, abre o arquivo CSV
    com o reader e carrega os dados em uma lista retornada.

    Args:
        path (String): Nome do arquivo

    Returns:
        (List): Lista com todos os registros
    """
    local_list = []
    with open(path, newline='\n') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for line in reader:
            local_list.append(line)
    return local_list


if __name__ == "__main__":
    path = 'usernames.csv'
    lista = []
    lista = carregar_arquivo(path)
    print(find_born_in_month_and_gender(lista))
    print(find_born_in_month_and_gender(lista, '01'))
    print(find_born_in_month_and_gender(lista, '01', 'M'))