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
			x = input(f'{name}, введите первое число: ')
			x = x.strip()
			while x.isdigit() == False:
				x = input(f'{name}, Вы должны ввести только число. Повторите попытку: ')
			if float(x).is_integer() == True:
				x = int(x)
			else:
				x = float(x)
			y = input(f'{name}, введите второе число: ')
			y = y.strip()
			while y.isdigit() == False:
				y = input(f'{name}, Вы должны ввести только число. Повторите попытку: ')
			if float(y).is_integer() == True:
				y = int(y)
			else:
				y = float(y)
			result = x + y
			print(f'Вы ввели x = {x} , y = {y}. Результат {x} {operation} {y} =', result)
			flag = 1
			continue
		elif operation == '-':
			x = input(f'{name}, введите первое число: ')
			x = x.strip()
			while x.isdigit() == False:
				x = input(f'{name}, Вы должны ввести только число. Повторите попытку: ')
			if float(x).is_integer() == True:
				x = int(x)
			else:
				x = float(x)
			y = input(f'{name}, введите второе число: ')
			y = y.strip()
			while y.isdigit() == False:
				y = input(f'{name}, Вы должны ввести только число. Повторите попытку: ')
			if float(y).is_integer() == True:
				y = int(y)
			else:
				y = float(y)
			result = x - y
			print(f'Вы ввели x = {x} , y = {y}. Результат {x} {operation} {y} =', result)
			flag = 1
			continue
		elif operation == '*':
			x = input(f'{name}, введите первое число: ')
			x = x.strip()
			while x.isdigit() == False:
				x = input(f'{name}, Вы должны ввести только число. Повторите попытку: ')
			if float(x).is_integer() == True:
				x = int(x)
			else:
				x = float(x)
			y = input(f'{name}, введите второе число: ')
			y = y.strip()
			while y.isdigit() == False:
				y = input(f'{name}, Вы должны ввести только число. Повторите попытку: ')
			if float(y).is_integer() == True:
				y = int(y)
			else:
				y = float(y)
			result = x * y
			print(f'Вы ввели x = {x} , y = {y}. Результат {x} {operation} {y} =', result)
			flag = 1
			continue
		elif operation == '/':
			x = input(f'{name}, введите первое число: ')
			x = x.strip()
			while x.isdigit() == False:
				x = input(f'{name}, Вы должны ввести только число. Повторите попытку: ')
			if float(x).is_integer() == True:
				x = int(x)
			else:
				x = float(x)
			y = input(f'{name}, введите второе число: ')
			y = y.strip()
			while y.isdigit() == False:
				y = input(f'{name}, Вы должны ввести только число. Повторите попытку: ')
			if float(y).is_integer() == True:
				y = int(y)
			else:
				y = float(y)
			result = x / y
			print(f'Вы ввели x = {x} , y = {y}. Результат {x} {operation} {y} =', result)
			flag = 1
			continue
		elif operation == '//':
			x = input(f'{name}, введите первое число: ')
			x = x.strip()
			while x.isdigit() == False:
				x = input(f'{name}, Вы должны ввести только число. Повторите попытку: ')
			if float(x).is_integer() == True:
				x = int(x)
			else:
				x = float(x)
			y = input(f'{name}, введите второе число: ')
			y = y.strip()
			while y.isdigit() == False:
				y = input(f'{name}, Вы должны ввести только число. Повторите попытку: ')
			if float(y).is_integer() == True:
				y = int(y)
			else:
				y = float(y)
			result = x // y
			print(f'Вы ввели x = {x} , y = {y}. Результат {x} {operation} {y} =', result)
			flag = 1
			continue
		elif operation == '%':
			x = input(f'{name}, введите первое число: ')
			x = x.strip()
			while x.isdigit() == False:
				x = input(f'{name}, Вы должны ввести только число. Повторите попытку: ')
			if float(x).is_integer() == True:
				x = int(x)
			else:
				x = float(x)
			y = input(f'{name}, введите второе число: ')
			y = y.strip()
			while y.isdigit() == False:
				y = input(f'{name}, Вы должны ввести только число. Повторите попытку: ')
			if float(y).is_integer() == True:
				y = int(y)
			else:
				y = float(y)
			result = x % y
			print(f'Вы ввели x = {x} , y = {y}. Результат {x} {operation} {y} =', result)
			flag = 1
			continue
		elif operation == '**':
			x = input(f'{name}, введите число: ')
			x = x.strip()
			while x.isdigit() == False:
				x = input(f'{name}, Вы должны ввести только число. Повторите попытку: ')
			if float(x).is_integer() == True:
				x = int(x)
			else:
				x = float(x)
			y = input(f'{name}, введите степень: ')
			y = y.strip()
			while y.isdigit() == False:
				y = input(f'{name}, Вы должны ввести только число. Повторите попытку: ')
			if float(y).is_integer() == True:
				y = int(y)
			else:
				y = float(y)
			result = x ** y
			print(f'Вы ввели x = {x} , y = {y}. Результат {x}^{y} =', result)
			flag = 1
			continue
		elif operation == 'Sqrt':
			x = input(f'{name}, введите число: ')
			x = x.strip()
			while x.isdigit() == False:
				x = input(f'{name}, Вы должны ввести только число. Повторите попытку: ')
			if float(x).is_integer() == True:
				x = int(x)
			else:
				x = float(x)
			result = math.sqrt(x)
			print(f'Вы ввели x = {x}. Результат sqrt({x}) =', result)
			flag = 1
			continue
		elif operation == 'Abs':
			x = input(f'{name}, введите число: ')
			x = x.strip()
			while x.isdigit() == False:
				x = input(f'{name}, Вы должны ввести только число. Повторите попытку: ')
			if float(x).is_integer() == True:
				x = int(x)
			else:
				x = float(x)
			result = abs(x)
			print(f'Вы ввели x = {x}. Результат abs({x}) =', result)
			flag = 1
			continue
		elif operation == '!':
			x = input(f'{name}, введите число: ')
			x = x.strip()
			while x.isdigit() == False:
				x = input(f'{name}, Вы должны ввести только число. Повторите попытку: ')
			if float(x).is_integer() == True:
				x = int(x)
			else:
				x = float(x)
			result = math.factorial(x)
			print(f'Вы ввели x = {x}. Результат {x}! =', result)
			flag = 1
			continue
		elif operation == 'Cmd':
			while True:
				input_str = input('Введите операцию полностью (для выхода введите "Exit"): ')
				len_str = len(input_str)
				len_str_cnt = 0
				in_operation = ''
				x = '0'
				y = '0'
				marker = 0				# Переменная для числа ( всмысле первое число или второе) 
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
							break
						else:
							in_operation += input_str[len_str_cnt]
							marker = 1
					len_str_cnt += 1

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
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} {in_operation} {y} =', result)
					flag = 1
					# continue
					break
				elif in_operation == '-':
					result = x - y
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} {in_operation} {y} =', result)
					flag = 1
					# continue
					break
				elif in_operation == '*':
					result = x * y
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} {in_operation} {y} =', result)
					flag = 1
					# continue
					break
				elif in_operation == '/':
					result = x / y
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} {in_operation} {y} =', result)
					flag = 1
					# continue
					break
				elif in_operation == '//':
					result = x // y
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} {in_operation} {y} =', result)
					flag = 1
					# continue
					break
				elif in_operation == '%':
					result = x % y
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} {in_operation} {y} =', result)
					flag = 1
					# continue
					break
				elif in_operation == '**':
					result = x ** y
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} {in_operation} {y} =', result)
					flag = 1
					# continue
					break
				elif in_operation == 'Sqrt':
					x = 0
					result = math.sqrt(y)
					print(f'Вы ввели x = {y}. Результат sqrt({y}) =', result)
					flag = 1
					# continue
					break
				elif in_operation == 'Abs':
					x = 0
					result = abs(y)
					print(f'Вы ввели x = {y}. Результат abs({y}) =', result)
					flag = 1
					# continue
					break
				elif in_operation == '!':
					y = 0
					result = math.factorial(x)
					print(f'Вы ввели x = {x}. Результат {x}! =', result)
					flag = 1
					# continue
					break
				elif in_operation == 'Exit':
					break
				else:
					print( 'Вы ввели некоректную операцию! Повторите пожалуйста.')
					flag = 0
					# continue
					break
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
			z = input(f'{name}, введите число: ')
			z= z.strip()
			while z.isdigit() == False:
				z = input(f'{name}, Вы должны ввести только число. Повторите попытку: ')
			if float(z).is_integer() == True:
				z = int(z)
			else:
				z = float(z)
			result1 = result
			result += z
			print(f'Результат {result1} {operation} {z} =', result)
			continue
		elif operation == '-':
			z = input(f'{name}, введите число: ')
			z= z.strip()
			while z.isdigit() == False:
				z = input(f'{name}, Вы должны ввести только число. Повторите попытку: ')
			if float(z).is_integer() == True:
				z = int(z)
			else:
				z = float(z)
			result1 = result
			result -= z
			print(f'Результат {result1} {operation} {z} =', result)
			continue
		elif operation == '*':
			z = input(f'{name}, введите число: ')
			z= z.strip()
			while z.isdigit() == False:
				z = input(f'{name}, Вы должны ввести только число. Повторите попытку: ')
			if float(z).is_integer() == True:
				z = int(z)
			else:
				z = float(z)
			result1 = result
			result *= z
			print(f'Результат: {result1} {operation} {z} =', result)
			continue
		elif operation == '/':
			z = input(f'{name}, введите число: ')
			z= z.strip()
			while z.isdigit() == False:
				z = input(f'{name}, Вы должны ввести только число. Повторите попытку: ')
			if float(z).is_integer() == True:
				z = int(z)
			else:
				z = float(z)
			result1 = result
			result /= z
			print(f'Результат: {result1} {operation} {z} =', result)
			continue
		elif operation == '//':
			z = input(f'{name}, введите число: ')
			z= z.strip()
			while z.isdigit() == False:
				z = input(f'{name}, Вы должны ввести только число. Повторите попытку: ')
			if float(z).is_integer() == True:
				z = int(z)
			else:
				z = float(z)
			result1 = result
			result //= z
			print(f'Результат: {result1} {operation} {z} =', result)
			continue
		elif operation == '%':
			z = input(f'{name}, введите число: ')
			z= z.strip()
			while z.isdigit() == False:
				z = input(f'{name}, Вы должны ввести только число. Повторите попытку: ')
			if float(z).is_integer() == True:
				z = int(z)
			else:
				z = float(z)
			result1 = result
			result %= z
			print(f'Результат: {result1} {operation} {z} =', result)
			continue
		elif operation == '**':
			z = input(f'{name}, введите число: ')
			while z.isdigit() == False:
				z = input(f'{name}, Вы должны ввести только число. Повторите попытку: ')
			if float(z).is_integer() == True:
				z = int(z)
			else:
				z = float(z)
			result1 = result
			result **= z
			print(f'Результат: {result1} {operation} {z} =', result)
			continue
		elif operation == 'Sqrt':
			result1 = result
			result = math.sqrt(result1)
			print(f'Результат: sqrt({result1}) =', result)
			continue
		elif operation == 'Abs':
			result1 = result
			result = abs(result)
			print(f'Результат: abs({result1}) =', result)
			continue
		elif operation == '!':
			result1 = result
			result = math.factorial(result)
			print(f'Результат: {result1}! =', result)
			continue
		elif operation == 'Cmd':
			input_str = input(f'Введите операцию которую хотите сделать с результатом (для выхода введите "Exit"): {result}')
			len_str = len(input_str)
			len_str_cnt = 0
			in_operation = ''
			y = '0'
			marker = 0				# Переменная для числа ( всмысле первое число или второе) 
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
						break
					else:
						in_operation += input_str[len_str_cnt]
				len_str_cnt += 1

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
				print(f'Результат {result1} {in_operation} {y} =', result)
				continue
			if in_operation == '-':
				result1 = result
				result -= y
				print(f'Результат {result1} {in_operation} {y} =', result)
				continue
			if in_operation == '*':
				result1 = result
				result *= y
				print(f'Результат {result1} {in_operation} {y} =', result)
				continue
			if in_operation == '/':
				result1 = result
				result /= y
				print(f'Результат {result1} {in_operation} {y} =', result)
				continue
			if in_operation == '//':
				result1 = result
				result //= y
				print(f'Результат {result1} {in_operation} {y} =', result)
				continue
			if in_operation == '%':
				result1 = result
				result %= y
				print(f'Результат {result1} {in_operation} {y} =', result)
				continue
			if in_operation == '**':
				result1 = result
				result **= y
				print(f'Результат {result1} {in_operation} {y} =', result)
				continue
			if in_operation == 'Sqrt':
				result1 = result
				result = math.sqrt(result1)
				print(f'Результат: sqrt({result1}) =', result)
				continue
			if in_operation == 'Abs':
				result1 = result
				result = abs(result)
				print(f'Результат: abs({result1}) =', result)
				continue
			if in_operation == '!':
				result1 = result
				result = math.factorial(result)
				print(f'Результат: {result1}! =', result)
				continue
			else:
				print('Вы ввели некоректную операцию! Повторите пожалуйста')
		else:
			print(f'{name}, Вы ввели некоректную операцию (или она пока неподдерживается)! Повторите пожалуйста.')
			continue
			
print(f'{name}, спасибо, что воспользовались услугами нашего калькулятора! Заходите еще раз!')