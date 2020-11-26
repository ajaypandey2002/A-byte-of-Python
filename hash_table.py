book = dict()

book['apple'] = 0.67
book['avocado'] = 1.49
book['milk'] = 1.49
print(book)
print(book['avocado'])

phone_book = {} # то же что и dict()
phone_book['Ajay'] = 89024565646
phone_book['emergency'] = 911
print(phone_book['Ajay'])

voted = {}
def check_voter(name):
	if voted.get(name):
		print('Kick', name, 'out!')
	else:
		voted[name] = True
		print('Let', name, 'vote!')
check_voter('Tom')
check_voter('Tom')
