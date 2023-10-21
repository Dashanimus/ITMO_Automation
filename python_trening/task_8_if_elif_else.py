num = -5
if num >= 0:
    print('число больше либо равно 0')
else:
    print('отрицательное')


str_1 = 'test'
str_2 = 'test1'
if str_1 in str_2:
    print('test1 содержит test')
else:
    print('test1 не содержит test')


num_float = 3.4
if num_float > 0:
        print('положительное')
elif num_float == 0:
        print('ноль')
else:
        print('отрицательное')


permit_print = True
num = 1
if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена!')


def student_rank(year):
    if year >= 1 and year <= 4:
        print('Бакалавр')
    elif year >= 5 and year <= 6:
        print('Магистр')
    elif year >= 7 and year <= 9:
        print('Аспирант')
    else:
        print('Введите корректный год обучения!')
student_rank(10)

s = 200
if s > 100 or s < -100:
    print('-')
else:
    print('+')
