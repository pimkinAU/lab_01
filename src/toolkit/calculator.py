from .errors import EmptyString, LetterError, MissedOperand, TwoBinaryOperators, DivisionByZero


# Функция проверки аргумента на соответствие числу

def is_number(n):
	try:
		float(n)
		return True
	except ValueError:
		return False

# Добавление числа в список токенизированных данных

def push(t, d):
	if d != '':
		t.append(d)
		return ''
	else:
		return d

# Функция токенизации переданной строки

def tokenize(exp):
	tokens = []
	i = 0
	# Сборка числа из цифр
	d = ''
	while i < len(exp):
		if exp[i].isspace() or exp[i] == '\t':
			d = push(tokens, d)
		elif exp[i].isdigit() or exp[i] == '.':
			d += exp[i]
		elif exp[i] in '+-/*':
			d = push(tokens, d)
			tokens.append(exp[i])
		else:
			# На этом этапе уже можно отследить попадание букв в исходную строку
			raise LetterError('Букв в строке не может быть')
		i += 1
	d = push(tokens, d)
	return tokens

'''
Функция валидации строки, проверяется отсутствие случаев:
1) Пустая строка
2) Два подряд идущих бинарных оператора
3) Пропуск операнда
4) Деление на ноль
5) Начало строки с бинарного оператора
'''

def validate(exp):
	e = tokenize(exp)
	if len(e) == 0: raise EmptyString('Пустая строка')
	if '---' in "".join(e) or '+++' in "".join(e): raise TwoBinaryOperators('Два бинарных оператора не могут идти подряд')
	state = 'START'
	for i in e:
		match state:
			case 'START':
				if is_number(i):
					state = 'EXPECT_OPERAND'
				elif i in '+-':
					state = 'EXPECT_NUMBER'
				else:
					raise ValueError('Строка не может начаться с бинарной операции')
			case 'EXPECT_OPERAND':
				if i in '+-*/':
					state = 'EXPECT_NUMBER'
				else:
					raise MissedOperand('Пропущен бинарный операнд')
			case 'EXPECT_NUMBER':
				if e[e.index(i)-1]+i == '/0':
					raise DivisionByZero('Деление на ноль запрещено')
				elif is_number(i):
					state = 'EXPECT_OPERAND'
				elif i in '+-':
					pass
				else:
					raise TwoBinaryOperators('Два бинарных оператора не могут идти подряд')

# Функция сращивания унарного минуса с числом

def unary(exp):
	e = tokenize(exp)
	if e[0] == '+':
		e.pop(0)
	if e[0] == '-':
		e[1] = f'-{e[1]}'
		e.pop(0)
	i = 1
	while i < len(e)-1:
		if not is_number(e[i]) and not is_number(e[i+1]) and is_number(e[i+2]):
			e[i+2] = e[i+1] + e[i+2]
			e.pop(i+1)
		else:
			i += 1
	return e

# Функция вычисления токенизированного выражения с учетом приоритета операций * и /

def calculate(exp):
	validate(exp)
	e = unary(exp)
	while '*' in e or '/' in e:
		if '*' in e:
			i = e.index('*')
			e[i-1:i+2] = [float(e[i-1])*float(e[i+1])]
		else:
			i = e.index('/')
			e[i-1:i+2] = [float(e[i-1])/float(e[i+1])]
	k = 0
	while k < len(e):
		match e[k]:
			case '+':
				e[k-1:k+2] = [float(e[k-1])+float(e[k+1])]
			case '-':
				e[k-1:k+2] = [float(e[k-1])-float(e[k+1])]
			case _:
				k += 1
	return float(e[0])



	
	


