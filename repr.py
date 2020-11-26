i = []
i.append('item')

a = repr(i)
print(a)

a = eval(repr(i)) 
print(a)

if eval(repr(i)) == i:
	print('True')

