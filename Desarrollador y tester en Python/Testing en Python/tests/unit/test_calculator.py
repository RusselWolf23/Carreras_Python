import unittest

from Calculadora.calculadora import calculadora

class TestCalculator(unittest.TestCase):
    
    def setUp(self)->None:
        self.calculadora=Calculadora()

    def test_operation_is_working_fine(self):
        result=self.calculadora.calcular(1,"+",4)
        self.assertEqual(result, "1+4=5")
