def sravni(q: int, w: int):
    if q > w:
        print(q)
    elif q < w:
        print(w)
    else:
        print('числа равны')

sravni(35, 97)


def number_135(x, y):
    if x + 135 == y or x - 135 == y:
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


def tri_chisla(n: int, l: int, o: int):
    if n > 10 and l > 10 and o > 10:
        print('YES')
    else:
        print('NO')

tri_chisla(51, 666, 99)


def six_task(a, b, c, d):
    if a > 0 or b > 0 or c > 0 or d > 0:
        print('Количество положительных чисел = ', (a > 0) + (b > 0) + (c > 0) + (d > 0))
    else:
        print('Положительных чисел НЕТ')

six_task(1, 2, -3, 4)


def yearday(year, month):
    if year >= 1 and month >= 1:
        print('Количество дней за это время = ', (year * 12 * 29) + (month * 29))
    else:
        print('Введите корректное значение')

yearday(5, 3)
