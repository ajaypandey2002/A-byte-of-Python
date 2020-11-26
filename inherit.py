class SchoolMember:
	'''представляет любого человека в школе.'''
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print('(Создан SchoolMember: {0})'.format(self.name))

	def tell(self):
		'''вывести  информацию.'''
		print('Имя: "{0}" Возраст: {1}"'.format(self.name, self.age), end = " ")

class Teacher(SchoolMember):
	'''представляет преподавателя.'''
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary
		print('(Создан Teacher: {0})'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('\nЗарплата: "{0:d}"'.format(self.salary))

class Student(SchoolMember):
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print('(Создан Student: {0})'.format(self.name))

	def tell(self):
		SchoolMember.tell(self)
		print('\nОценки: "{0:d}"'.format(self.marks))

t = Teacher('Mrs. Protopopova', 40, 30000)
s = Student('Ajay', 18, 75)

print() # печатает пустую строку

members = [t, s]
for member in members:
	member.tell() # работает как для преподавателя, так и для студента