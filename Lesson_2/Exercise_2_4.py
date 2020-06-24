# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

new_string = input("Введите строку из нескольких слов ==>> ")
words = []
num = 1

for el in range(new_string.count(' ') + 1):
    words = new_string.split()
    if len(str(words)) <= 10:
        print(f" {num} {words[el]}")
        num += 1
    else:
        print(f" {num} {words[el][0:10]}")
        num += 1

