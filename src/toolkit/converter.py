from .calculator import is_number
from .errors import DiffUnits, LetterError, MTemp, UnknownUnit

# Доступные единицы измерения

distance = ['mm', 'cm', 'm', 'km']
weight = ['g', 'kg']
temp = ['c', 'f', 'k']

'''
Функция валидации строки, проверяется отсутствие случаев:
1) Неизвестная единица измерения
2) Наличие букв
3) Несовместимые единицы измерения
4) Абсолютная температура ниже 0
'''

def validate(exp, fromU, toU):
	vse = distance+weight+temp
	if fromU not in vse or toU not in vse:
		raise UnknownUnit('Передана неизвестная единица измерения')
	if not is_number(exp):
		raise LetterError('Букв не может быть')
	if not((fromU in distance and toU in distance) or (fromU in weight and toU in weight) or (fromU in temp and toU in temp)):
		raise DiffUnits('Несовместимые единицы измерения')
	match fromU:
		case 'c':
			if float(exp) < -273.15:
				raise MTemp('Абсолютная температура не может быть ниже нуля')
		case 'k':
			if float(exp) < 0:
				raise MTemp('Абсолютная температура не может быть ниже нуля')
		case 'f':
			if float(exp) < -459.67:
				raise MTemp('Абсолютная температура не может быть ниже нуля')

# Двойные функции перевода из одной единицы в другую. Реализованы с помощью степени (1, -1)

# Температура

def kTc(exp, a):
	match a:
		case 'k|c':
			return exp-273.15
		case 'c|k':
			return exp+273.15

def kTf(exp, a):
	match a:
		case 'f|k':
			return (exp-32)*(5/9)+273.15
		case 'k|f':
			return (exp-273.15)/(5/9)+32

def cTf(exp, a):
	match a:
		case 'c|f':
			return exp/(5/9)+32
		case 'f|c':
			return (exp-32)*(5/9)

# Масса

def gTkg(exp, a):
	return exp*1000**a

# Расстояние

def mmTcm(exp, a):
	return exp*10**a

def mmTm(exp, a):
	return exp*1000**a

def mmTkm(exp, a):
	return exp*10**(6*a)

def cmTm(exp, a):
	return exp*100**a

def cmTkm(exp, a):
	return exp*(10**5*a)

def mTkm(exp, a):
	return exp*1000**a

# Функция конвертации единиц

def convert(exp, fromU, toU):
	# Выполнение валидации строки
	validate(exp, fromU, toU)
	exp = float(exp)
	u = f'{fromU}|{toU}'
	# Всевозможные случаи перевода единиц
	match u:
		case 'kg|g':
			return gTkg(exp, 1)
		case 'g|kg':
			return gTkg(exp, -1)
		case 'k|c':
			return kTc(exp, u)
		case 'c|k':
			return kTc(exp, u)
		case 'k|f':
			return kTf(exp, u)
		case 'f|k':
			return kTf(exp, u)
		case 'c|f':
			return cTf(exp, u)
		case 'f|c':
			return cTf(exp, u)
		case 'k|k':
			return exp
		case 'c|c':
			return exp
		case 'f|f':
			return exp
		case 'mm|mm':
			return exp
		case 'mm|cm':
			return mmTcm(exp, -1)
		case 'mm|m':
			return mmTm(exp, -1)
		case 'mm|km':
			return mmTkm(exp, -1)
		case 'cm|mm':
			return mmTcm(exp, 1)
		case 'cm|cm':
			return exp
		case 'cm|m':
			return cmTm(exp, -1)
		case 'cm|km':
			return cmTkm(exp, -1)
		case 'm|mm':
			return mmTm(exp, 1)
		case 'm|cm':
			return cmTm(exp, 1)
		case 'm|m':
			return exp
		case 'm|km':
			return mTkm(exp, -1)
		case 'km|mm':
			return mmTkm(exp, 1)
		case 'km|cm':
			return cmTkm(exp, 1)
		case 'km|m':
			return mTkm(exp, 1)
		case 'km|km':
			return exp

