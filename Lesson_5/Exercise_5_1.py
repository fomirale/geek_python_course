# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

my_f = open('file_ex_5_1.txt', 'w')
text = input('Введите текст ==>>\n ')
while text:
    my_f.writelines(text)
    text = input('Введите текст (или пустую строку для выхода) ==>>\n ')
    if not text:
        break

my_f.close()
my_f = open('file_ex_5_1.txt', 'r')
text_result = my_f.readlines()
print(text_result)
my_f.close()
