from datetime import datetime

today = datetime.today()
born_date = datetime(1999, 3, 16)
count_day_life = today - born_date
print(f' Voce possui {count_day_life.days} de vida')