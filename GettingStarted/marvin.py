#-*-coding: UTF-8 -*-
#Author by Mikle Fedorenko

#Программа выводит посимвольно вертикально, указанную
#фразу или слово. Демонстрация работы цикла со списками

paranoid_android = "Marvin"  #слово которое будем выводить

letters = list(paranoid_android) #преоюразование в список

for char in letters:
    print('\t' + char)
