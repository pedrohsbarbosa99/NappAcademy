import unittest
from exercicio08 import juros_compostos


class CalculoJurosCompostosTestCase(unittest.TestCase):
    def test_calculo_juros_cenario_1(self):
        self.assertEqual(259.38, juros_compostos(100, 10, 10))
        self.assertNotEqual(259.38, juros_compostos(100, 10, 10))

    def test_calculo_juros_cenario_2(self):
        self.assertEqual(259.37, juros_compostos(100, 10, '10'))
        self.assertEqual(259.37, juros_compostos('100', '10', '10'))

    def test_wrong_cenario_1(self):
        with self.assertRaises(ValueError):
            juros_compostos(1, 'a', 10)
