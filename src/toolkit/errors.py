# Класс всех ошибок
class WholeErrors(Exception):
	pass
# Ошибка деления на ноль
class DivisionByZero(WholeErrors):
	pass
# Передано 0 аргументов
class ZeroArguments(WholeErrors):
	pass
# Два бинарных оператора идут подряд
class TwoBinaryOperators(WholeErrors):
	pass
# Передана пустая строка
class EmptyString(WholeErrors):
	pass
# Пропущен оператор
class MissedOperand(WholeErrors):
	pass
# Передана буква
class LetterError(WholeErrors):
	pass
# Несовместимые единицы измерения
class DiffUnits(WholeErrors):
	pass
# Абсолютная температура ниже 0
class MTemp(WholeErrors):
	pass
# Неизвестная единица измерения
class UnknownUnit(WholeErrors):
	pass
# Не хватает аргумента
class MissingArgumentError(WholeErrors):
	pass
# Передан лишний аргумент
class ExtraArgumentError(WholeErrors):
	pass