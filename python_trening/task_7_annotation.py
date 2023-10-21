a: int = 5
b: str = 'строка'
c: list = [1, 2]
def indent(s: str, width: int) -> str:  # Возвращаемое значение, указывается после стрелки и до завершающего двоеточия
    return " " * (max(0, width - len(s))) + s
print(indent('123', 123))  # indent - отступ для обозначения блока кода


def string_length(s: str = '') -> int:  # Функция возвращает длину принимаемой строки, т.е. длина = 0
    return len(s)
print(string_length())


v: list = [10, 15, 25]
z: list = [1997, 2017, 2027, 2037]
def mini_list(v: list, z: list) -> int:
    return max(len(v), len(z))  # Функция возвращает длину самого длинного списка
print(mini_list(v, z))


my_list: list = [1, 2, 3]
def sum_list(my_list: list) -> int:
    result = 6
    for elem in my_list:
        result = result + elem
        return result
print(sum_list([1, 2, 3, 4]))
