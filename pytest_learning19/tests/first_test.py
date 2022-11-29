import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_div_calculate_correctly(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_sub_calculate_correctly(self):
        assert self.calc.subtraction(self, 10, 2) == 8

    def test_add_calculate_correctly(self):
        assert self.calc.adding(self, 10, 2) == 12