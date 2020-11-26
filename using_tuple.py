zoo = ('python', 'elefant', 'pinguin')
print('количество животных в зоопарке - ', len(zoo))

new_zoo = 'monkey', 'camel', zoo
print('количество клеток в зоопарке - ', len(new_zoo))
print('все животные в новом зоопарке: ', new_zoo)
print('животные, привезенные из старого зоопарка: ', new_zoo[2])
print('последнее животное, привезенноe из старого зоопарка - ', new_zoo[2][2])
print('количество животных в новом зоопарке - ', len(new_zoo)-1+len(new_zoo[2])) 