def reverse(text):
	return text[::-1] # разворачивает слово наоборот

def is_palindrome(text):
	return text == reverse(text) # функция проверяющее палиндром ли слово

something = input('Введите текст: ')
if (is_palindrome(something)):
	print("Да, это палиндром")
else:
	print("Нет, это не палиндром")