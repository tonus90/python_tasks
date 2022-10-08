# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
# были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
import json #импорт джсон
result = []
my_dict = {}
with open('file.txt', 'r') as file:
    subjects_list = file.readlines() #считаем файл в лист
    for i in range (len(subjects_list)):
        my_list = subjects_list[i].split() #разобьем строку предмета по словам
        sub_name = my_list.pop(0) #вытащим название предмета
        for n in my_list:
            try:   #отловим ошибку, если нет цифр в названии предмета
                hours_list = n.split('(') #сплитуем по скобочке ( получим лист '100', 'л)')
                result.append(int(hours_list[0])) #проинтуем и добавим в результат число 100
            except ValueError:
                result.append(0) #если там чисел не было, то добавим 0
        my_dict[sub_name] = sum(result) #запишем в словарик Назв_предмета : часы
        result.clear() #зачистим резалт список, для след предмета

print(f'\nОбработали текстовый файл, получили словарь: {my_dict}') #напечатаем словарь

with open('my_json.json', 'w') as my_json: #ну и в json попробуем запихнуть, для наглядности, чтоб рез-тат показать на Гите
    json.dump(my_dict, my_json)