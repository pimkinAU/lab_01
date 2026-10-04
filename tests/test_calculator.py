import pytest

from toolkit.calculator import calculate
from toolkit.errors import EmptyString, LetterError, MissedOperand, TwoBinaryOperators, DivisionByZero


class TestCalculator:
	# Тесты на проверку корректной работы калькулятора
	def test_add(self):
		assert calculate("2+2") == 4
	def test_minus(self):
		assert calculate("2-3") == -1
	def test_prior(self):
		assert calculate("2-4*10") == -38
	def test_div(self):
		assert calculate("10+100/2") == 60
	def test_unary(self):
		assert calculate("-5") == -5
	def test_unary_minus_after_multi(self):
		assert calculate("2 * -3") == -6
	def test_spaces(self):
		assert calculate('2   + 3') == 5
	def test_mixed_operators(self):
		assert calculate('10 - 2 * 3 + 4') == 8
	# Негативные тесты корректности работы калькулятора
	def test_dev_by_zero(self):
		with pytest.raises(DivisionByZero):
			calculate("5 / 0")
	def test_empty(self):
		with pytest.raises(EmptyString):
			calculate("")
	def test_double_bin(self):
		with pytest.raises(TwoBinaryOperators):
			calculate("5 + * 3")
	def test_missed_operand(self):
		with pytest.raises(MissedOperand):
			calculate("5 3")
	def test_letter(self):
		with pytest.raises(LetterError):
			calculate("5a+1")
	
