#-*-coding: UTF-8 -*-
#Author by Mikle Fedorenko

#Программа выводит посимвольно вертикально, указанную
#фразу или слово. Демонстрация работы цикла со списками, срезами

paranoid_android = "Marvin, the Paranoid Android"  #слово которое будем выводить

letters = list(paranoid_android) #преоюразование в список

for char in letters[:6]:
    print('\t' + char)

#отступ 2 табуляции
for char in letters[-7:]:
    print('\t' * 2 + char)

#отступ 3 табуляции
for char in letters[12:20]:
    print('\t' * 3 + char)
