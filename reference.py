print('простое присваивание')
shoplist = ['apples','mango','carrot','bananas']
mylist = shoplist #еще одно имя указывающее на тот же объект

del shoplist[0] #удаляем первую покупку из списка
 
print('shoplist: ', shoplist)
print('mylist: ', mylist) #выводят одно и то же без пункта яблоко => указывают на один объект

print('копирование при помощи полной вырезки')
mylist = shoplist[:] #создаем копию путем полной вырезки
del mylist[0] #удаляем первый элемент

print('shoplist: ', shoplist)
print('mylist: ', mylist) #теперь списки разные
