s = input('Введите строку: ')

if len(s) > 2:
	print(s[:2] + s[-2:])
elif len(s) == 2:
	print(s*2)
else:
	print()

# v1.1 - с Бесконечным циклом и выходом из него
# while 1:
# 	s = input("Введите строку (для выхода введите 'break'): ")
# 	if s == 'break':
# 		break
# 	elif len(s) > 2:
# 		print(s[:2] + s[-2:])
# 	elif len(s) == 2:
# 		print(s*2)
# 	elif len(s) < 2:
# 		print()
