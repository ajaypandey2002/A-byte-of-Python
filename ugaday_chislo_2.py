number = 20
running = True
while running :
	guess = int(input('Введите число : '))
	if guess == number :
		print('Поздравляю, Вы угадали.')
		running = False
	elif guess < number :
		print('Вы не угадали. Ваше число меньше, попытайтесь еще раз.')
	else :
		print('Вы не угадали. Ваше число больше, попытайтесь еще раз')
else :
	print('Малаца')