import unittest
from exercicio06 import calculo_porcentagem_entre_0_e_1

class CalculoPorcentagemTestCase(unittest.TestCase):
    def test_calculo_porcetagem_cenario_1(self):
        self.assertEqual(8, calculo_porcentagem_entre_0_e_1(10, 0.8))
        self.assertNotEqual(9, calculo_porcentagem_entre_0_e_1(10, 0.8))

    def test_calculo_porcetagem_cenario_2(self):
        with self.assertRaises(ValueError):
            calculo_porcentagem_entre_0_e_1(10, 1.1)
        with self.assertRaises(ValueError):
            calculo_porcentagem_entre_0_e_1(10, -0.1)
        with self.assertRaises(TypeError):
            calculo_porcentagem_entre_0_e_1(1, '0.8')


if __name__ == '__main__':
    unittest.main()