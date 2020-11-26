import pickle


class Address:
    my_dict = dict()
    def __init__(self, key, value):
        self.key = key
        self.value = value

        Address.my_dict = dict()
        with open('booking.txt', 'w') as file:
            file.write(key)
            file.write(value)

        file.close()

    def __setitem__(self, key, value):
        self.key = input('Введите имя: ')
        self.value = input('Введите адрес: ')
        Address.my_dict[self.key] = self.value
        if self.key in Address.my_dict:
            print('\nАдрес:', Address.my_dict)

    def __delitem__(self, key):
        self.key = input('Введите имя для удаления: ')
        del Address.my_dict[self.key]
        print('\nВ адресной книге: {0} контактов\n'.format(len(Address.my_dict)))
        for name, address in Address.my_dict.items():
            print('\nКонтакт: {0}, с адресом {1}.'.format(name, address))

    def change(self):
        self.key = input('Введите имя которое нужно изменить: ')
        del Address.my_dict[self.key]

        self.fname = input('Введите новое имя: ')
        self.semail = input('Введите новый адрес: ')
        Address.my_dict[self.fname] = self.semail
        if self.fname in Address.my_dict:
            print('\nАдрес:', Address.my_dict)

    def find(self):
        self.key = input('Введите имя для поиска: ')
        if self.key in Address.my_dict:
            print('Адрес: ', Address.my_dict[self.key])

        else:
            print('Такого имени не найдено.')

    def loading():
        file = open('Book.data', 'rb')
        Address.my_dict=pickle.load(file)  # Помещаем объект в файл.
        file.close()

    loading = staticmethod(loading)

    def store():
        file = open('Book.data', 'wb')
        pickle.dump(Address.my_dict, file)  # Помещаем объект в файл.
        file.close()

    store = staticmethod(store)


r = Address('', '')
Address.loading()
running = True
while running:
    search = int(input('Введите - 1-Добавить контакт; 2-Удалить контакт; 3-Изменить контакт; 4-Найти контакт;\
 Для выхода их программы введите 5-Выход: '))
    if search == 1:
        r.__setitem__('', '')
        if len(Address.my_dict) == 100:
            print('Адресная книга переполнена, удалите 1 из контактов')
            r.__delitem__('')

    if search == 2:
        r.__delitem__('')
        Address.store()

    if search == 3:
        r.change()
        Address.store()

    if search == 4:
        r.find()

    if search == 5:
        Address.store()
        running = False

    if len(Address.my_dict) == 0:
        running = False
