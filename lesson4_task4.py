import random

x = random.randint(5, 10)
y = random.randint(0, 5)
operation = ['+', '-', '*', '/']
choose_oper = random.choice(operation)

if choose_oper == '+':
	in_value = int(input(f'Сколько будет {x} + {y}: '))
	if in_value == x + y:
		print('Да ты математик =) ')
	else:
		print('Попробуй в следующий раз!')
elif choose_oper == '-':
	in_value = int(input(f'Сколько будет {x} - {y}: '))
	if in_value == x - y:
		print('Да ты математик =) ')
	else:
		print('Попробуй в следующий раз!')
elif choose_oper == '*':
	in_value = int(input(f'Сколько будет {x} * {y}: '))
	if in_value == x * y:
		print('Да ты математик =) ')
	else:
		print('Попробуй в следующий раз!')
elif choose_oper == '/':
	in_value = float(input(f'Сколько будет {x} / {y}: '))
	if in_value == x / y:
		print('Да ты математик =) ')
	else:
		print('Попробуй в следующий раз!')