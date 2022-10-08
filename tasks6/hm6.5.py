# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
# draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить
# уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print(f'Запускаю отрисовку')

class Pen(Stationery):
    def draw(self):
        print(f'Запускаю отрисовку {self.title}')

pen1 = Pen('Ручкой')
pen1.draw()

class Pencil(Stationery):
    def draw(self):
        print(f'Запускаю отрисовку {self.title}')

pencil1 = Pencil('Карандашом')
pencil1.draw()

class Handle(Stationery):
    def draw(self):
        print(f'Запускаю отрисовку {self.title}')

handle1 = Handle('Маркером')
handle1.draw()