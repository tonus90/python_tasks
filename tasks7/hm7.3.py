# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
# инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление
# (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное
# (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
# нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
# двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек
# этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод
# позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
# *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
# *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.

class Cell:
    def __init__(self, cnt_cell):
        self.cell = cnt_cell
    def __str__(self):
        return f'Ячеек в полученной клетке: {self.cell}'
    def __add__(self, other):
        return Cell(self.cell + other.cell)
    def __sub__(self, other):
        try:
            if self.cell>=other.cell:
                return Cell(self.cell - other.cell)
            else:
                raise ValueError('Первая клетка должна быть больше второй, чтобы вычесть и что-то осталось!!!!')
        except ValueError:
            print('Первая клетка должна быть больше второй, чтобы вычесть и что-то осталось!!!!')
    def __mul__(self, other):
        return Cell(self.cell*other.cell)
    def __truediv__(self, other):
        return Cell(self.cell//other.cell)
    def make_order(self, n_row):
        self.n_row = n_row
        ost = self.cell%self.n_row
        rows = self.cell//self.n_row
        a = str()
        for i in range(0, rows, 1):
            a += f'{"*"*self.n_row}\n'

        return f'{a}{"*"*ost}'

cell1 = Cell(23)
cell2 = Cell(5)
print(cell1+cell2)
print(cell1-cell2)
print(cell1/cell2)
print(cell1.make_order(5))
