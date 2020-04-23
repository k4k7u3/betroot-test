# v.1.1 
# Добавить список
# Добавить все операции которые нужно через переменные в начале

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
operation_step = '**'
operation_sqrt = 'Sqrt'
operation_modul = 'Abs'
operation_fact = '!'
operation_auto = 'Auto'
operation_exit = 'Exit'
operation_info = 'Info'

list_operation = [operation_sum, operation_min, operation_umn, operation_del, operation_celdel, operation_ostatok, operation_step, operation_sqrt, operation_modul, operation_fact, operation_auto, operation_exit, operation_info]
# Функция для вводимого числа
def input_chislo():
	while True:
		input_per = input('Введите число: ')
		input_per = input_per.strip().replace(' ', '')
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
					break
		else:
			input_per = int(input_per)
			break
	return input_per
# Функция для автоматического ввода
def auto_oper(input_value):
	if input_value.isdigit() == False:
		if input_value.count('.') == 0 or input_value.count('.') > 1:
			print('Вы ввели некоректное число!')
			input_value = False
		elif input_value.count('.') == 1:
			input_value1 = input_value
			input_value = input_value.replace('.', '')
			if input_value.isdigit() == False:
				print('Вы ввели некоректное число!')
				input_value = False
			else:
				input_value = input_value1
				input_value = float(input_value)
	else:
		input_value = int(input_value)
	return input_value
name = input('Здравствуйте! Введите ваше имя: ')
name = name.strip().capitalize()
# Основной цикл
while True:
	if flag == 0:
		operation = input(f'{name}, выберите какую операцию Вы хотите произвести (для выхода введите "Exit", для описания операций введите "Info"): ')
		operation = operation.strip().capitalize()
		if operation not in list_operation:
			print(f'{name}, Вы ввели некоректную операцию. Повторите попытку')
			continue
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
			print('auto' + '\t'*2 + '- позволяет вводить команду полностью (доступна только одна операция!!!)')
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
			x = input_chislo()
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
			x = input_chislo()
			result = round(math.factorial(x), 3)
			print(f'Вы ввели x = {x}. Результат {x}! =', result)
			flag = 1
			continue
		elif operation == operation_auto:	
			while True:
				input_per = input('Введите операцию полностью (для выхода введите "Exit"): ')
				input_per = input_per.strip().replace(' ', '')
				if operation_sum in input_per:
					input_per = input_per.split('+')
					x = input_per[0]
					y = input_per[1]
					x = auto_oper(x)
					if x == False:
						continue
					y = auto_oper(y)
					if y == False:
						continue
					result = round(x + y, 3)
					print(f'Вы ввели x = {x} , y = {y}. Результат {x} + {y} =', result)
					flag = 1
					break
	else:
		pass


