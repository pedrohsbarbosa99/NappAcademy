from produtos.classes.Produtos import CocaCola, Pepsi, GuaranaAntartica, Dolly
from produtos.classes.Caracteristicas import (
    Tamanho600ml,
    Tamanho1litro,
    Tamanho2litros,
    Tamanho3litros,
)


def client_code(produto):
    print(produto.operation())


if __name__ == "__main__":
    caracteristicas = [
        Tamanho600ml(),
        Tamanho1litro(),
        Tamanho2litros(),
        Tamanho3litros(),
    ]

    for c in caracteristicas:
        produto = CocaCola(c)
        client_code(produto)

    for c in caracteristicas:
        produto = Pepsi(c)
        client_code(produto)

    for c in caracteristicas:
        produto = GuaranaAntartica(c)
        client_code(produto)

    for c in caracteristicas:
        produto = Dolly(c)
        client_code(produto)
