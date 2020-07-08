# 4. Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def summ():
    try:
        with open('file_ex_5_4.txt', 'w+') as file_obj:
            line = input('Введите набор чисел, разделенных пробелами ==>> \n')
            file_obj.writelines(line)
            numbers = line.split()

            print(sum(map(int, numbers)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильный ввод набора.')


summ()
