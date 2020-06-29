# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(num_1, num_2):
    try:
        result = num_1 / num_2
    except ZeroDivisionError:
        return "Деление на 0!"
    return result


num_1 = int(input("Введите первое число ==>> "))
num_2 = int(input("Введите второе число ==>> "))
print(division(num_1, num_2))
