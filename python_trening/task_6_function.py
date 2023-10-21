# Функции - составные инструкции, принимают данные ввода, выполняют указания и возвращают данные вывода.
# Вызывать функцию - передать ей входные данные, необходимые для выполнения и возвращения результата.
# Входные данные - аргументы функции.
def arg(a, b, c=2, d=3):  # В скобках - аргументы функции
    return a + b + c + d  # return - инструкция, говорит, что нужно вернуть значение (сумма)

print(arg(1, 1, 1, 1))  # = 4
print(arg(2, 2))  # = 9


def range_arg(a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' + d

print(range_arg('1', '2', '3', '4'))
print(range_arg('1', '2', d='3', c='4'))


def task_func(a=(1, 2, 3, 4)):
    return a[0]

print(task_func())


def compute_surface(radius, pi=3.14159):
    return pi * radius * radius

print(compute_surface(2))


def append_list(my_list: list):
    my_list.append('test')
    return my_list

print(append_list(['один', 2, 3]))
