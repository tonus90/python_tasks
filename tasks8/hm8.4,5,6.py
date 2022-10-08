# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
# данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

"""
С помощью программы можно генерировать разное кол-во техники трех типов: сканер, принтер, ксерокс
и сохранять их в список эти объекты, атрибуты объектов формируются случайным образом, для каждого типа
атрибуты отличаются, но значения атрибутов комбинируются.
Можно передавать из списка объекты на склад в словарь, где ключ - название техники, значение -
список объектов.
Можно со склада забирать технику и передавать в отделы, и выводить словарь, где ключ -
название отдела, значение - словарь, в котором ключ - название техники, значение - список объектов этого типа
Также сделана примитивная логика реботы любого принтера, сканера, ксерокса.
Например. Могу вызвать объект принтер1 и через метод printer_logic(10) засуну ему 10 листов на печать,
в консоле он покажет, что их печатает. По логике: к примеру ч/б лазерный принтер печатает быстрее
чем цветной струйный и тд. По времени работы все настроено также и для сканеров и для ксероксов.
У принтеров есть запас чернил, который уменьшается с каждым листом, и система подачи чернил - струйная, лазер. У сканера
есть режимы сканирования - цветной/черно-белый. У ксерокса есть атрибуты как принтеров так и сканеров.
То есть в программе есть бизнес логика склада с конкретными результатами - словарями и логика работы оргтехники
в зависимости от нагенеренных параметров.
"""
from abc import ABC, abstractmethod
from time import sleep, time
from random import choice
import copy as c

class OrgWarehouse():
    def __init__(self, capacity):
        self.capacity = capacity
        self.get_dict = {}
        self.take_out_dict = {}
        self.item_list1 = []
        self.item_list2 = []
        self.item_list3 = []
        self.list_for_buh = []
        self.list_for_analit = []
        self.list_for_it = []

    def for_str(self):
        try:
            a = len(type(self.get_dict.get("Принтеры")))
        except TypeError:
            print('Ошибка! Принтеров еще не завезли на склад')
            a=0
        return f'Сканеров: {len(self.get_dict.get("Сканеры"))}, Принтеров: {a} Ксероксов: ' \
               f'{len(self.get_dict.get("Ксероксы"))}'

    def get_in(self, items, cnt):
        my_list = []
        if type(cnt) == str:
            raise GetInException('Ошибка, число принтеров должно быть int, а не str')

        for i in range(1, cnt+1, 1):
            my_list.append(items.pop())

        if type(my_list[0]) == Printer:
            for i in my_list:
                self.item_list1.append(i)
                self.capacity -= 1
            self.get_dict['Принтеры'] = self.item_list1
        elif type(my_list[0]) == Scaner:
            for i in my_list:
                self.item_list2.append(i)
                self.capacity -= 1
            self.get_dict['Сканеры'] = self.item_list2
        elif type(my_list[0]) == Xerox:
            for i in my_list:
                self.item_list3.append(i)
                self.capacity -= 1
            self.get_dict['Ксероксы'] = self.item_list3


        return self.get_dict

    def __str__(self):
        return f'На складе вот такая орг техника:\n {self.for_str()} и места: {self.capacity}'

    def take_out(self, dep, type_of, cnt):
        my_dict = {}
        if dep == 'Бухгалтерия':
            for i in range(cnt):
                self.list_for_buh.append(self.get_dict.get(type_of).pop())
                my_dict[type_of] = self.list_for_buh
                self.capacity += 1
        if dep == 'Аналитика':
            for i in range(cnt):
                self.list_for_analit.append(self.get_dict.get(type_of).pop())
                my_dict[type_of] = self.list_for_analit
                self.capacity += 1
        if dep == 'IT':
            for i in range(cnt):
                self.list_for_it.append(self.get_dict.get(type_of).pop())
                my_dict[type_of] = self.list_for_it
                self.capacity += 1
        self.take_out_dict[dep] = c.deepcopy(my_dict)

        return self.take_out_dict
    #Нижний метод в разработке, он должен вернуть, сколько какой техники в департаментах, отделах, но скорее всего такой метод
    #лучше реализовать на базе классов отделов.
    # def what_in_departments(self):
    #     return f'В отделе Бухгалтерии такая оргтехника: \nСканеров: {len(self.take_out_dict.get("Бухгалтерия").get("Сканеры"))} ' \
    #            f'Принтеров: {len(self.take_out_dict.get("Бухгалтерия").get("Принтеры"))} Ксероксов: {len(self.take_out_dict.get("Бухгалтерия").get("Ксероксов"))}\n' \
    #            f'В отделе Аналитики такая оргтехника: \nСканеров: {len(self.take_out_dict.get("Аналитика").get("Сканеры"))} ' \
    #            f'Принтеров: {len(self.take_out_dict.get("Аналитика").get("Принтеры"))} Ксероксов: {len(self.take_out_dict.get("Аналитика").get("Ксероксов"))}\n' \
    #            f'В отделе IT такая оргтехника: \nСканеров: {len(self.take_out_dict.get("IT").get("Сканеры"))} ' \
    #            f'Принтеров: {len(self.take_out_dict.get("IT").get("Принтеры"))} Ксероксов: {len(self.take_out_dict.get("IT").get("Ксероксов"))}\n'

