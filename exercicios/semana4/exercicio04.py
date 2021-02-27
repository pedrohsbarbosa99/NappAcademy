from datetime import datetime, date

today = datetime.today()
fatidico_dia = '2014-07-08'
fatidico_dia = datetime.strptime(fatidico_dia, '%Y-%m-%d')
dias_passados = today - fatidico_dia
print(f'se passaram {dias_passados.days} dias do fatidico dia')