# v.1.1 
# Добавить список
# Добавить все операции которые нужно через переменные в начале
# добавил отрицательные числа в ручном режиме

import random
import math

result = 0
flag = 0
x = 0    			# Первое вводимое число
y = 0				# Второе вводимое число
z = 0				# Третье вводимое число
input_per = 0		# Переменная для функции

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

list_operation = [operation_sum, operation_min, operation_umn, operation_del, operation_celdel, operation_ostatok, operation_step, operation_sqrt, operation_modul, operation_fact, operation_auto, operation_exit, operation_info]
# Функция для вводимого числа
def input_chislo():
	while True:
		input_per = input('Введите число: ')
		input_per = input_per.strip().replace(' ', '')
		if input_per[0] == '-' and input_per.count('-') == 1:
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
	else:
		input_value = int(input_value)
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
	operation = []
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
			operation.append(i)
			number.append(num)
			num = ''
			flag1 = 0
		else:
			print('Вы ввели неверное число')
			return None
	number.append(num)
	return number, operation
name = input('Здравствуйте! Введите ваше имя: ')
name = name.strip().capitalize()
# Основной цикл
while True:
	if flag == 0:
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
				if operation_sum in input_per:
					input_per = input_per.split('+')
					x = input_per[0]
					y = input_per[1]
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
				elif operation_min in input_per:
					input_per = input_per.split('-')
					x = input_per[0]
					y = input_per[1]
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
				elif operation_umn in input_per:
					input_per = input_per.split('*')
					x = input_per[0]
					y = input_per[1]
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
				elif operation_del in input_per:
					input_per = input_per.split('/')
					x = input_per[0]
					y = input_per[1]
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
				elif operation_celdel in input_per:
					input_per = input_per.split('//')
					x = input_per[0]
					y = input_per[1]
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
				elif operation_ostatok in input_per:
					input_per = input_per.split('%')
					x = input_per[0]
					y = input_per[1]
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
				elif operation_step in input_per:
					input_per = input_per.split('^')
					x = input_per[0]
					y = input_per[1]
					x = auto_oper(x)
					if x == 'Error':
						continue
					y = auto_oper(y)
					if y == 0:
						print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
						continue
					if y == 'Error':
						continue
					result = round(x ** y, 3)
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} ^ {y} =', result)
					flag = 1
					break
				elif operation_sqrt in input_per:
					input_per = input_per.split('sqrt')
					x = input_per[0]
					y = input_per[1]
					if x == '':
						y = auto_oper(y)
						if y == 'Error':
							continue
						result = round(math.sqrt(y), 3)
						print(f'Вы ввели x = {y}. Результат sqrt({y}) =', result)
						flag = 1
						break
					elif y == '':
						x = auto_oper(x)
						if x == 'Error':
							continue
						result = round(math.sqrt(x), 3)
						print(f'Вы ввели x = {x}. Результат sqrt({x}) =', result)
						flag = 1
						break
				elif operation_modul in input_per:
					input_per = input_per.split('abs')
					x = input_per[0]
					y = input_per[1]
					if x == '':
						y = auto_oper(y)
						if y == 'Error':
							continue
						result =  round(abs(y), 3)
						print(f'Вы ввели x = {y}. Результат abs({y}) =', result)
						flag = 1
						break
					elif y == '':
						x = auto_oper(x)
						if x == 'Error':
							continue
						result =  round(abs(x), 3)
						print(f'Вы ввели x = {x}. Результат abs({x}) =', result)
						flag = 1
						break
				elif operation_fact in input_per:
					input_per = input_per.split('!')
					x = input_per[0]
					y = input_per[1]
					if x == '':
						y = auto_oper(y)
						if y == 'Error':
							continue
						result = round(math.factorial(y), 3)
						print(f'Вы ввели x = {y}. Результат ({y})! =', result)
						flag = 1
						break
					elif y == '':
						x = auto_oper(x)
						if x == 'Error':
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
				input_per = input_per.lower().strip().replace(' ', '')
				if operation_sum in input_per:
					input_per = input_per.split('+')
					x = input_per[1]
					x = auto_oper(x)
					if x == 'Error':
						continue
					result1 = result
					result = round(result + x, 3)
					print(f'Результат: {result1} + {x} =', result)
					break
				elif operation_min in input_per:
					input_per = input_per.split('-')
					x = input_per[1]
					x = auto_oper(x)
					if x == 'Error':
						continue
					result1 = result
					result = round(result - x, 3)
					print(f'Результат: {result1} - {x} =', result)
					break
				elif operation_umn in input_per:
					input_per = input_per.split('*')
					x = input_per[1]
					x = auto_oper(x)
					if x == 'Error':
						continue
					result1 = result
					result = round(result * x, 3)
					print(f'Результат: {result1} * {x} =', result)
					break
				elif operation_del in input_per:
					input_per = input_per.split('/')
					x = input_per[1]
					x = auto_oper(x)
					if x == 0:
						print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
						continue
					if x == 'Error':
						continue
					result1 = result
					result = round(result / x, 3)
					print(f'Результат: {result1} / {x} =', result)
					break
				elif operation_celdel in input_per:
					input_per = input_per.split('//')
					x = input_per[1]
					x = auto_oper(x)
					if x == 0:
						print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
						continue
					if x == 'Error':
						continue
					result1 = result
					result = round(result // x, 3)
					print(f'Результат: {result1} // {x} =', result)
					break
				elif operation_celdel in input_per:
					input_per = input_per.split('%')
					x = input_per[1]
					x = auto_oper(x)
					if x == 0:
						print(f'{name}, что же вы так, на 0 мы делить не можем. Повторите попытку')
						continue
					if x == 'Error':
						continue
					result1 = result
					result = round(result % x, 3)
					print(f'Результат: {result1} % {x} =', result)
					break
				elif operation_step in input_per:
					input_per = input_per.split('^')
					x = input_per[1]
					x = auto_oper(x)
					if x == 'Error':
						continue
					result1 = result
					result = round(result ** x, 3)
					print(f'Результат: {result1} ^ {x} =', result)
					break
				elif operation_sqrt in input_per:
					result1 = result
					result = math.sqrt(result1)
					print(f'Результат: sqrt({result1}) =', result)
					break
				elif operation_modul in input_per:
					result1 = result
					result = abs(result1)
					print(f'Результат: abs({result1}) =', result)
					break
				elif operation_fact in input_per:
					result1 = result
					result =  math.factorial(result)
					print(f'Результат: ({result1})! =', result)
					break
				elif input_per == 'exit':
					break
		else:
			print(f'{name}, Вы ввели некоректную операцию. Повторите попытку')
			continue
 
print(f'{name}, спасибо, что воспользовались услугами нашего калькулятора! Заходите еще раз!')