import pytest
from exercicio07 import calculo_porcentagem_entre_0_e_100

def test_calculo_porcentagem_entre_0_e_100_cenario_1():
    assert calculo_porcentagem_entre_0_e_100(10, 10) == 1.0

def test_calculo_porcentagem_entre_0_e_100_cenario_2():
    with pytest.raises(ValueError) as error:
        calculo_porcentagem_entre_0_e_100(10, 200)
    assert str(error.value) == 'Porcentagem precisa estar entre 0 e 100'

def test_calculo_porcentagem_entre_0_e_100_cenario_3():
    with pytest.raises(ValueError) as error:
        calculo_porcentagem_entre_0_e_100(1, -80)
    assert str(error.value) == 'Porcentagem precisa estar entre 0 e 100'