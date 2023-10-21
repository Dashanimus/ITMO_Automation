a: int = 3
b: float = 10.25
c: str = "это строка"
d: list = [10, 15, 20, 25]
e: bool = 13 > 12
def task_1(a: int, b: float, c: str, d: list, e: bool):
    return a, b, c, d, e
print(task_1(a, b, c, d, e))


def task_2():
    a = [1, 2, 3, 4, 5, 8, 13, 21]
    return a[0:3]
print(task_2())


u: int = 9
t: int = 2
def task_3(u: int, t: int):
    return u ** t
print(task_3(u, t))
