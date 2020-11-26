class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def sayHi(self):
		print('Hi! My name is', self.name, ". I'm", self.age, 'years old' )

Person('Ajay', 18).sayHi()

# равносильно

p = Person('Ajay', 18)
p.sayHi()