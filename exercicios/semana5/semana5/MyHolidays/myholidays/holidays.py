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

    def add_holiday(self, *args):
        lista = self.datas
        for arg in args:
            if isinstance(arg, date):
                lista.append(arg)
            if isinstance(arg, str):
                try:
                    arg = datetime.strptime(arg, '%d/%m/%Y').date()
                    lista.append(arg)
                except Exception:
                    pass
            self.datas = self.remove_repetido(lista)
        return self.datas

    def check_holiday(self, data):
        if isinstance(data, date):
            return data in self.datas
        if isinstance(data, str):
            try:
                data = datetime.strptime(data, '%d/%m/%Y').date()
                return data in self.datas
            except Exception:
                return False
