# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс. Используйте форматирование строк.

time_seconds = int(input('Введите время в секундах: '))

# minutes = time_seconds/60 с плавующей точкой получается надо делать округление, нашел функцию divmod,так проще
# print(f'Время в минутах: {minutes}')
# seconds = minutes//100
# print(seconds)

min, sec = divmod(time_seconds, 60)
hour, min = divmod(min, 60)

print(f'{hour:02}:{min:02}:{sec:02}') # вот тут вот есть вопросик, внутри {} ставим min:02, из урока я понял зачем это, но что тут такое ':' как это влияет на дальнейшую строку 02,
                                      # строкой '2' мы задаем кол-во нулей перед числом?, а строкой '0' тогда что делаем. можно ли вместо '0' перед секундами
                                      # ставить 1, 2 или любые другие символы, теже *.