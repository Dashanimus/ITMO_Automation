a = 5
print(a, "Относится к типу ", type(a))

b = 15.0001
print(b, "Относится к типу ", type(b))

c = 1+5j
print(c, "Комплексное число? ", isinstance(c, complex))  # isinstance - проверка указанного класса
