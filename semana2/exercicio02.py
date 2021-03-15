from massa_dados import list_spend_money

def spend_by_gender(gender):
    for registro in list_spend_money:
        if registro[2].upper() == gender.upper():
            registros = print(registro)
    return registros


def sum_by_gender(gender):
    soma = 0
    for registro in list_spend_money:
        try:
            if registro[2] == gender:
                for gasto in range(len(registro)):
                    if gasto == len(registro)-1:
                        soma += float(registro[gasto])
        except:
            pass
    return round(soma, 2)


if __name__ == "__main__":
    gender = 'M'
    spend_by_gender(gender)
    print('A soma total é: ')
    print(sum_by_gender(gender))