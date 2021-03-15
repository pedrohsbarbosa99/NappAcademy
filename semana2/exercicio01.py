from massa_dados import list_spend_money

def spend_by_login(login):
    for registro in list_spend_money:
        if registro[1] == login:
            registros = print(registro)
    return registros
        

def sum_by_login(login): 
    soma = 0
    for registro in list_spend_money:
        try:
            if registro[1] == login:
                for gasto in range(len(registro)):
                    if gasto == len(registro)-1:
                        soma += float(registro[3])
        except:
            pass
    return round(soma, 2)

if __name__ == "__main__":
    login = 'justin16'
    spend_by_login(login)
    print('A soma total é: ')
    print(sum_by_login(login))