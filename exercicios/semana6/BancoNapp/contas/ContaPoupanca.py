from BancoNapp.contas.Conta import Conta


class ContaPoupanca(Conta):
   def __init__(self, **kwargs):
      self.limite = kwargs.setdefault('limite', 0)
      super(ContaPoupanca, self).__init__(**kwargs)

   def rendimento_aniversario(self, juros):
      if juros < 0 or juros > 1:
          raise ValueError('Os juros precisam ser entre 0 (0%) e 1 (100%).')
      juros = self.saldo * juros
      self.saldo = self.saldo + juros
      return self.saldo

   def deposito(self, valor):
        """
        Método para realizar depósito.
        Este método suporta somente números maiores que zero.

        Args:
            valor (float ou int): Valor positivo do depósito

        Raises:
            ValueError: Erro ocorre quando é informado valor negativo.
            TypeError: Quando o tipo passado não for inteiro ou float.
        """
        if isinstance(valor, (float, int)):
            if valor <= 0:
                raise ValueError('Valor do depósito precisa ser maior que zero')
            self.saldo = self.saldo + valor
            self.extrato.append(('D', valor))
            return
        raise TypeError('O depósito precisa ser numérico')

   def saque(self, valor):
      """
      Método para realizar saque.
      Este método suporta somente números maiores que zero.

      Args:
         valor (float ou int): Valor positivo do saque

      Raises:
         ValueError: Erro ocorre quando é informado valor negativo.
         TypeError: Quando o tipo passado não for inteiro ou float.

      Returns:
         Float: Valor do saque realizado.
      """
      if isinstance(valor, (float, int)):
         if valor > (self.saldo):
               raise ValueError('Valor do saque supera seu saldo.')
               return
         self.saldo = self.saldo - valor
         self.extrato.append(('S', valor))
         return valor
      raise TypeError('O valor do saque precisa ser numérico')

   def get_extrato(self):
      """
      Retorna a lista dos saques e depósitos feitos na conta.

      Returns:
         List: Lista de operações
      """
      return self.extrato