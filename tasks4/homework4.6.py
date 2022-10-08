# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл
# не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import cycle, count
print('СДЕЛАЕМ ЗАДАЧУ 1 ЧЕРЕЗ count()')
go=int(input('Введите число с которого начнем генерировать числа: '))
stop=int(input('Введите число на котором остановимся генерировать числа: '))
generator = count(go, 1)
for i in generator:
    print(i)
    if i == stop:
        break

print('СДЕЛАЕМ ЗАДАЧУ 1 ЧЕРЕЗ ФУНКЦИЮ И ЦИКЛ')
def int_cell(sp):
    while True:
        yield sp
        sp+=1

start = int(input('начать генерировать числа с: '))
finish = int(input('закончить генерировать числа на числе: '))

for el in int_cell(start):
    if el == finish+1:
        break
    print(el)

print('СДЕЛАЕМ ЗАДАЧУ 2 ЧЕРЕЗ ФУНКЦИЮ И ЦИКЛ')
def copy_list(sl): #sl = set_list
    i=0
    while True:
        yield sl[i]
        i+=1

first_list = [1231, 'skdjnfk', 999.2, 'ПреВед Как ДИЛА', 'числооо??', 1198]

for el in copy_list(first_list):
    if el == first_list[len(first_list)-1]:
        print(el)
        break
    print(el)

print('СДЕЛАЕМ ЗАДАЧУ 2 ЧЕРЕЗ cycle()')
copier = cycle(first_list)

for el in copier:
    if el == first_list[len(first_list)-1]:
        print(el)
        break
    print(el)