class GetInException(Exception):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

class OrgTechnic(ABC):
    def __init__(self, name, price, color):
        self.name = name
        self.price = price
        self.color = color

    @abstractmethod
    def print(self, cnt_paper, time_print):
        pass

    @abstractmethod
    def scan(self,  cnt_paper, time_scan):
        pass

class Printer(OrgTechnic):
    type_org = 'Printer'
    def __init__(self, name, price, color, colorful, ink_system, ink_capacity):
        super().__init__(name, price, color)

        self.colorful = colorful
        self.ink_system = ink_system
        self.ink_capacity = ink_capacity

    def print(self, cnt_paper, time_print):
        my_list = [el for el in range(1, cnt_paper, 1)]
        time_cnter = 0
        printed_list = []
        for i in my_list:
            print(f'Печатаю лист {i}')
            a = time()
            sleep(time_print)
            time_cnter += time_print
            b = time()
            if b-a > b+2:
                try:
                    raise RuntimeError('Произошло Замятие бумаги, вытащите бумагу и перезапустите')
                except RuntimeError as err:
                    print(err)
            printed_list.append(i)
            print(f'Напечатал лист {i}')
            self.ink_capacity -= 2
        return print(f'Напечатал {len(printed_list)+1} листов за {int(time_cnter)} секунд')

    def scan(self,  cnt_paper, time_scan):
        pass

    def print_logic(self, lists):
        my_dict1 = {
            'цветной': 1.2,
            'чб': 0.6,
        }
        my_dict2 = {
            'лазер': 0.5,
            'струйный': 1
        }

        time_c = my_dict1.get(self.colorful)
        time_i = my_dict2.get(self.ink_system)
        summ_time = time_c+time_i
        return self.print(lists, summ_time)

    def __str__(self):
        return f'Параметры принтера. Фирма: {self.name}, Стоимость: {self.price}р., Цвет: {self.color}, Чернила: {self.ink_system} Запас чернил: {self.ink_capacity}, Цвет/ЧБ: {self.colorful}'

