import random
import math

result = 0
flag = 0
x = 0    			# Первое вводимое число
y = 0				# Второе вводимое число
z = 0				# Третье вводимое число
input_per = ''		# Переменная для функции
input_operation = []
per_word = 0

operation_sum = '+'
operation_min = '-'
operation_umn = '*'
operation_del = '/'
operation_celdel = '//'
operation_ostatok = '%'
operation_step = '^'
operation_sqrt = 'sqrt'
operation_modul = 'abs'
operation_fact = '!'
operation_auto = 'auto'
operation_exit = 'exit'
operation_info = 'info'

list_operation = [operation_sum, operation_min, operation_umn, operation_del, operation_celdel, operation_ostatok, operation_step, operation_sqrt, operation_modul, operation_fact, operation_auto, operation_exit, operation_info, '?']
# Функция для вводимого числа
def input_chislo():
	while True:
		input_per = input('Введите число: ')
		input_per = input_per.strip().replace(' ', '')
		if input_per == '':
			print('Вы ввели некоректное число!')
			continue
		elif input_per[0] == '-' and input_per.count('-') == 1:
			input_per = input_per.replace('-', '')
			negative_number = 1
		else:
			negative_number = 0
		if input_per.isdigit() == False:
			if input_per.count('.') == 0 or input_per.count('.') > 1:
				print('Вы ввели некоректное число!')
				continue
			elif input_per.count('.') == 1:
				input_per1 = input_per
				input_per = input_per.replace('.', '')
				if input_per.isdigit() == False:
					print('Вы ввели некоректное число!')
					continue
				else:
					input_per = input_per1
					input_per = float(input_per)
					if negative_number == 1:
						input_per = input_per * -1
					break
		else:
			input_per = int(input_per)
			if negative_number == 1:
				input_per = input_per * -1
			break
	return input_per
# Функция для автоматического ввода
def auto_oper(input_value):
	if input_value[0] == '-' and input_value.count('-') == 1:
		input_value = input_value.replace('-', '')
		negative_number = 1
	else:
		negative_number = 0
	if input_value.isdigit() == False:
		if input_value.count('.') == 0 or input_value.count('.') > 1:
			print('Вы ввели некоректное число!')
			input_value = 'Error'
		elif input_value.count('.') == 1:
			input_value1 = input_value
			input_value = input_value.replace('.', '')
			if input_value.isdigit() == False:
				print('Вы ввели некоректное число!')
				input_value = 'Error'
			else:
				input_value = input_value1
				input_value = float(input_value)
				if negative_number == 1:
					input_value = input_value * -1
				return input_value
	else:
		input_value = int(input_value)
		if negative_number == 1:
			input_value = input_value * -1
	return input_value
#Функция для вывода информации об операциях
def description_oper():
	print('+' + '\t'*2 + '- сложение;')
	print('-' + '\t'*2 + '- вычитание;')
	print('*' + '\t'*2 + '- умножение;')
	print('/' + '\t'*2 + '- деление;')
	print('//' + '\t'*2 + '- получение целой части от деления;')
	print('%' + '\t'*2 + '- получение остатка от деления;')
	print('^' + '\t'*2 + '- возведение числа в степень;')
	print('sqrt' + '\t' + '- извлечение квадратного корня;')
	print('abs n' + '\t' + '- модуль числа, где n - введеное число;')
	print('!' + '\t'*2 + '- факториал числа, n! - где n введеное число;')
	print('auto' + '\t' + '- позволяет вводить команду полностью (доступна только одна операция!!!)')
# Функция для сортировки вводимой строки в автоматическом режиме
def sort_string(s):
	flag1 = 0
	num = ''
	number = []
	for i in s:
		if i.isdigit() == True:
			num += i
			flag1 = 1
		elif i == '-' and flag1 == 0:
			num += i
		elif i == '.' and flag1 == 1:
			num += i
		elif i in list_operation and flag1 == 1:
			input_operation.append(i)
			number.append(num)
			num = ''
			flag1 = 0
		elif i in list_operation and flag == 0:
			input_operation.append(i)
		else:
			print('Вы ввели неверное число')
			return None
	number.append(num)
	return number, input_operation

