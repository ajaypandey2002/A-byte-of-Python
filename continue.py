while True:
	s = input('Введите что-нибудь: ')
	if s == 'Выход':
		break
	if len(s) < 3:
		print('Слишком мало символов')
		continue
	print('Введенная строка достаточной длины')