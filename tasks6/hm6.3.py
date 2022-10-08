# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position
# (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, wage, bonus): #добавили все атрибуты и оклад с бонусом
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self.my_dict = {
            'wage' : self.wage,
            'bonus' : self.bonus
        }   #оклад с бонусом запишу в словарь по ключам

class Position(Worker): #сабкласс позиция
    def get_full_name(self):
        return f'Полное имя: {self.name} {self.surname}' #метод - вывели имя и фамилию
    def get_total_income(self):
        self.__income = self.my_dict.get('wage') + self.my_dict.get('bonus') #метод вывели доход в защищенном атрибуте метода,
#!!!! не знаю мб в этой задаче я что-то не то делаю, мне так показалось проще... либо я смысла недопонял куда ставить словарь, а
        #куда атрибут __income?
        return f'Получает: {self.__income}'

worker1 = Position('Эмиль', 'Грабчук', 'Начальник смены', 95_000, 20_000) #объект сделали

print(worker1.get_full_name()) #получили полное имя по методу
print(f'Должность: {worker1.position}') #должность по атрибуту position
print(f'{worker1.get_total_income()} из них - оклад: {worker1.wage}, премия: {worker1.bonus}') #доход и тд