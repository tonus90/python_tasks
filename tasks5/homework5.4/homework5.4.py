# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

rus_nums = {
    1:'odin', #тут так написал чтобы не было проблем с кодировкой
    2:'dva',
    3:'tri',
    4:'4etyre'
}

new_list = [] #пустой лист понадобится

with open('file.txt', 'r') as file:
    num_list = file.readlines() #файл в лист
    for i in range(len(num_list)): #по каждому числу проходимся
        my_list = num_list[i].split('-') #сплитуем по тире и в лист
        my_list.pop() #далим посл элемент останется только 'one'
        my_list.append(f'-{rus_nums.get(i+1)}') #к 'one' припишем '-odin' из словаря по ключам
        new_list.append(my_list) #засунем 'one', '-odin' первый элемент в новый лист
        print(my_list) #для отладки

with open('new_file.txt', 'w') as new_file:
    for i in new_list: #каждый элемент ('one', '-odin') списка нью лист
        str=''.join(i) #объединим без пробелов в строку
        new_file.writelines(f'{str}\n') #и запишем построчно эту строку в новый файл
