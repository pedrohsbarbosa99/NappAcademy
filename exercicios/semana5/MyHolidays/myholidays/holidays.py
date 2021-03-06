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
                except:
                    pass
            self.datas = self.remove_repetido(lista)
        return self.datas

    def check_holiday(self, *data):
        for dt in data:
            if isinstance(dt, date):
                return dt in self.datas
            if isinstance(dt, str):
                try:
                    dt = datetime.strptime(dt, '%d/%m/%Y').date()
                    return dt in self.datas
                except:
                    return False
            
