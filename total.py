def total(initial=1, *numbers, **keywords):
	count = initial
	for number in numbers:
		count += number
		print(count)
	for key in keywords:
		count += keywords[key]
		print(key)
	return count

print(total(10, 1, 2, 3, vegetables = 50, fruits = 100))