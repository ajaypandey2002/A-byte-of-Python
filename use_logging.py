import os, platform, logging

if platform.platform().startswith('Windows'):	#проверяем, Windows ли
	#определяем диск, на котором домашний каталог
	logginng_file = os.path.join(os.getenv('HOMEDRIVE'), \
		#определяем путь к домашнему каталогу
		os.getenv('HOMEPATH'), \
		#имя файла в котором хотим сохранить информацию
		'test.log')
	# сложив всё, получаем полный путь к файлу
	#os.path.join складывает все три части вместе
else:
	logginng_file = os.path.join(os.getenv('HOME'),'test.log')

print("Сохраняем лог в", logginng_file)

logging.basicConfig(
	level = logging.DEBUG,
	format = '%(asctime)s : %(levelname)s : %(message)s',
	filename = logginng_file,
	filemode = 'w',
)

logging.debug("Начало программы")
logging.info("Какие-то действия")
logging.warning("рограмма умирает")