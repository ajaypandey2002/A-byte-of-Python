# создать 5-ую версию с использованием zipfile вместо os.system. Не получилось 


import os
import time
import zipfile

#1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['C:\\py']

#2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'C:\\Backup' #подставить тот путь, который будем использовать (в моем случае этот)

#3. Файлы помещаются в zip-архив
#4. Текущая дата является именем подкаталога в основном каталоге.
today = target_dir + os.sep + time.strftime('%d%m%Y')
# Текущее имя явлется именем zip-архива
now = time.strftime('%H%M%S')

# Запрашиваем комментарий пользователя для имени файла 
comment = input('Введите комментарий --> ')
if len(comment) == 0: # проверяем, введён ли комментарий
	target = today + os.sep + now + '.zip'
else:
	target = today + os.sep + now + '_' + \
		comment.replace(' ', '_') + '.zip'

# создаем каталог, если его ещё нет
if not os.path.exists(today):
	os.mkdir(today) # создание каталога
print('Каталог успешно создан', today)

# 5. Используем команду "zip" для помещения файлов в zip-архив
zip_command = "zip -qp {0} {1}".format(target, ' '.join(source))

if zipfile.is_zipfile(target) == True:
	print('Резервная копия успешно создана в ', target)
else:
	print('Создание резервной копии НЕ УДАЛОСЬ')