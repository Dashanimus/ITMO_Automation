a: int = 3
b: float = 10.25
c: str = "это строка"
d: list = [10, 15, 20, 25]
e: bool = 13 > 12
def task_1(a: int, b: float, c: str, d: list, e: bool): # Аннотация возвращаемых данных
    return a, b, c, d, e
print(task_1(a, b, c, d, e)) # Вызов функции


def task_2():
    n = [1, 2, 3, 4, 5, 8, 13, 21] # Эта последовательность - список
    return n[0:3]
print(task_2())


x: int = 9
z: int = 2
def task_3(x: int, z: int): # Функция принимает число и возвращает его квадрат
    return x ** z
print(task_3(x, z))
