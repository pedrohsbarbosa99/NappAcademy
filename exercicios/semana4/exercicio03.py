from datetime import datetime

today = datetime.today()
born_date = datetime(1999, 3, 16)
if today.month < born_date.month:
    anos =  today.year - (born_date.year + 1)
else:
    anos =  today.year - born_date.year
print(f'Voce tem {anos} de idade')