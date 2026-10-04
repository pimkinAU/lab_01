import pytest

from toolkit.converter import convert
from toolkit.errors import DiffUnits, LetterError, UnknownUnit

class TestConverter:
	# Тесты на корректность работы конвертера
	def test_km_to_m(self):
		assert convert(1, "km", "m") == 1000.0
	def test_m_to_km(self):
		assert convert(1000, "m", "km") == 1.0
	def test_m_to_cm(self):
		assert convert(2, "m", "cm") == 200.0
	def test_cm_to_m(self):
		assert convert(300, "cm", "m") == 3.0
	def test_same_unit(self):
		assert convert(5, "m", "m") == 5.0
	# Негативные тесты для отработки ошибочных случаев
	def test_unknown_from_unit(self):
		with pytest.raises(UnknownUnit):
			convert(10, "abc", "m")
	def test_unknown_to_unit(self):
		with pytest.raises(UnknownUnit):
			convert(10, "m", "abc")
	def test_incompatible_units(self):
		with pytest.raises(DiffUnits):
			convert(10, "kg", "m")
	def test_invalid_value(self):
		with pytest.raises(LetterError):
			convert("abc", "m", "cm")
	def test_empty_unit(self):
		with pytest.raises(UnknownUnit):
			convert(10, "", "m")