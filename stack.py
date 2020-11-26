

def greet(name):
	print('Hello,', name, '!')
	greet2(name)
	print('getting ready to say bye...')
	bye()
def greet2(name):
	print('How are you,', name,'?')
def bye():
	print('ok bye!')


#name = greet('Ajay')


def fact(x):
	if x ==1:
		return 1
	else:
		return x*fact(x-1)

x = fact(5)
print(x)