name = input('Здравствуйте! Введите ваше имя: ')
name = name.strip().capitalize()
# Основной цикл
while True:
	if flag == 0:
		input_operation = []
		input_number = []
		per_word = 0
		operation = input(f'{name}, выберите какую операцию Вы хотите произвести (для выхода введите "Exit", для описания операций введите "Info"): ')
		operation = operation.strip().lower()
		if operation not in list_operation:
			print(f'{name}, Вы ввели некоректную операцию. Повторите попытку')
			continue
		if operation == 'exit':
			break
		elif operation == 'info':
			description_oper()
			continue
		elif operation == operation_sum:
			x = input_chislo()
			y = input_chislo()
			result = round(x + y, 3)
			print(f'Вы ввели x = {x} , y = {y}. Результат {x} {operation} {y} =', result)
			flag = 1
			continue
		elif operation == operation_min:
			x = input_chislo()
			y = input_chislo()
			result = round(x - y, 3)
			print(f'Вы ввели x = {x} , y = {y}. Результат {x} {operation} {y} =', result)
			flag = 1
			continue
		elif operation == operation_umn:
			x = input_chislo()
			y = input_chislo()
			result = round(x - y, 3)
			print(f'Вы ввели x = {x} , y = {y}. Результат {x} {operation} {y} =', result)
			flag = 1
			continue
		elif operation == operation_del:
			x = input_chislo()
			while True:
				y = input_chislo()
				if y == 0:
					print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
					continue
				break
			result = round(x / y, 3)
			print(f'Вы ввели x = {x} , y = {y}. Результат {x} {operation} {y} =', result)
			flag = 1
			continue
		elif operation == operation_celdel:
			x = input_chislo()
			while True:
				y = input_chislo()
				if y == 0:
					print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
					continue
				break
			result = round(x // y, 3)
			print(f'Вы ввели x = {x} , y = {y}. Результат {x} {operation} {y} =', result)
			flag = 1
			continue
		elif operation == operation_ostatok:
			x = input_chislo()
			while True:
				y = input_chislo()
				if y == 0:
					print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
					continue
				break
			result = round(x % y, 3)
			print(f'Вы ввели x = {x} , y = {y}. Результат {x} {operation} {y} =', result)
			flag = 1
			continue
		elif operation == operation_step:
			x = input_chislo()
			y = input_chislo()
			result = round(x ** y, 3)
			print(f'Вы ввели x = {x} , y = {y}. Результат {x} {operation} {y} =', result)
			flag = 1
			continue
		elif operation == operation_sqrt:
			while True:
				x = input_chislo()
				if x < 0:
					print("Мы не извлекаем корень с отрицательного числа! Может кто другой сможет, let's try = ) ")
					continue
				break
			result = round(math.sqrt(x), 3)
			print(f'Вы ввели x = {x}. Результат {operation}({x}) =', result)
			flag = 1
			continue
		elif operation == operation_modul:
			x = input_chislo()
			result = round(abs(x), 3)
			print(f'Вы ввели x = {x}. Результат {operation}({x}) =', result)
			flag = 1
			continue
		elif operation == operation_fact:
			while True:
				x = input_chislo()
				if x < 0:
					print('''Мы не находим факториал отрицательного числа! Может кто другой сможет, let's try = ) ''')
					continue
				break
			result = round(math.factorial(x), 3)
			print(f'Вы ввели x = {x}. Результат {x}! =', result)
			flag = 1
			continue
		elif operation == operation_auto:	
			while True:
				input_per = input('Введите операцию полностью (для выхода введите "Exit"): ')
				input_per = input_per.lower().strip().replace(' ', '')
				if input_per == '':
					print('Вы ввели некоректное число')
					continue
				elif operation_exit in input_per:
					break
				if operation_sqrt in input_per:
					input_operation.append('sqrt')
					input_per = input_per.replace('sqrt', '')
					per_word = 1
				elif operation_modul in input_per:
					input_operation.append('abs')
					input_per = input_per.replace('abs', '')
					per_word = 1
				elif operation_fact in input_per:
					input_operation.append('!')
					input_per = input_per.replace('!', '')
					per_word = 1
				elif operation_celdel in input_per:
					input_operation.append('?')
					input_per = input_per.replace('//', '?')
				return_all = sort_string(input_per)
				if return_all == None:
					continue
				input_number, input_operation = return_all
				if len(input_operation) < 1:
					print('Вы ввели некоректное число')
					input_operation = []
					input_number = []
					continue
				elif len(input_number) == 2:
					if input_number[0] == '' or input_number[1] == '':
						print('Вы ввели некоректное число')
						input_operation = []
						input_number = []
						continue
				elif len(input_number) == 1 and per_word == 0:
					print('Вы ввели некоректное число')
					input_operation = []
					input_number = []
					continue
				if input_operation[0] == operation_sum:
					# input_per = input_per.split('+')
					x = input_number[0]
					y = input_number[1]
					x = auto_oper(x)
					if x == 'Error':
						continue
					y = auto_oper(y)
					if y == 'Error':
						continue
					result = round(x + y, 3)
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} + {y} =', result)
					flag = 1
					break
				elif input_operation[0] == operation_min:
					# input_per = input_per.split('-')
					x = input_number[0]
					y = input_number[1]
					x = auto_oper(x)
					if x == 'Error':
						continue
					y = auto_oper(y)
					if y == 'Error':
						continue
					result = round(x - y, 3)
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} - {y} =', result)
					flag = 1
					break
				elif input_operation[0] == operation_umn:
					# input_per = input_per.split('*')
					x = input_number[0]
					y = input_number[1]
					x = auto_oper(x)
					if x == 'Error':
						continue
					y = auto_oper(y)
					if y == 'Error':
						continue
					result = round(x * y, 3)
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} * {y} =', result)
					flag = 1
					break
				elif input_operation[0] == operation_del:
					# input_per = input_per.split('/')
					x = input_number[0]
					y = input_number[1]
					x = auto_oper(x)
					if x == 'Error':
						continue
					y = auto_oper(y)
					if y == 0:
						print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
						continue
					if y == 'Error':
						continue
					result = round(x / y, 3)
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} / {y} =', result)
					flag = 1
					break
				elif input_operation[0] == '?':
					# input_per = input_per.split('//')
					x = input_number[0]
					y = input_number[1]
					x = auto_oper(x)
					if x == 'Error':
						continue
					y = auto_oper(y)
					if y == 0:
						print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
						continue
					if y == 'Error':
						continue
					result = round(x // y, 3)
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} // {y} =', result)
					flag = 1
					break
				elif input_operation[0] == operation_ostatok:
					# input_per = input_per.split('%')
					x = input_number[0]
					y = input_number[1]
					x = auto_oper(x)
					if x == 'Error':
						continue
					y = auto_oper(y)
					if y == 0:
						print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
						continue
					if y == 'Error':
						continue
					result = round(x % y, 3)
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} % {y} =', result)
					flag = 1
					break
				elif input_operation[0] == operation_step:
					# input_per = input_per.split('^')
					x = input_number[0]
					y = input_number[1]
					x = auto_oper(x)
					if x == 'Error':
						continue
					y = auto_oper(y)
					if y == 'Error':
						continue
					result = round(x ** y, 3)
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} ^ {y} =', result)
					flag = 1
					break
				elif input_operation[0] == operation_sqrt:
					# input_per = input_per.split('sqrt')
					x = input_number[0]
					x = auto_oper(x)
					if x == 'Error':
						continue
					if x < 0:
						print("Мы не извлекаем корень с отрицательного числа! Может кто другой сможет, let's try = ) ")
						continue
					result = round(math.sqrt(x), 3)
					print(f'Вы ввели x = {x}. Результат sqrt({x}) =', result)
					flag = 1
					break
				elif input_operation[0] == operation_modul:
					# input_per = input_per.split('abs')
					x = input_number[0]
					x = auto_oper(x)
					if x == 'Error':
						continue
					result =  round(abs(x), 3)
					print(f'Вы ввели x = {x}. Результат abs({x}) =', result)
					flag = 1
					break
				elif input_operation[0] == operation_fact:
					# input_per = input_per.split('!')
					x = input_number[0]
					x = auto_oper(x)
					if x == 'Error':
						continue
					if x < 0:
						print('''Мы не находим факториал отрицательного числа! Может кто другой сможет, let's try = ) ''')
						continue
					result = round(math.factorial(x), 3)
					print(f'Вы ввели x = {x}. Результат ({x})! =', result)
					flag = 1
					break
				elif input_per == 'exit':
					break
	else:
		operation = input('Ввести дальнейшую операцию или сбросить? (для cброса введите "clear", для описания операций введите "Info", для выхода введите "Exit"): ')
		operation = operation.strip().lower()
		if operation == 'exit':
			break
		elif operation == 'info':
			description_oper()
			continue
		elif operation == 'clear':
			result = 0
			flag = 0
			continue
		elif operation == operation_sum:
			z = input_chislo()
			result1 = result
			result += z
			result = round(result, 3)
			print(f'Результат {result1} {operation} {z} =', result)
			continue
		elif operation == operation_min:
			z = input_chislo()
			result1 = result
			result -= z
			result = round(result, 3)
			print(f'Результат {result1} {operation} {z} =', result)
			continue
		elif operation == operation_umn:
			z = input_chislo()
			result1 = result
			result *= z
			result = round(result, 3)
			print(f'Результат {result1} {operation} {z} =', result)
			continue
		elif operation == operation_del:
			while True:
				z = input_chislo()
				if z == 0:
					print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
					continue
				break
			result1 = result
			result /= z
			result = round(result, 3)
			print(f'Результат {result1} {operation} {z} =', result)
			continue
		elif operation == operation_celdel:
			while True:
				z = input_chislo()
				if z == 0:
					print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
					continue
				break
			result1 = result
			result //= z
			result = round(result, 3)
			print(f'Результат {result1} {operation} {z} =', result)
			continue
		elif operation == operation_ostatok:
			while True:
				z = input_chislo()
				if z == 0:
					print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
					continue
				break
			result1 = result
			result %= z
			result = round(result, 3)
			print(f'Результат {result1} {operation} {z} =', result)
			continue
		elif operation == operation_step:
			z = input_chislo()
			result1 = result
			result **= z
			result = round(result, 3)
			print(f'Результат {result1} {operation} {z} =', result)
			continue
		elif operation == operation_sqrt:
			if result < 0:
				print("Мы не извлекаем корень с отрицательного числа! Может кто другой сможет, let's try = ) ")
				continue
			result1 = result
			result = round(math.sqrt(result), 3)
			print(f'Результат sqrt({result1}) =', result)
			continue
		elif operation == operation_modul:
			result1 = result
			result = round(abs(result), 3)
			print(f'Результат abs({result1}) =', result)
			continue
		elif operation == operation_fact:
			if result < 0:
				print("Мы не находим факториал отрицательного числа Может кто другой сможет, let's try = ) ")
				continue
			result1 = result
			result = round(math.factorial(result), 3)
			print(f'Результат abs({result1})! =', result)
			continue
		elif operation == operation_auto:
			while True:
				input_per = input(f'Введите операцию которую хотите сделать с результатом (для выхода введите "Exit"): {result} ')
				result1 = result
				result = str(result)
				input_per = result + input_per
				input_per = input_per.lower().strip().replace(' ', '')
				if input_per == '':
					print('Вы ввели некоректное число')
					continue
				elif operation_exit in input_per:
					break
				elif operation_sqrt in input_per:
					input_operation.append('sqrt')
					input_per = input_per.replace('sqrt', '')
				elif operation_modul in input_per:
					input_operation.append('abs')
					input_per = input_per.replace('abs', '')
				elif operation_fact in input_per:
					input_operation.append('!')
					input_per = input_per.replace('!', '')
				elif operation_celdel in input_per:
					input_operation.append('?')
					input_per = input_per.replace('//', '?')
				return_all = sort_string(input_per)
				if return_all == None:
					continue
				input_number, input_operation = return_all
				if len(input_operation) < 1:
					print('Вы ввели некоректное число')
					input_operation = []
					input_number = []
					continue
				elif len(input_number) == 2:
					if input_number[0] == '' or input_number[1] == '':
						print('Вы ввели некоректное число')
						input_operation = []
						input_number = []
						continue
				elif len(input_number) == 1 and per_word == 0:
					print('Вы ввели некоректное число')
					input_operation = []
					input_number = []
					continue
				if input_operation[0] == operation_sum:
					x = input_number[0]
					y = input_number[1]
					x = auto_oper(x)
					if x == 'Error':
						continue
					y = auto_oper(y)
					if y == 'Error':
						continue
					result = round(x + y, 3)
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} + {y} =', result)
					flag = 1
					break
				elif input_operation[0] == operation_min:
					x = input_number[0]
					y = input_number[1]
					x = auto_oper(x)
					if x == 'Error':
						continue
					y = auto_oper(y)
					if y == 'Error':
						continue
					result = round(x - y, 3)
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} - {y} =', result)
					flag = 1
					break
				elif input_operation[0] == operation_umn:
					# input_per = input_per.split('*')
					x = input_number[0]
					y = input_number[1]
					x = auto_oper(x)
					if x == 'Error':
						continue
					y = auto_oper(y)
					if y == 'Error':
						continue
					result = round(x * y, 3)
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} * {y} =', result)
					flag = 1
					break
				elif input_operation[0] == operation_del:
					# input_per = input_per.split('/')
					x = input_number[0]
					y = input_number[1]
					x = auto_oper(x)
					if x == 'Error':
						continue
					y = auto_oper(y)
					if y == 0:
						print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
						continue
					if y == 'Error':
						continue
					result = round(x / y, 3)
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} / {y} =', result)
					flag = 1
					break
				elif input_operation[0] == '?':
					# input_per = input_per.split('//')
					x = input_number[0]
					y = input_number[1]
					x = auto_oper(x)
					if x == 'Error':
						continue
					y = auto_oper(y)
					if y == 0:
						print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
						continue
					if y == 'Error':
						continue
					result = round(x // y, 3)
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} // {y} =', result)
					flag = 1
					break
				elif input_operation[0] == operation_ostatok:
					# input_per = input_per.split('%')
					x = input_number[0]
					y = input_number[1]
					x = auto_oper(x)
					if x == 'Error':
						continue
					y = auto_oper(y)
					if y == 0:
						print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
						continue
					if y == 'Error':
						continue
					result = round(x % y, 3)
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} % {y} =', result)
					flag = 1
					break
				elif input_operation[0] == operation_step:
					# input_per = input_per.split('^')
					x = input_number[0]
					y = input_number[1]
					x = auto_oper(x)
					if x == 'Error':
						continue
					y = auto_oper(y)
					if y == 'Error':
						continue
					result = round(x ** y, 3)
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} ^ {y} =', result)
					flag = 1
					break
				elif input_operation[0] == operation_sqrt:
					# input_per = input_per.split('sqrt')
					x = input_number[0]
					x = auto_oper(x)
					if x == 'Error':
						continue
					if x < 0:
						print("Мы не извлекаем корень с отрицательного числа! Может кто другой сможет, let's try = ) ")
						continue
					result = round(math.sqrt(x), 3)
					print(f'Вы ввели x = {x}. Результат sqrt({x}) =', result)
					flag = 1
					break
				elif input_operation[0] == operation_modul:
					# input_per = input_per.split('abs')
					x = input_number[0]
					x = auto_oper(x)
					if x == 'Error':
						continue
					result =  round(abs(x), 3)
					print(f'Вы ввели x = {x}. Результат abs({x}) =', result)
					flag = 1
					break
				elif input_operation[0] == operation_fact:
					# input_per = input_per.split('!')
					x = input_number[0]
					x = auto_oper(x)
					if x == 'Error':
						continue
					if x < 0:
						print('''Мы не находим факториал отрицательного числа! Может кто другой сможет, let's try = ) ''')
						continue
					result = round(math.factorial(x), 3)
					print(f'Вы ввели x = {x}. Результат ({x})! =', result)
					flag = 1
					break
				elif input_per == 'exit':
					break
		else:
			print(f'{name}, Вы ввели некоректную операцию. Повторите попытку')
			continue
 
print(f'{name}, спасибо, что воспользовались услугами нашего калькулятора! Заходите еще раз!')