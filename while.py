number = 23
running = True

while running:
	guess = int(input('Введите целое число: '))

	if guess == number:
		print('Congratulations!')
		running = False
	elif guess < number:
		print('Нет, загаданное число больше')
	else:
		print('Нет, загаданное число меньше')
else:
	print('Цикл while закончен.')