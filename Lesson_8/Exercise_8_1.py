# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'Всё ОК'
                else:
                    return f'Некорректное значение года'
            else:
                return f'Некорректное значение месяца'
        else:
            return f'Некорректное значение дня'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'


today = Data('21 - 07 - 2020')
print(today)
print(Data.valid(11, 11, -1907))
print(today.valid(21, 13, 2009))
print(Data.extract('25 - 05 - 1991'))
print(today.extract('21 - 07 - 2020'))
print(Data.valid(21, 7, 2020))
