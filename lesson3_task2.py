while 1:
	s = input("Введите номер телефона( для выхода введите break): ")
	if s == 'break':
		break
	elif s.isdigit() == True and len(s) == 10:
		print(f'Вы ввели такой номер телeфона - {s}')
	elif s.isdigit() == True and (len(s) < 10 or len(s) > 10):
		print('Номер телефона состоит из 10 цифр. Не переживайте, можете повторить еще раз =) У вас все получится. just do it')
	elif s.isdigit() == False:
		print('Номер состоит только из цифр. Не переживайте, можете повторить еще раз =) У вас все получится. just do it')