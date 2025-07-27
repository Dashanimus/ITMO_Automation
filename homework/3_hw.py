def compare_numbers(m: int, n: int):
    if m > n:
        print(m)
    elif m < n:
        print(n)
    else:
        print('Числа равны')

compare_numbers(35, 97)


def number_135(x, y): # Функция получает на вход два числа
    if x + 135 == y or x - 135 == y: # Если они отличаются друг от друга на 135
        print('YES')
    else:
        print('NO')

number_135(270, 135)


def month_season(month):
    if month == 1 or month == 2 or month == 12:
        print('Зима')
    elif month >= 3 and month <= 5:
        print('Весна')
    elif month >= 6 and month <= 8:
        print('Лето')
    elif month >= 9 and month <= 11:
        print('Осень')
    else:
        print('Такого месяца не существует, извини :(')

month_season(13)


def three_numbers(u: int, f: int, o: int):
    if u > 10 and f > 10 and o > 10: # Если все числа больше 10
        print('YES')
    else:
        print('NO')

three_numbers(51, 666, 99)


def positive_numbers(a, b, c, d):
    if a > 0 or b > 0 or c > 0 or d > 0:
        print('Количество положительных чисел = ', (a > 0) + (b > 0) + (c > 0) + (d > 0))
    else:
        print('Положительных чисел НЕТ')

positive_numbers(1, 2, -3, 4)


def year_days(year, month): # Функция получает количество лет и колчество месяцев
    if year >= 1 and month >= 1:
        print('Количество дней за это время = ', (year * 12 * 29) + (month * 29))
    else:
        print('Введите корректное значение')

year_days(5, 3)
