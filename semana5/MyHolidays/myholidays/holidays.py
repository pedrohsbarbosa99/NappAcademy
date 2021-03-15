from datetime import datetime, date


class MyCalendar:
    def __init__(self, *args):
        self.datas = []
        self.datas = self.add_holiday(*args)

    def remove_repetido(self, lista):
        lisa_interna = []
        for i in lista:
            if i not in lisa_interna:
                lisa_interna.append(i)
        return lisa_interna

    def normalize_data(self, data):
        if isinstance(data, date):
            return data
        if isinstance(data, str):
            try:
                data = datetime.strptime(data, '%d/%m/%Y').date()
                return data
            except Exception:
                pass

    def add_holiday(self, *args):
        lista = self.datas
        for arg in args:
            arg = self.normalize_data(arg)
            if arg:
                lista.append(arg)
            self.datas = self.remove_repetido(lista)
        return self.datas

    def check_holiday(self, data):
        data = self.normalize_data(data)
        return data in self.datas
