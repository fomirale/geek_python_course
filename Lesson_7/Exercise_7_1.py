# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        m = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                m[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in m]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in m]))


my_matrix = Matrix([[2, 13, 48],
                    [76, 11, 4],
                    [6, 53, 99]],
                   [[34, 2, 18],
                    [65, 43, 3],
                    [25, 9, 27]])

print(my_matrix.__add__())
