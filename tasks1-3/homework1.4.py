# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Введите целое положительное число: '))


length = len(str(number)) #подсчитаем длину числа
n = 0 #счетчик равен 0
max = number%10 #изначально примем за максимум последнюю цифру числа

while n < length:               #пока счетчик меньше длины числа делаем цикл, для переборка каждой цифры
    num_1 = number%10           #на первой итерации получим последнюю цифру введенного числа
    number = number//10         #последняя цифра исходного числа записалась в checker, тут получим число без последней цифры
    if max < num_1:             #сравним начальный максимум с последней цифрой числа, на первой итерации они будут равны, со второй уже пойдет сравнение
        max = num_1             #если записанный максимум меньше последнего числа то записываем новый максимум как последнее число
    n = n + 1                   #увеличиваем счетчик

print(f'Максимум числа: {max}')     #выведи максимальное число