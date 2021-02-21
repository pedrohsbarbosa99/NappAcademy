from massa_dados import list_spend_money

def spend_by_subname(name):
    for registro in list_spend_money:
        if registro[0].__contains__(name):
            registros = print(registro)
    return registros


def sum_by_subname(name):
    soma = 0
    for registro in list_spend_money:
        try:
            if registro[0].upper().__contains__(name.upper()):
                for gasto in range(len(registro)):
                    if gasto == len(registro)-1:
                        soma += float(registro[gasto])
        except:
            pass
    return round(soma, 2)


if __name__ == "__main__":
    name = 'J'
    spend_by_subname(name)
    print('A soma total é: ')
    print(sum_by_subname(name))