# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого
# проекта —
# одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
# соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
# классы для основных классов проекта, проверить на практике работу декоратора @property.

class Cloths:
    def __init__(self, param, name = 'Всей одежды'):
        self.name = name
        self.param = param
    def summ(self):
        if self.name == 'Пальто':
            summ = self.param/6.5+0.5
            return round(summ, 1)
        elif self.name == 'Костюма':
            summ = 2*self.param+0.3
            return round(summ, 1)
        elif self.name == 'Всей одежды':
            summ = self.param
            return round(summ, 1)
    def __add__(self, other):
        return Cloths(self.summ()+other.summ())
    def __str__(self):
        return f'На изготовление {self.name} уйдет {round(self.param, 1)}м ткани.'


class Coat(Cloths):
    def __init__(self, param, name='Пальто'):
        super().__init__(param, name)
    def __str__(self):
        return f'На изготовление {self.name} уйдет {round(self.summ(), 1)}м ткани.'

class Suit(Cloths):
    def __init__(self, param, name='Костюма'):
        super().__init__(param, name)
    def __str__(self):
        return f'На изготовление {self.name} уйдет {round(self.summ(), 1)}м ткани.'



coat1 = Coat(46.5)
suit1 = Suit(1.8)
coat2 = Coat(50)
print(coat1)
print(suit1)
print(coat2)
print(coat1+suit1+coat2)
