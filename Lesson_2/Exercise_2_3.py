# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

season_list = ['зима', 'весна', 'лето', 'осень']
season_dict = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}
month_num = int(input("Введите месяц в виде целого числа от 1 до 12 ==> "))
if month_num in (12, 1, 2):
    print(season_dict.get(1))
    print(season_list[0])
elif month_num in (3, 4, 5):
    print(season_dict.get(2))
    print(season_list[1])
elif month_num in (6, 7, 8):
    print(season_dict.get(3))
    print(season_list[2])
elif month_num in (9, 10, 11):
    print(season_dict.get(4))
    print(season_list[3])
else:
    print("Число должно быть в диапазоне от 1 до 12!")
