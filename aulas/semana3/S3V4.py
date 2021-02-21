"""
* S3V4 - Introdução à Orientação a Objetos

"""

class MinhaPrimeiraClasse:
    """ Minha Primeira Classe """
    pass

obj1 = MinhaPrimeiraClasse()

class SegundaClasse:
    """ Classe que retorna numeros """
    def retorna_dez(self):
        return 10
    def retorna_numero(self, numero):
        return numero

obj2 = SegundaClasse()

obj2.retorna_dez()

class IMC:
    peso = 100
    altura = 1.71
    def calculo(self):
        return self.peso / (self.altura * self.altura)

obj_imc = IMC()
print(obj_imc.calculo())