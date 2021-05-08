from BancoNapp.contas.Conta import Conta


class ContaPessoaJuridica(Conta):
    def __init__(self, **kwargs):
        self.limite = kwargs.setdefault('limite', 1500)
        super(ContaPessoaJuridica, self).__init__(**kwargs)
