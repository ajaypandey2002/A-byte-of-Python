name = 'Swaroop' #объект строки
 
if name.startswith('Swa'):
	print('Да, строка начинается на "Swa"')

if 'a' in name:
	print('Да, она содержит строку "а"')

if name.find('war') != -1:
	print('Да, она содержит строку "war"')

delimiter = '_*_'

mylist = ['Brasil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))