class Scaner(OrgTechnic):
    type_org = 'Scaner'
    def __init__(self, name, price, color, scan_mode):
        super().__init__(name, price, color)

        self.scan_mode = scan_mode


    def scan(self, cnt_paper, time_scan):
        my_list = [el for el in range(1, cnt_paper, 1)]
        time_cnter = 0
        scan_list = []
        for i in my_list:
            print(f'Сканирую лист {i}')
            sleep(time_scan)
            time_cnter += time_scan
            scan_list.append(i)
            print(f'Отсканировал лист {i}')
        return print(f'Отсканировано {len(scan_list)} листов за {int(time_cnter)} секунд. Листы записаны в память.')

    def print(self, cnt_paper, time_print):
        pass

    def scan_logic(self, lists):
        my_dict1 = {
            'цветной': 3,
            'чб': 1.5
        }
        time_s = my_dict1.get(self.scan_mode)
        return self.scan(lists+1, time_s)

    def __str__(self):
        return f'Параметры Сканера. Фирма: {self.name}, Стоимость: {self.price}р., Цвет: {self.color}, Скан - цвет/чб: {self.scan_mode}'

class Xerox(OrgTechnic):
    type_org = 'Xerox'
    def __init__(self, name, price, color, colorful, ink_system, ink_capacity, scan_mode):
        super().__init__(name, price, color)
        self.colorful = colorful
        self.ink_system = ink_system
        self.ink_capacity = ink_capacity
        self.scan_mode = scan_mode

    def scan(self, cnt_paper, time_scan):
        my_list = [el for el in range(1, cnt_paper, 1)]
        time_cnter = 0
        scan_list = []
        for i in my_list:
            print(f'Сканирую листов {i}')
            sleep(time_scan)
            time_cnter += time_scan
            scan_list.append(i)
        return print(f'Отсканировал листов {len(scan_list)}')

    def print(self, cnt_paper, time_print):
        my_list = [el for el in range(1, cnt_paper, 1)]
        time_cnter = 0
        printed_list = []
        for i in my_list:
            print(f'Печатаю лист {i}')
            a = time()
            sleep(time_print)
            time_cnter += time_print
            b = time()
            if b-a > b+2:
                try:
                    raise RuntimeError('Произошло Замятие бумаги, вытащите бумагу и перезапустите')
                except RuntimeError as err:
                    print(err)
            printed_list.append(i)
            self.ink_capacity -= 2
        return print(f'Напечатал листов {len(printed_list)}')

    def logic_xerox(self, lists):
        my_dict1 = {
            'цветной': 1.2,
            'чб': 0.6,
        }
        my_dict2 = {
            'лазер': 0.5,
            'струйный': 1
        }
        my_dict3 = {
            'цветной': 3,
            'чб': 1.5,
        }

        time_c = my_dict1.get(self.colorful)
        time_i = my_dict2.get(self.ink_system)
        time_s = my_dict3.get(self.scan_mode)
        time_p = time_c+time_i
        time_copy = time_p +time_s
        self.scan(lists+1, time_s)
        self.print(lists+1, time_p)
        return print(f'Откопировано {lists} листов за {int(time_copy)} секунд.')

    def __str__(self):
        return f'Параметры Xeroxa. Фирма: {self.name}, Стоимость: {self.price}р., Цвет: {self.color}, ' \
               f'Скан - цвет/чб: {self.scan_mode}, Печать - цвет/чб: {self.colorful}, Чернила: {self.ink_system}, ' \
               f'Запас чернил: {self.ink_capacity}'

class GenObj():
    def __init__(self, cnt, mode):
        self.cnt = cnt
        self.mode = mode.lower()
    def generate_params(self):
        name = ['Sony', 'Epson', 'Cannon', 'HP', 'Kyocera', 'Xerox']
        price = [3000, 4000, 5000, 6000, 9000]
        color = ['white', 'black', 'blue', 'gray']
        colorful = ['цветной', 'чб']
        ink_system = ['лазер', 'струйный']
        ink_capacity = [100, 150, 200]
        scan_mode = ['цветной', 'чб']
        print_params = [name, price, color, colorful, ink_system, ink_capacity]
        name_list = ['name', 'price', 'color', 'colorful', 'ink_system', 'ink_capacity']
        p_dict = {}
        if self.mode == 'x':
            print_params.append(scan_mode)
            name_list.append('scan_mode')
        elif self.mode == 's':
            print_params.remove(colorful)
            print_params.remove(ink_system)
            print_params.remove(ink_capacity)
            print_params.append(scan_mode)
            name_list.remove('colorful')
            name_list.remove('ink_system')
            name_list.remove('ink_capacity')
            name_list.append('scan_mode')
        for i in range(len(name_list)):
            p_dict[name_list[i]] = choice(print_params[i])
        return p_dict

    def generate_obj(self):
        list_obj = []
        if self.mode == 'p':
            for i in range(self.cnt):
                obj = Printer(**self.generate_params())
                list_obj.append(obj)
        elif self.mode == 'x':
            for i in range(self.cnt):
                obj = Xerox(**self.generate_params())
                list_obj.append(obj)
        elif self.mode == 's':
            for i in range(self.cnt):
                obj = Scaner(**self.generate_params())
                list_obj.append(obj)
        return list_obj

