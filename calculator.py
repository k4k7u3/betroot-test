# 22.04.20 - добавил деление на 0 =)) 
import random
import math

result = 0  # переменная для хранения промежуточного результата
flag = 0	# флаг, для того, что бы мы могли после первой операции производить действия с результатом, а не с новыми числами

name = input("Здравствуйте! Введите свое имя: ")
name = name.strip()
name = name.capitalize()

list_operations = ('+', '-', '*', '/', '//', '%', '**', 'sqrt', 'abs', '!', 'cmd') # 
print(f'{name}, добро пожаловать в калькулятор. Вот список доступных операций: {list_operations}.')

while True:
	if flag == 0:
		operation = input('Выберите какую операцию Вы хотите произвести (для выхода введите "Exit", для описания операций введите "Info"): ')
		operation = operation.strip()
		operation = operation.capitalize()
		if operation == 'Exit':
			break
		elif operation == 'Info':
			print('+' + '\t'*2 + '- сложение;')
			print('-' + '\t'*2 + '- вычитание;')
			print('*' + '\t'*2 + '- умножение;')
			print('/' + '\t'*2 + '- деление;')
			print('//' + '\t'*2 + '- получение целой части от деления;')
			print('%' + '\t'*2 + '- получение остатка от деления;')
			print('**' + '\t'*2 + '- возведение числа в степень;')
			print('sqrt' + '\t' + '- извлечение квадратного корня;')
			print('abs n' + '\t' + '- модуль числа, где n - введеное число;')
			print('!' + '\t'*2 + '- факториал числа, n! - где n введеное число;')
			print('cmd' + '\t'*2 + '- позволяет вводить команду полностью (доступна только одна операция!!!)')
			continue
		elif operation == '+':
			while True:
				input_str = input(f'{name}, введите первое число: ')
				input_str = input_str.strip()
				len_str = len(input_str)
				len_str_cnt = 0
				x = ''
				flag1 = 0
				if len_str == 0:
					flag1 = 2
				else:
					while len_str_cnt != len_str:
						if input_str[len_str_cnt].isdigit() == True:
							x += input_str[len_str_cnt]
						else:
							if input_str[len_str_cnt] == '.':
								x += input_str[len_str_cnt]
							elif input_str[len_str_cnt] == ',':
								print('Дробное число записывается через точку (пример: 10.2)')
								flag1 = 1
								break
							elif input_str[len_str_cnt] == ' ':
								None
							else:
								flag1 = 2
								break
						len_str_cnt += 1
				if flag1 == 0:
					if float(x).is_integer() == True:
						x = int(x)
					else:
						x = float(x)
					break
				elif flag1 == 1:
					continue
				elif flag1 == 2:
					print(f'{name}, Вы ввели некоректное число!')
					continue
			while True:
				input_str = input(f'{name}, введите второе число: ')
				input_str = input_str.strip()    
				len_str = len(input_str)
				len_str_cnt = 0
				y = ''
				flag1 = 0
				if len_str == 0:
					flag1 = 2
				else:
					while len_str_cnt != len_str:
						if input_str[len_str_cnt].isdigit() == True:
							y += input_str[len_str_cnt]
						else:
							if input_str[len_str_cnt] == '.':
								y += input_str[len_str_cnt]
							elif input_str[len_str_cnt] == ',':
								print('Дробное число записывается через точку (пример: 10.2)')
								flag1 = 1
								break
							elif input_str[len_str_cnt] == ' ':
								None
							else:
								flag1 = 2
								break
						len_str_cnt += 1
				if flag1 == 0:
					if float(y).is_integer() == True:
						y = int(y)
					else:
						y = float(y)
					break
				elif flag1 == 1:
					continue
				elif flag1 == 2:
					print(f'{name}, Вы ввели некоректное число!')
					continue
			result = x + y
			result = round(result, 3)
			print(f'Вы ввели x = {x} , y = {y}. Результат {x} {operation} {y} =', result)
			flag = 1
			continue
		elif operation == '-':
			while True:
				input_str = input(f'{name}, введите первое число: ')
				input_str = input_str.strip()
				len_str = len(input_str)
				len_str_cnt = 0
				x = ''
				flag1 = 0
				if len_str == 0:
					flag1 = 2
				else:
					while len_str_cnt != len_str:
						if input_str[len_str_cnt].isdigit() == True:
							x += input_str[len_str_cnt]
						else:
							if input_str[len_str_cnt] == '.':
								x += input_str[len_str_cnt]
							elif input_str[len_str_cnt] == ',':
								print('Дробное число записывается через точку (пример: 10.2)')
								flag1 = 1
								break
							elif input_str[len_str_cnt] == ' ':
								None
							else:
								flag1 = 2
								break
						len_str_cnt += 1
				if flag1 == 0:
					if float(x).is_integer() == True:
						x = int(x)
					else:
						x = float(x)
					break
				elif flag1 == 1:
					continue
				elif flag1 == 2:
					print(f'{name}, Вы ввели некоректное число!')
					continue
			while True:
				input_str = input(f'{name}, введите второе число: ')
				input_str = input_str.strip()
				len_str = len(input_str)
				len_str_cnt = 0
				y = ''
				flag1 = 0
				if len_str == 0:
					flag1 = 2
				else:
					while len_str_cnt != len_str:
						if input_str[len_str_cnt].isdigit() == True:
							y += input_str[len_str_cnt]
						else:
							if input_str[len_str_cnt] == '.':
								y += input_str[len_str_cnt]
							elif input_str[len_str_cnt] == ',':
								print('Дробное число записывается через точку (пример: 10.2)')
								flag1 = 1
								break
							elif input_str[len_str_cnt] == ' ':
								None
							else:
								flag1 = 2
								break
						len_str_cnt += 1
				if flag1 == 0:
					if float(y).is_integer() == True:
						y = int(y)
					else:
						y = float(y)
					break
				elif flag1 == 1:
					continue
				elif flag1 == 2:
					print(f'{name}, Вы ввели некоректное число!')
					continue
			result = x - y
			result = round(result, 3)
			print(f'Вы ввели x = {x} , y = {y}. Результат {x} {operation} {y} =', result)
			flag = 1
			continue
		elif operation == '*':
			while True:
				input_str = input(f'{name}, введите первое число: ')
				input_str = input_str.strip()
				len_str = len(input_str)
				len_str_cnt = 0
				x = ''
				flag1 = 0
				if len_str == 0:
					flag1 = 2
				else:
					while len_str_cnt != len_str:
						if input_str[len_str_cnt].isdigit() == True:
							x += input_str[len_str_cnt]
						else:
							if input_str[len_str_cnt] == '.':
								x += input_str[len_str_cnt]
							elif input_str[len_str_cnt] == ',':
								print('Дробное число записывается через точку (пример: 10.2)')
								flag1 = 1
								break
							elif input_str[len_str_cnt] == ' ':
								None
							else:
								flag1 = 2
								break
						len_str_cnt += 1
				if flag1 == 0:
					if float(x).is_integer() == True:
						x = int(x)
					else:
						x = float(x)
					break
				elif flag1 == 1:
					continue
				elif flag1 == 2:
					print(f'{name}, Вы ввели некоректное число!')
					continue
			while True:
				input_str = input(f'{name}, введите второе число: ')
				input_str = input_str.strip()
				len_str = len(input_str)
				len_str_cnt = 0
				y = ''
				flag1 = 0
				if len_str == 0:
					flag1 = 2
				else:
					while len_str_cnt != len_str:
						if input_str[len_str_cnt].isdigit() == True:
							y += input_str[len_str_cnt]
						else:
							if input_str[len_str_cnt] == '.':
								y += input_str[len_str_cnt]
							elif input_str[len_str_cnt] == ',':
								print('Дробное число записывается через точку (пример: 10.2)')
								flag1 = 1
								break
							elif input_str[len_str_cnt] == ' ':
								None
							else:
								flag1 = 2
								break
						len_str_cnt += 1
				if flag1 == 0:
					if float(y).is_integer() == True:
						y = int(y)
					else:
						y = float(y)
					break
				elif flag1 == 1:
					continue
				elif flag1 == 2:
					print(f'{name}, Вы ввели некоректное число!')
					continue
			result = x * y
			result = round(result, 3)
			print(f'Вы ввели x = {x} , y = {y}. Результат {x} {operation} {y} =', result)
			flag = 1
			continue
		elif operation == '/':
			while True:
				input_str = input(f'{name}, введите первое число: ')
				input_str = input_str.strip()
				len_str = len(input_str)
				len_str_cnt = 0
				x = ''
				flag1 = 0
				if len_str == 0:
					flag1 = 2
				else:
					while len_str_cnt != len_str:
						if input_str[len_str_cnt].isdigit() == True:
							x += input_str[len_str_cnt]
						else:
							if input_str[len_str_cnt] == '.':
								x += input_str[len_str_cnt]
							elif input_str[len_str_cnt] == ',':
								print('Дробное число записывается через точку (пример: 10.2)')
								flag1 = 1
								break
							elif input_str[len_str_cnt] == ' ':
								None
							else:
								flag1 = 2
								break
						len_str_cnt += 1
				if flag1 == 0:
					if float(x).is_integer() == True:
						x = int(x)
					else:
						x = float(x)
					break
				elif flag1 == 1:
					continue
				elif flag1 == 2:
					print(f'{name}, Вы ввели некоректное число!')
					continue					
			while True:
				input_str = input(f'{name}, введите второе число: ')
				input_str = input_str.strip()
				len_str = len(input_str)
				len_str_cnt = 0
				y = ''
				flag1 = 0
				if len_str == 0:
					flag1 = 2
				else:
					while len_str_cnt != len_str:
						if input_str[len_str_cnt].isdigit() == True:
							y += input_str[len_str_cnt]
						else:
							if input_str[len_str_cnt] == '.':
								y += input_str[len_str_cnt]
							elif input_str[len_str_cnt] == ',':
								print('Дробное число записывается через точку (пример: 10.2)')
								flag1 = 1
								break
							elif input_str[len_str_cnt] == ' ':
								None
							else:
								flag1 = 2
								break
						len_str_cnt += 1
				if flag1 == 0:
					if float(y).is_integer() == True:
						y = int(y)
					else:
						y = float(y)
					break
				elif flag1 == 1:
					continue
				elif flag1 == 2:
					print(f'{name}, Вы ввели некоректное число!')
					continue
			if y == 0:
				print(f'{name}, на 0 мы не делим, а умножаем =)) ')
				continue
			result = x / y
			result = round(result, 3)
			print(f'Вы ввели x = {x} , y = {y}. Результат {x} {operation} {y} =', result)
			flag = 1
			continue
		elif operation == '//':
			while True:
				input_str = input(f'{name}, введите первое число: ')
				input_str = input_str.strip()
				len_str = len(input_str)
				len_str_cnt = 0
				x = ''
				flag1 = 0
				if len_str == 0:
					flag1 = 2
				else:
					while len_str_cnt != len_str:
						if input_str[len_str_cnt].isdigit() == True:
							x += input_str[len_str_cnt]
						else:
							if input_str[len_str_cnt] == '.':
								x += input_str[len_str_cnt]
							elif input_str[len_str_cnt] == ',':
								print('Дробное число записывается через точку (пример: 10.2)')
								flag1 = 1
								break
							elif input_str[len_str_cnt] == ' ':
								None
							else:
								flag1 = 2
								break
						len_str_cnt += 1
				if flag1 == 0:
					if float(x).is_integer() == True:
						x = int(x)
					else:
						x = float(x)
					break
				elif flag1 == 1:
					continue
				elif flag1 == 2:
					print(f'{name}, Вы ввели некоректное число!')
					continue
			while True:
				input_str = input(f'{name}, введите второе число: ')
				input_str = input_str.strip()
				len_str = len(input_str)
				len_str_cnt = 0
				y = ''
				flag1 = 0
				if len_str == 0:
					flag1 = 2
				else:
					while len_str_cnt != len_str:
						if input_str[len_str_cnt].isdigit() == True:
							y += input_str[len_str_cnt]
						else:
							if input_str[len_str_cnt] == '.':
								y += input_str[len_str_cnt]
							elif input_str[len_str_cnt] == ',':
								print('Дробное число записывается через точку (пример: 10.2)')
								flag1 = 1
								break
							elif input_str[len_str_cnt] == ' ':
								None
							else:
								flag1 = 2
								break
						len_str_cnt += 1
				if flag1 == 0:
					if float(y).is_integer() == True:
						y = int(y)
					else:
						y = float(y)
					break
				elif flag1 == 1:
					continue
				elif flag1 == 2:
					print(f'{name}, Вы ввели некоректное число!')
					continue
			if y == 0:
				print(f'{name}, на 0 мы не делим, а умножаем =)) ')
				continue
			result = x // y
			result = round(result, 3)
			print(f'Вы ввели x = {x} , y = {y}. Результат {x} {operation} {y} =', result)
			flag = 1
			continue
		elif operation == '%':
			while True:
				input_str = input(f'{name}, введите первое число: ')
				input_str = input_str.strip()
				len_str = len(input_str)
				len_str_cnt = 0
				x = ''
				flag1 = 0
				if len_str == 0:
					flag1 = 2
				else:
					while len_str_cnt != len_str:
						if input_str[len_str_cnt].isdigit() == True:
							x += input_str[len_str_cnt]
						else:
							if input_str[len_str_cnt] == '.':
								x += input_str[len_str_cnt]
							elif input_str[len_str_cnt] == ',':
								print('Дробное число записывается через точку (пример: 10.2)')
								flag1 = 1
								break
							elif input_str[len_str_cnt] == ' ':
								None
							else:
								flag1 = 2
								break
						len_str_cnt += 1
				if flag == 0:
					if float(x).is_integer() == True:
						x = int(x)
					else:
						x = float(x)
					break
				elif flag1 == 1:
					continue
				elif flag1 == 2:
					print(f'{name}, Вы ввели некоректное число!')
					continue
			while True:
				input_str = input(f'{name}, введите второе число: ')
				input_str = input_str.strip()
				len_str = len(input_str)
				len_str_cnt = 0
				y = ''
				flag1 = 0
				if len_str == 0:
					flag1 = 2
				else:
					while len_str_cnt != len_str:
						if input_str[len_str_cnt].isdigit() == True:
							y += input_str[len_str_cnt]
						else:
							if input_str[len_str_cnt] == '.':
								y += input_str[len_str_cnt]
							elif input_str[len_str_cnt] == ',':
								print('Дробное число записывается через точку (пример: 10.2)')
								flag1 = 1
								break
							elif input_str[len_str_cnt] == ' ':
								None
							else:
								flag1 = 2
								break
						len_str_cnt += 1
				if flag1 == 0:
					if float(y).is_integer() == True:
						y = int(y)
					else:
						y = float(y)
					break
				elif flag1 == 1:
					continue
				elif flag1 == 2:
					print(f'{name}, Вы ввели некоректное число!')
					continue
			if y == 0:
				print(f'{name}, на 0 мы не делим, а умножаем =)) ')
				continue
			result = x % y
			result = round(result, 3)
			print(f'Вы ввели x = {x} , y = {y}. Результат {x} {operation} {y} =', result)
			flag = 1
			continue
		elif operation == '**':
			while True:
				input_str = input(f'{name}, введите первое число: ')
				input_str = input_str.strip()
				len_str = len(input_str)
				len_str_cnt = 0
				x = ''
				flag1 = 0
				if len_str == 0:
					flag1 = 2
				else:
					while len_str_cnt != len_str:
						if input_str[len_str_cnt].isdigit() == True:
							x += input_str[len_str_cnt]
						else:
							if input_str[len_str_cnt] == '.':
								x += input_str[len_str_cnt]
							elif input_str[len_str_cnt] == ',':
								print('Дробное число записывается через точку (пример: 10.2)')
								flag1 = 1
								break
							elif input_str[len_str_cnt] == ' ':
								None
							else:
								flag1 = 2
								break
						len_str_cnt += 1
				if flag1 == 0:
					if float(x).is_integer() == True:
						x = int(x)
					else:
						x = float(x)
					break
				elif flag1 == 1:
					continue
				elif flag1 == 2:
					print(f'{name}, Вы ввели некоректное число!')
					continue
			while True:
				input_str = input(f'{name}, введите второе число: ')
				input_str = input_str.strip()
				len_str = len(input_str)
				len_str_cnt = 0
				y = ''
				flag1 = 0
				if len_str == 0:
					flag1 = 2
				else:
					while len_str_cnt != len_str:
						if input_str[len_str_cnt].isdigit() == True:
							y += input_str[len_str_cnt]
						else:
							if input_str[len_str_cnt] == '.':
								y += input_str[len_str_cnt]
							elif input_str[len_str_cnt] == ',':
								print('Дробное число записывается через точку (пример: 10.2)')
								flag1 = 1
								break
							elif input_str[len_str_cnt] == ' ':
								None
							else:
								flag1 = 2
								break
						len_str_cnt += 1
				if flag1 == 0:
					if float(y).is_integer() == True:
						y = int(y)
					else:
						y = float(y)
					break
				elif flag1 == 1:
					continue
				elif flag1 == 2:
					print(f'{name}, Вы ввели некоректное число!')
					continue
			result = x ** y
			result = round(result, 3)
			print(f'Вы ввели x = {x} , y = {y}. Результат {x}^{y} =', result)
			flag = 1
			continue
		elif operation == 'Sqrt':
			while True:
				input_str = input(f'{name}, введите первое число: ')
				input_str = input_str.strip()
				len_str = len(input_str)
				len_str_cnt = 0
				x = ''
				flag1 = 0
				if len_str == 0:
					flag1 = 2
				else:
					while len_str_cnt != len_str:
						if input_str[len_str_cnt].isdigit() == True:
							x += input_str[len_str_cnt]
						else:
							if input_str[len_str_cnt] == '.':
								x += input_str[len_str_cnt]
							elif input_str[len_str_cnt] == ',':
								print('Дробное число записывается через точку (пример: 10.2)')
								flag1 = 1
								break
							elif input_str[len_str_cnt] == ' ':
								None
							else:
								flag1 = 2
								break
						len_str_cnt += 1
				if flag1 == 0:
					if float(x).is_integer() == True:
						x = int(x)
					else:
						x = float(x)
					break
				elif flag1 == 1:
					continue
				elif flag1 == 2:
					print(f'{name}, Вы ввели некоректное число!')
					continue
			result = math.sqrt(x)
			result = round(result, 3)
			print(f'Вы ввели x = {x}. Результат sqrt({x}) =', result)
			flag = 1
			continue
		elif operation == 'Abs':
			while True:
				input_str = input(f'{name}, введите первое число: ')
				input_str = input_str.strip()
				len_str = len(input_str)
				len_str_cnt = 0
				x = ''
				flag1 = 0
				if len_str == 0:
					flag1 = 2
				else:
					while len_str_cnt != len_str:
						if input_str[len_str_cnt].isdigit() == True:
							x += input_str[len_str_cnt]
						else:
							if input_str[len_str_cnt] == '.':
								x += input_str[len_str_cnt]
							elif input_str[len_str_cnt] == ',':
								print('Дробное число записывается через точку (пример: 10.2)')
								flag1 = 1
								break
							elif input_str[len_str_cnt] == ' ':
								None
							else:
								flag1 = 2
								break
						len_str_cnt += 1
				if flag1 == 0:
					if float(x).is_integer() == True:
						x = int(x)
					else:
						x = float(x)
					break
				elif flag1 == 1:
					continue
				elif flag1 == 2:
					print(f'{name}, Вы ввели некоректное число!')
					continue
			result = abs(x)
			result = round(result, 3)
			print(f'Вы ввели x = {x}. Результат abs({x}) =', result)
			flag = 1
			continue
		elif operation == '!':
			while True:
				input_str = input(f'{name}, введите первое число: ')
				input_str = input_str.strip()
				len_str = len(input_str)
				len_str_cnt = 0
				x = ''
				flag = 0
				if len_str == 0:
					flag1 = 2
				else:
					while len_str_cnt != len_str:
						if input_str[len_str_cnt].isdigit() == True:
							x += input_str[len_str_cnt]
						else:
							if input_str[len_str_cnt] == '.':
								x += input_str[len_str_cnt]
							elif input_str[len_str_cnt] == ',':
								print('Дробное число записывается через точку (пример: 10.2)')
								flag1 = 1
								break
							elif input_str[len_str_cnt] == ' ':
								None
							else:
								flag1 = 2
								break
						len_str_cnt += 1
				if flag == 0:
					if float(x).is_integer() == True:
						x = int(x)
					else:
						x = float(x)
					print(x)
					break
				elif flag1 == 1:
					continue
				elif flag1 == 2:
					print(f'{name}, Вы ввели некоректное число!')
					continue
			result = math.factorial(x)
			result = round(result, 3)
			print(f'Вы ввели x = {x}. Результат {x}! =', result)
			flag = 1
			continue
		elif operation == 'Cmd':
			while True:
				input_str = input('Введите операцию полностью (для выхода введите "Exit"): ')
				input_str = input_str.strip()
				len_str = len(input_str)
				len_str_cnt = 0
				in_operation = ''
				x = '0'
				y = '0'
				flag1 = 0
				marker = 0				# Переменная для числа ( всмысле первое число или второе)
				if len_str == 0:
					flag1 = 2
				else: 
					# Цикл сортировки введеных символов на числа и операцию
					while len_str_cnt != len_str:
						if input_str[len_str_cnt].isdigit() == True:
							if marker == 0:
								x += input_str[len_str_cnt]
							else:
								y += input_str[len_str_cnt]
						else:
							if input_str[len_str_cnt] == '.':
								if marker == 0:
									x += input_str[len_str_cnt]
								else:
									y += input_str[len_str_cnt]
							elif input_str[len_str_cnt] == ',':
								print('Дробное число записывается через точку (пример: 10.2)')
								x = '0'
								y = '0'
								in_operation = ''
								flag1 = 1
								break
							elif input_str[len_str_cnt] == ' ':
								None
							else:
								in_operation += input_str[len_str_cnt]
								marker = 1
						len_str_cnt += 1

				if flag1 == 1:
					continue
				x = x.strip()
				y = y.strip()
				in_operation = in_operation.strip()
				in_operation = in_operation.capitalize()

				if float(x).is_integer() == True:
					x = int(x)
				else:
					x = float(x)
				if float(y).is_integer() == True:
					y = int(y)
				else:
					y = float(y)
				# Тут мы уже выбираем операцию ( если такой операции нет или она не одна выдаем сообщение об ошибке)
				if in_operation == '+':
					result = x + y
					result = round(result, 3)
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} {in_operation} {y} =', result)
					flag = 1
					# continue
					break
				elif in_operation == '-':
					result = x - y
					result = round(result, 3)
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} {in_operation} {y} =', result)
					flag = 1
					# continue
					break
				elif in_operation == '*':
					result = x * y
					result = round(result, 3)
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} {in_operation} {y} =', result)
					flag = 1
					# continue
					break
				elif in_operation == '/':
					if y == 0:
						print(f'{name}, на 0 мы не делим, а умножаем =)) ')
						continue
					result = x / y
					result = round(result, 3)
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} {in_operation} {y} =', result)
					flag = 1
					# continue
					break
				elif in_operation == '//':
					if y == 0:
						print(f'{name}, на 0 мы не делим, а умножаем =)) ')
						continue
					result = x // y
					result = round(result, 3)
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} {in_operation} {y} =', result)
					flag = 1
					# continue
					break
				elif in_operation == '%':
					if y == 0:
						print(f'{name}, на 0 мы не делим, а умножаем =)) ')
						continue
					result = x % y
					result = round(result, 3)
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} {in_operation} {y} =', result)
					flag = 1
					# continue
					break
				elif in_operation == '**':
					result = x ** y
					result = round(result, 3)
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} {in_operation} {y} =', result)
					flag = 1
					# continue
					break
				elif in_operation == 'Sqrt':
					x = 0
					result = math.sqrt(y)
					result = round(result, 3)
					print(f'Вы ввели x = {y}. Результат sqrt({y}) =', result)
					flag = 1
					# continue
					break
				elif in_operation == 'Abs':
					x = 0
					result = abs(y)
					result = round(result, 3)
					print(f'Вы ввели x = {y}. Результат abs({y}) =', result)
					flag = 1
					# continue
					break
				elif in_operation == '!':
					y = 0
					result = math.factorial(x)
					result = round(result, 3)
					print(f'Вы ввели x = {x}. Результат {x}! =', result)
					flag = 1
					# continue
					break
				elif in_operation == 'Exit':
					break
				else:
					print( 'Вы ввели некоректную операцию! Повторите пожалуйста.')
					flag = 0
					continue
		else:
			print(f'{name}, Вы ввели некоректную операцию (или она пока неподдерживается)! Повторите пожалуйста.')
			flag = 0
			continue
	else:
		operation = input('Ввести дальнейшую операцию или сбросить? (для cброса введите "clear", для описания операций введите "Info", для выхода введите "Exit"): ')
		operation = operation.strip()
		operation = operation.capitalize()
		if operation == 'Exit':
			break
		elif operation == 'Info':
			print('+' + '\t'*2 + '- сложение;')
			print('-' + '\t'*2 + '- вычитание;')
			print('*' + '\t'*2 + '- умножение;')
			print('/' + '\t'*2 + '- деление;')
			print('//' + '\t'*2 + '- получение целой части от деления;')
			print('%' + '\t'*2 + '- получение остатка от деления;')
			print('**' + '\t'*2 + '- возведение числа в степень;')
			print('sqrt' + '\t' + '- извлечение квадратного корня;')
			print('abs n' + '\t' + '- модуль числа, где n - введеное число;')
			print('!' + '\t'*2 + '- факториал числа, n! - где n введеное число;')
			print('cmd' + '\t'*2 + '- позволяет вводить команду полностью')
			continue
		elif operation == 'Clear':
			result = 0
			flag = 0
			continue
		elif operation == '+':
			while True:
				input_str = input(f'{name}, введите число: ')
				input_str = input_str.strip()
				len_str = len(input_str)
				len_str_cnt = 0
				z = ''
				flag1 = 0
				if len_str == 0:
					flag1 = 2
				else:
					while len_str_cnt != len_str:
						if input_str[len_str_cnt].isdigit() == True:
							z += input_str[len_str_cnt]
						else:
							if input_str[len_str_cnt] == '.':
								z += input_str[len_str_cnt]
							elif input_str[len_str_cnt] == ',':
								print('Дробное число записывается через точку (пример: 10.2)')
								flag = 1
								break
							elif input_str[len_str_cnt] == ' ':
								None
							else:
								flag = 2
								break
						len_str_cnt += 1
				if flag1 == 0:
					if float(z).is_integer() == True:
						z = int(z)
					else:
						z = float(z)
					break
				elif flag1 == 1:
					continue
				elif flag1 == 2:
					print(f'{name}, Вы ввели некоректное число!')
					continue
			result1 = result
			result += z
			result = round(result, 3)
			print(f'Результат {result1} {operation} {z} =', result)
			continue
		elif operation == '-':
			while True:
				input_str = input(f'{name}, введите число: ')
				input_str = input_str.strip()
				len_str = len(input_str)
				len_str_cnt = 0
				z = ''
				flag1 = 0
				if len_str == 0:
					flag1 = 2
				else:
					while len_str_cnt != len_str:
						if input_str[len_str_cnt].isdigit() == True:
							z += input_str[len_str_cnt]
						else:
							if input_str[len_str_cnt] == '.':
								z += input_str[len_str_cnt]
							elif input_str[len_str_cnt] == ',':
								print('Дробное число записывается через точку (пример: 10.2)')
								flag = 1
								break
							elif input_str[len_str_cnt] == ' ':
								None
							else:
								flag = 2
								break
						len_str_cnt += 1
				if flag1 == 0:
					if float(z).is_integer() == True:
						z = int(z)
					else:
						z = float(z)
					break
				elif flag1 == 1:
					continue
				elif flag1 == 2:
					print(f'{name}, Вы ввели некоректное число!')
					continue
			result1 = result
			result -= z
			result = round(result, 3)
			print(f'Результат {result1} {operation} {z} =', result)
			continue
		elif operation == '*':
			while True:
				input_str = input(f'{name}, введите число: ')
				input_str = input_str.strip()
				len_str = len(input_str)
				len_str_cnt = 0
				z = ''
				flag1 = 0
				if len_str == 0:
					flag1 = 2
				else:
					while len_str_cnt != len_str:
						if input_str[len_str_cnt].isdigit() == True:
							z += input_str[len_str_cnt]
						else:
							if input_str[len_str_cnt] == '.':
								z += input_str[len_str_cnt]
							elif input_str[len_str_cnt] == ',':
								print('Дробное число записывается через точку (пример: 10.2)')
								flag = 1
								break
							elif input_str[len_str_cnt] == ' ':
								None
							else:
								flag = 2
								break
						len_str_cnt += 1
				if flag1 == 0:
					if float(z).is_integer() == True:
						z = int(z)
					else:
						z = float(z)
					break
				elif flag1 == 1:
					continue
				elif flag1 == 2:
					print(f'{name}, Вы ввели некоректное число!')
					continue
			result1 = result
			result *= z
			result = round(result, 3)
			print(f'Результат: {result1} {operation} {z} =', result)
			continue
		elif operation == '/':
			while True:
				input_str = input(f'{name}, введите число: ')
				input_str = input_str.strip()
				len_str = len(input_str)
				len_str_cnt = 0
				z = ''
				flag1 = 0
				if len_str == 0:
					flag1 = 2
				else:
					while len_str_cnt != len_str:
						if input_str[len_str_cnt].isdigit() == True:
							z += input_str[len_str_cnt]
						else:
							if input_str[len_str_cnt] == '.':
								z += input_str[len_str_cnt]
							elif input_str[len_str_cnt] == ',':
								print('Дробное число записывается через точку (пример: 10.2)')
								flag = 1
								break
							elif input_str[len_str_cnt] == ' ':
								None
							else:
								flag = 2
								break
						len_str_cnt += 1
				if flag1 == 0:
					if float(z).is_integer() == True:
						z = int(z)
					else:
						z = float(z)
					break
				elif flag1 == 1:
					continue
				elif flag1 == 2:
					print(f'{name}, Вы ввели некоректное число!')
					continue
			if z == 0:
				print(f'{name}, на 0 мы не делим, а умножаем =)) ')
				continue
			result1 = result
			result /= z
			result = round(result, 3)
			print(f'Результат: {result1} {operation} {z} =', result)
			continue
		elif operation == '//':
			while True:
				input_str = input(f'{name}, введите число: ')
				input_str = input_str.strip()
				len_str = len(input_str)
				len_str_cnt = 0
				z = ''
				flag1 = 0
				if len_str == 0:
					flag1 = 2
				else:
					while len_str_cnt != len_str:
						if input_str[len_str_cnt].isdigit() == True:
							z += input_str[len_str_cnt]
						else:
							if input_str[len_str_cnt] == '.':
								z += input_str[len_str_cnt]
							elif input_str[len_str_cnt] == ',':
								print('Дробное число записывается через точку (пример: 10.2)')
								flag = 1
								break
							elif input_str[len_str_cnt] == ' ':
								None
							else:
								flag = 2
								break
						len_str_cnt += 1
				if flag1 == 0:
					if float(z).is_integer() == True:
						z = int(z)
					else:
						z = float(z)
					break
				elif flag1 == 1:
					continue
				elif flag1 == 2:
					print(f'{name}, Вы ввели некоректное число!')
					continue
			if z == 0:
				print(f'{name}, на 0 мы не делим, а умножаем =)) ')
				continue
			result1 = result
			result //= z
			result = round(result, 3)
			print(f'Результат: {result1} {operation} {z} =', result)
			continue
		elif operation == '%':
			while True:
				input_str = input(f'{name}, введите число: ')
				input_str = input_str.strip()
				len_str = len(input_str)
				len_str_cnt = 0
				z = ''
				flag1 = 0
				if len_str == 0:
					flag1 = 2
				else:
					while len_str_cnt != len_str:
						if input_str[len_str_cnt].isdigit() == True:
							z += input_str[len_str_cnt]
						else:
							if input_str[len_str_cnt] == '.':
								z += input_str[len_str_cnt]
							elif input_str[len_str_cnt] == ',':
								print('Дробное число записывается через точку (пример: 10.2)')
								flag = 1
								break
							elif input_str[len_str_cnt] == ' ':
								None
							else:
								flag = 2
								break
						len_str_cnt += 1
				if flag1 == 0:
					if float(z).is_integer() == True:
						z = int(z)
					else:
						z = float(z)
					break
				elif flag1 == 1:
					continue
				elif flag1 == 2:
					print(f'{name}, Вы ввели некоректное число!')
					continue
			if z == 0:
				print(f'{name}, на 0 мы не делим, а умножаем =)) ')
				continue
			result1 = result
			result %= z
			result = round(result, 3)
			print(f'Результат: {result1} {operation} {z} =', result)
			continue
		elif operation == '**':
			while True:
				input_str = input(f'{name}, введите число: ')
				input_str = input_str.strip()
				len_str = len(input_str)
				len_str_cnt = 0
				z = ''
				flag1 = 0
				if len_str == 0:
					flag1 = 2
				else:
					while len_str_cnt != len_str:
						if input_str[len_str_cnt].isdigit() == True:
							z += input_str[len_str_cnt]
						else:
							if input_str[len_str_cnt] == '.':
								z += input_str[len_str_cnt]
							elif input_str[len_str_cnt] == ',':
								print('Дробное число записывается через точку (пример: 10.2)')
								flag = 1
								break
							elif input_str[len_str_cnt] == ' ':
								None
							else:
								flag = 2
								break
						len_str_cnt += 1
				if flag1 == 0:
					if float(z).is_integer() == True:
						z = int(z)
					else:
						z = float(z)
					break
				elif flag1 == 1:
					continue
				elif flag1 == 2:
					print(f'{name}, Вы ввели некоректное число!')
					continue
			result1 = result
			result **= z
			result = round(result, 3)
			print(f'Результат: {result1} {operation} {z} =', result)
			continue
		elif operation == 'Sqrt':
			result1 = result
			result = math.sqrt(result1)
			result = round(result, 3)
			print(f'Результат: sqrt({result1}) =', result)
			continue
		elif operation == 'Abs':
			result1 = result
			result = abs(result)
			result = round(result, 3)
			print(f'Результат: abs({result1}) =', result)
			continue
		elif operation == '!':
			result1 = result
			result = math.factorial(result)
			result = round(result, 3)
			print(f'Результат: {result1}! =', result)
			continue
		elif operation == 'Cmd':
			while True:
				input_str = input(f'Введите операцию которую хотите сделать с результатом (для выхода введите "Exit"): {result} ')
				input_str = input_str.strip()
				len_str = len(input_str)
				len_str_cnt = 0
				in_operation = ''
				y = '0'
				flag1 = 0
				marker = 0				# Переменная для числа ( всмысле первое число или второе)
				if len_str == 0:
					flag1 = 2
				else: 
					# Цикл сортировки введеных символов на числа и операцию
					while len_str_cnt != len_str:
						if input_str[len_str_cnt].isdigit() == True:
							y += input_str[len_str_cnt]
						else:
							if input_str[len_str_cnt] == '.':
									y += input_str[len_str_cnt]
							elif input_str[len_str_cnt] == ',':
								print('Дробное число записывается через точку (пример: 10.2)')
								y = '0'
								in_operation = ''
								flag1 = 1
								break
							elif input_str[len_str_cnt] == ' ':
								None
							else:
								in_operation += input_str[len_str_cnt]
						len_str_cnt += 1
				if flag1 == 1:
					continue
				y = y.strip()
				in_operation = in_operation.strip()
				in_operation = in_operation.capitalize()
				if float(x).is_integer() == True:
					x = int(x)
				else:
					x = float(x)
				if float(y).is_integer() == True:
					y = int(y)
				else:
					y = float(y)
				x = 0
				if in_operation == '+':
					result1 = result
					result += y
					result = round(result, 3)
					print(f'Результат {result1} {in_operation} {y} =', result)
					break
					# continue
				if in_operation == '-':
					result1 = result
					result -= y
					result = round(result, 3)
					print(f'Результат {result1} {in_operation} {y} =', result)
					break
					# continue
				if in_operation == '*':
					result1 = result
					result *= y
					result = round(result, 3)
					print(f'Результат {result1} {in_operation} {y} =', result)
					break
					# continue
				if in_operation == '/':
					if y == 0:
						print(f'{name}, на 0 мы не делим, а умножаем =)) ')
						continue
					result1 = result
					result /= y
					result = round(result, 3)
					print(f'Результат {result1} {in_operation} {y} =', result)
					break
					# continue
				if in_operation == '//':
					if y == 0:
						print(f'{name}, на 0 мы не делим, а умножаем =)) ')
						continue
					result1 = result
					result //= y
					result = round(result, 3)
					print(f'Результат {result1} {in_operation} {y} =', result)
					break
					# continue
				if in_operation == '%':
					if y == 0:
						print(f'{name}, на 0 мы не делим, а умножаем =)) ')
						continue
					result1 = result
					result %= y
					result = round(result, 3)
					print(f'Результат {result1} {in_operation} {y} =', result)
					break
					# continue
				if in_operation == '**':
					result1 = result
					result **= y
					result = round(result, 3)
					print(f'Результат {result1} {in_operation} {y} =', result)
					break
					# continue
				if in_operation == 'Sqrt':
					result1 = result
					result = math.sqrt(result1)
					result = round(result, 3)
					print(f'Результат: sqrt({result1}) =', result)
					break
					# continue
				if in_operation == 'Abs':
					result1 = result
					result = abs(result)
					result = round(result, 3)
					print(f'Результат: abs({result1}) =', result)
					break
					# continue
				if in_operation == '!':
					result1 = result
					result = math.factorial(result)
					result = round(result, 3)
					print(f'Результат: {result1}! =', result)
					break
					# continue
				else:
					print('Вы ввели некоректную операцию! Повторите пожалуйста')
					continue
		else:
			print(f'{name}, Вы ввели некоректную операцию (или она пока неподдерживается)! Повторите пожалуйста.')
			continue
			
print(f'{name}, спасибо, что воспользовались услугами нашего калькулятора! Заходите еще раз!')