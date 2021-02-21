class IMC:
    """
    calculo do IMC baseado em OO
    """
    def __init__(self, peso=80, altura=1.65):
        self.peso = peso
        self.altura = altura
        self.imc = self.calculo()
    def calculo(self):
        """
        Metodo para calculo do IMC
        """
        return self.peso / (self.altura * self.altura)

pessoa1 = IMC(89, 1.69)
pessoa2 = IMC()
pessoa1.peso
pessoa1.calculo()