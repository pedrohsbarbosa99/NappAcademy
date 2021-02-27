from datetime import datetime, timedelta

today = datetime.today()
previsao = today + timedelta(days=3, weeks=1)
previsao = previsao.strftime('%d/%m/%Y')
print(f'Daqui uma semana e tres dias, sera dia {previsao}')