objects_p = GenObj(6, 'p') #есть класс GenObj создаем объект генератора, куда кладем инфу сколько объектов создать и
#какого типа 'p'-принтер, 's' - сканер, 'x' - ксерокс
printers = objects_p.generate_obj() #генерируем 6 принтеров в список, с помощью метода

objects_s = GenObj(5, 's') #тоже самое дял сканеров
scaners = objects_s.generate_obj() #генерируем 5 сканеров
print(scaners) #убедились, что они создались

objects_x = GenObj(4, 'x')
xeroxes = objects_x.generate_obj() #нагенерили 4 ксерокса

warehouse1 = OrgWarehouse(30) #создали склад на 30 мест
print(warehouse1.get_in(scaners, 3)) #добавим из имеющихся 3 сканера в словарь ключ - "Сканеры" значение -
# лист с объектами сканер и посмотрим через принт
print(warehouse1.get_in(scaners, 2))#добавим еще 2 сканера

try:
    print(warehouse1.get_in(printers, '5')) #добавим 5 принтеров, но введем вместо инт - строку, получим сообщение об
    #ошибке, но не отвалимся
except GetInException as err:
    print(err)

print(warehouse1.get_in(xeroxes, 3)) #добавим 3 ксерокса из имеющихся
print(scaners)
print(printers)
print(xeroxes) #убедимся, что у нас осталось меньшее кол-во орг техники, на величину, забранную на склад


print(warehouse1) #посмотрим, что на складе, получим сообщ, что принтеров на складе нет, сканеров - 5, ксероксов - 3

#зарабнная техника хранится в словаре ключ - название отдела, значение - словарь с ключами название оргтехники, значение - листы объектов
print(warehouse1.take_out('Бухгалтерия', 'Сканеры', 2)) #заберем со склада 2 сканера и отправим их в бухгалетриюв
print(warehouse1.take_out('Бухгалтерия', 'Сканеры', 1)) #еще 1 в бух-ю
print(warehouse1.take_out('Аналитика', 'Сканеры', 1)) #один сканер в отдел Аналитики
print(warehouse1.take_out('IT', 'Сканеры', 1)) #и один айтишникам, останется на складе 0 сканеров

print(warehouse1.take_out('Аналитика', 'Ксероксы', 1)) #аналитикам 1 ксерокс
print(scaners) #увидим еще раз, что сканеров - пустой лист
print(warehouse1) #что осталось на складе после передачи отделам

#Создам еще сканер, тк все отдал на скад и со склада в отделы:
scaners_new = GenObj(1, 's') #создал 1 объект генератора
scaner1 = scaners_new.generate_obj()[0] #с помощью метода generate_obj сделал сканер и вытащил его с индексом 0

scaner1.scan_logic(4) #сканер работает, засунул ему 4 листа для скана, можно убедиться

printer1 = printers[0] #вытащил из листа принтеров 1 принтер
printer1.print_logic(10) #аставил печатать его 10 листов

xerox1 = xeroxes[0] #вытащу ксерокс
xerox1.logic_xerox(3) #отксерю 3 листа, все работает, все круто.
