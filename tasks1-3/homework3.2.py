# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя,
# фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def user_data(name, surname, birthyear, city, email, phone, **kwargs): #принимаем на вход словарь и распаковываем по ключам в аргументы
    string=f'{name} {surname}, {birthyear}, {city}, {email}, {phone}' #вывод данных одной строкой
    return string

#получили словарь с данными пользователя
user = {
    'name':'Emil',
    'surname': 'Grabchuk',
    'birthyear': '1990',
    'city': 'Moscow',
    'email': 'emile90@mail.ru',
    'phone': '+7-903-138-35-51'
}

#засунули словарь в функцию и вывели данные одной строкой с помощью функции
print(user_data(**user))
