from rh.classes.Departamento import Departamento
from datetime import date, timedelta


class TestDepartamento:
    def test_class_declared(self):
        objeto = Departamento('Departamento XYZ', 'Jose', 1, 1, 1990)
        assert isinstance(objeto, Departamento)

    def test_instanciar(self):
        objeto = Departamento('Departamento XYZ', 'Jose', 1, 1, 1990)
        assert objeto.nome_setor == 'Departamento XYZ'
        assert objeto.responsavel == 'Jose'

    def test_str_repr(self):
        objeto = Departamento('Departamento XYZ', 'Jose', 1, 1, 1990)
        assert str(objeto) == 'Departamento XYZ'
        assert repr(objeto) == 'Departamento = Departamento XYZ'

    def test_setters(self):
        objeto = Departamento('Curadoria', 'Jose', 1, 1, 1990)
        assert objeto.nome_setor == 'Curadoria'
        objeto.nome_setor = 'ETL'
        assert objeto.nome_setor == 'ETL'

    def test_properties(self):
        objeto = Departamento('Departamento XYZ', 'Jose', 1, 1, 1990)
        assert objeto.nome_setor == 'Departamento XYZ'

    def test_responsavel(self):
        departamento = Departamento('Departamento XYZ', 'Jose', 5, 2, 1990)
        assert departamento.responsavel is 'Jose'
        departamento.informar_responsavel('Jose', 1, 1, 1990)
        assert departamento.responsavel == 'Jose'

    def test_responsavel_substituido(self):
        departamento = Departamento('Departamento XYZ', 'Jose', 1, 1, 1990)
        assert departamento.responsavel is 'Jose'
        departamento.informar_responsavel('Jose', 1, 1, 1990)
        assert departamento.responsavel == 'Jose'
        departamento.informar_responsavel('Joao Oliveira', 1, 1, 1990)
        assert departamento.responsavel == 'Joao Oliveira'

    def test_add_colaborador(self):
        departamento = Departamento('Departamento XYZ', 'Jose', 1, 1, 1990)
        departamento.informar_responsavel('Jose', 1, 1, 1990)
        departamento.add_colaborador('Joao Oliveira', 18, 3, 1992)
        departamento.add_colaborador('Pedro Mendonça', 18, 4, 1993)
        assert len(departamento.colaboradores) == 2

    def test_verificar_aniversariantes(self):
        retorno = [('Joao Oliveira', '1992-03-27', 'Departamento XYZ'),
                   ('Luis Fernando', '2000-03-27', 'Departamento XYZ'),
                   ('Jose', '1990-03-27', 'Departamento XYZ')]
        dt1 = date.today() - timedelta(days=4)
        hoje = date.today()
        depto = Departamento('Departamento XYZ', 'Jose', 1, 1, 1990)
        depto.informar_responsavel('Jose', hoje.day, hoje.month, 1990)
        depto.add_colaborador('Joao Oliveira', hoje.day, hoje.month, 1992)
        depto.add_colaborador('Pedro Mendonça', dt1.day, dt1.month, 1993)
        depto.add_colaborador('Luis Fernando', hoje.day, hoje.month, 2000)
        depto.add_colaborador('Maurício Souza', dt1.day, dt1.month, 1085)
        aniversariantes = depto.verificar_aniversariantes()
        assert aniversariantes == retorno
        assert len(aniversariantes) == 3
        assert len(aniversariantes[0]) == 3
        assert type(aniversariantes[0]) == tuple
        assert type(aniversariantes) == list