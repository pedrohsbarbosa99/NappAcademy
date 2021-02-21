from massa_dados import list_spend_money

def spend_by_login(login, limit=1000):
    for registro in list_spend_money:
        try:
            if registro[1] == login and registro[3] <= limit:
                registros = print(registro)
        except:
            pass
    return registros


def sum_by_login(login, limit=1000):
    soma = 0
    for registro in list_spend_money:
        try:
            if registro[1] == login:
                for gasto in range(len(registro)):
                    if gasto == len(registro)-1:
                        soma += registro[gasto]
            if soma > limit:
                for gasto in range(len(registro)):
                    if gasto == len(registro)-1:
                        soma -= float(registro[gasto])
        except:
            pass
    return round(soma, 2)



if __name__ == "__main__":
    login = 'justin16'
    spend_by_login(login, 1200)
    print('A soma total até 600: ')
    print(sum_by_login(login, 600))
    print('A soma total até 1200: ')
    print(sum_by_login(login, 1200))
