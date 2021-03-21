from ecommerce.classes.Ecommerce import Loja
from ecommerce.classes.Pedido import Pedido
from ecommerce.classes.Cliente import Cliente
import pytest

class TestEcommerce:
    def test_class_declared(self):
        objeto = Loja('Lojao Tabajara')
        assert isinstance(objeto, Loja)
    
    def test_instanciar(self):
        objeto = Loja('Lojao Tabajara')
        assert objeto.nome, 'Lojao Tabajara'

    def test_setter(self):
        objeto = Loja('Lojao Tabajara')
        assert objeto.nome == 'Lojao Tabajara'
        objeto.nome = 'Lojao Tabajara Centro'
        assert objeto.nome == 'Lojao Tabajara Centro'
        assert objeto.estoque == []

    def test_str_repr(self):
        objeto = Loja('Lojao Tabajara')
        assert str(objeto) == 'Lojao Tabajara'
        assert repr(objeto) == 'Nome da Loja => Lojao Tabajara'
    
    def test_metodo_add_estoque_ok(self):
        loja = Loja('Lojao Tabajara')
        loja.add_estoque('12345678911', 15, 1)
        assert len(loja.estoque) == 1
    
    def test_metodo_add_estoque_ok2(self):
        loja = Loja('Lojao Tabajara')
        loja.add_estoque('12345678911', 15, 3)
        loja.add_estoque('123', 15, 5)
        assert len(loja.estoque) == 8
    
    def test_quantidade_produtos(self):
        loja = Loja('Lojao Tabajara')
        loja.add_estoque('123', 15, 10)
        loja.add_estoque('1234', 20, 5)
        loja.add_estoque('1235', 20, -1)
        loja.add_estoque('123456', 20, 0)
        assert loja.quantidade_produtos('123') == 10
        assert loja.quantidade_produtos('1234') == 5
        assert loja.quantidade_produtos('12345') == 0
        assert loja.quantidade_produtos('123456') == 0
    
    def test_metodo_comprar_ok(self):
        loja = Loja('Lojao Tabajara')
        loja.add_estoque('123', 15, 3)
        assert len(loja.estoque) == 3
        loja.comprar('123')
        assert len(loja.estoque) == 2
    
    def test_metodo_comprar_sem_produto(self):
        loja = Loja('Lojao Tabajara') 
        assert loja.comprar('9999999999') is None
    
    def test_devolver_carrinho(self):
        loja = Loja('Lojao Tabajara')
        loja.add_estoque('123', 15, 10)
        loja.add_estoque('1234', 20, 5)
        assert len(loja.estoque) == 15
        cliente = Cliente('John Doe')
        pedido = Pedido(cliente)
        pedido.add_item(loja.comprar('1234'))
        pedido.add_item(loja.comprar('123'))
        assert len(pedido.itens) == 2
        assert len(loja.estoque) == 13
        assert loja.quantidade_produtos('1234') == 4
        assert loja.quantidade_produtos('123') == 9
        loja.devolver_carrinho(pedido)
        assert len(pedido.itens) == 0
        assert len(loja.estoque) == 15
