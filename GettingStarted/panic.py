#-*-coding: UTF-8 -*-

#Программа преобразует фразу "Don`t panic!" в
# вывод "on tap" и выводит на экран

phrase = "Don`t panic!"
plist = list(phrase) #определение списка
#вывод переменой и списка на экран
print(phrase)
print(plist)

#извлекаем четыре последних объекта
#и удаляем "nic"
for i in range(4):
    plist.pop()
plist.pop(0) #извлекаем первую букву списка
plist.remove("`") #удаляем апостроф
#меняем местами два последних элемента списка
plist.extend([plist.pop(), plist.pop()])
#извлекаем из списка пробел и вставляем его на место
#второго элемента
plist.insert(2, plist.pop(3))

new_phrase = ''.join(plist) #преобразование списка
#в строку
#вывод списка и новой фразы на экран
print(plist)
print(new_phrase)