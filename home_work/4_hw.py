class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height

    def perimetr(self):
        return (2 * self.width) + (2 * self.height)


rectangle1 = Rectangle(6, 9)
rectangle2 = Rectangle(35, 101)
rectangle3 = Rectangle(3, 118)

print(f'S1 = {rectangle1.square()} m^2')
print(f'S1 = {rectangle1.perimetr()} m^2')
print(f'S2 = {rectangle2.square()} m^2')
print(f'S2 = {rectangle2.perimetr()} m^2')
print(f'S3 = {rectangle3.square()} m^2')
print(f'S3 = {rectangle3.perimetr()} m^2')


class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addiction(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b


summary = Math(99, 81)
product = Math(0, 44)
quotient = Math(36, 6)
difference = Math(11, 43)

print(f"Сумма = {summary.addiction()}")
print(f'Произведение = {product.multiplication()}')
print(f'Частное = {quotient.division()}')
print(f'Разность = {difference.subtraction()}')


class Button:
    def __init__(self, text, type, loc):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        return f'Клик по кнопке {self.text}'


button_1 = Button('Text Box', 'Кнопка', ' ')
button_2 = Button('Check Box', 'Кнопка', ' ')
button_3 = Button('Radio Button', 'Кнопка', ' ')
button_4 = Button('Web Tables', 'Кнопка', ' ')
button_5 = Button('Buttons', 'Кнопка', ' ')

print(button_1.click())
print(button_2.click())
print(button_3.click())
print(button_4.click())
print(button_5.click())
