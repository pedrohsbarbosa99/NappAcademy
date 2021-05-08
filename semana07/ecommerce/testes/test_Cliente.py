from ecommerce.classes.Cliente import Cliente


class TestClient:
    def test_class_declared(self):
        objeto = Cliente('John Doe')
        assert isinstance(objeto, Cliente)

    def test_instanciar_objeto(self):
        objeto = Cliente('Jose da Silva')
        assert objeto.nome, 'Jose da Silva'

    def test_setter(self):
        objeto = Cliente('Jose da Silva')
        assert objeto.nome == 'Jose da Silva'
        objeto.nome = 'Jose da Silva Junior'
        assert objeto.nome == 'Jose da Silva Junior'

    def test_str_repr(self):
        cliente = Cliente('Jose da Silva')
        assert str(cliente) == 'Jose da Silva'
        assert repr(cliente) == 'Cliente => Jose da Silva'
