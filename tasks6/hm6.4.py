# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и
# WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car: #класс тачка
    def __init__(self, speed, color, name, is_police : bool): #тут все атрибуты по заданию, is_police - bool
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self): #нужные метода
        print('Автомобиль едет')
    def stop(self):
        print('Автомобиль стоит')
    def turn(self, direction):
        self.direction = direction
    def show_speed(self):
        print(f'Текущая скорость машины {self.name} - {self.speed} км/ч')
        return self.speed

class TownCar(Car): #городская тачка - подкласс

    def __init__(self, speed, color, name, is_police = False): #по умолчанию не полицейская, но может ей стать?))
        super().__init__(speed, color, name, is_police) #все атрибуты забрали от родителя, возможно этих двух строчек тут не нужно
        #т.к. нет новых атрибутов подкласса
    def show_speed(self):
        if self.speed > 60:
            print(f'Текущая скорость: {self.speed} превысит ограничение = 60км/ч')
        else:
            print('Превышения скорости нет') #проверка скорости, если больше 60 напишем об этом, если нет, то все ок


class WorkCar(Car): #рабочая тачка

    def __init__(self, speed, color, name, free_space = 100, is_police = False):
        self.free_space = free_space #добавим атрибут свободное место в грузовом отсеке, по умолчанию 100
        super().__init__(speed, color, name, is_police)
    def load_car(self, cargo): #метод - загрузить тачку
        self.free_space -= cargo #свободное минус загруженное
        print(f'Загрузили в тачку {self.name}: {cargo}') #выведем для наглядности
        print(f'Осталось места под груз: {self.free_space}') #выведем для наглядности
    def show_speed(self):
        if self.speed > 40:
            print(f'Текущая скорость: {self.speed} превысит ограничение = 40км/ч')
        else:
            print('Превышения скорости нет') #переопределим метод шоу спид для 40 км в ч

class SportCar(Car): #спорт тачка
    def __init__(self, speed, color, name, nitro_oxide_supply = 200, is_police = False):
        self.nitro_oxide = nitro_oxide_supply #свой атрибут - запас закиси азота))) по умолчанию 200
        super().__init__(speed, color, name, is_police)
    def afterburner_N2O(self, usage_N2O): #метод будем использовать форсаж
        self.speed = self.speed + 0.1 * usage_N2O #когда заюзаем форсаж то скорость увеличится в км на 10% от использованного кол-ва закиси азота
        self.nitro_oxide -= usage_N2O #снизим запасы азота
    def max_speed(self): #метод - ограничитель скорости спортивной тачки
        if self.speed > 210:
            print('Максимальная скорость спортТачки - 210')
            self.speed = 210 #если скорость больше 210 напишем об этом и сделаем ее равной 210
    def show_nitro_supply(self):
        print(f'Запас нитро в {self.name} = {self.nitro_oxide}') #отдельно покажем запас нитро для удобства и в какой именно тачке

class PoliceCar(Car): #Полицейская тачка
    def __init__(self, speed, color, name, is_police = True):
        super().__init__(speed, color, name, is_police)
    def max_speed(self):
        if self.speed > 320:
            print('Максимальная скорость Полицейской тачки - 320')
            self.speed = 320 #у нее скорость побольше но нет Нитро, также есть ограничитель в 320км в ч
    def signals(self):
        print(f'Сирена и мигалки на {self.name} включены!') #умеет включать сигналки и серену

lada_priora = TownCar(55, 'white', 'Лада Приора') #объект Лада, городская тачилла
lada_priora.show_speed() #покажет что со скоростью все ок
lada_priora.speed = 76 #увеличим скорость
lada_priora.show_speed() #покажет, что скорость превышена это плохо, можно запустить метод поличейской тачки о вкл сирены, но она еще не создана)))
print(f'Является ли тачка {lada_priora.name} полицейской: {lada_priora.is_police}') #проверим, что она не полицейская

#грузовая машина
gazel = WorkCar(30, 'blue', 'Газелист')
gazel.show_speed()
gazel.speed = 44
gazel.show_speed() #предупреждение скорости работает также как у городской
print(f'Свободного места под груз: {gazel.free_space}') #сколько места под загруз?
gazel.load_car(40) #загрузили машину 40 юнитами груза


nissan350z = SportCar(200, 'red_fire', 'Ниссан 350z') #создадим спорт тачку, скорость 200
nissan350z.show_nitro_supply() #посмотрим сколько осталось нитро
nissan350z.afterburner_N2O(50) #используем форсаж
nissan350z.show_speed()  #проверим скорость, будет уже 205
nissan350z.show_nitro_supply() #проверим запасы нитро
nissan350z.afterburner_N2O(100) #дадим еще 100 нитро на форсаж
nissan350z.show_speed() #покажем скорость с род. класса уже будет 215, а у спорт ограничение 210
nissan350z.max_speed() #вступает метод ограничивающий скорость 215 до 210
nissan350z.show_speed() #и да действительно убедились в этом


doge_viper = PoliceCar(300, 'black', 'Додж Вайпер') #создали полицейскую тачку скорость 300
doge_viper.show_speed()
doge_viper.speed = 350 #разогнались до 350
doge_viper.max_speed() #вступил в работу ограничитель
doge_viper.show_speed()
doge_viper.signals()  #включим сигналы
print(f'Является ли тачка {doge_viper.name} полицейской: {doge_viper.is_police}!!!')

#тут вот еще подумаю как похожие методы разных дочерних классов не копировать целиком, а как-то переопределять, это
#ведь правильнее будет? Разбор ДЗ еще не смотрел мб там есть)
