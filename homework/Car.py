class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def car_start(self):
        print('Автомобиль заведён')

    def car_stop(self):
        print('Автомобиль заглушён')

    def car_year(self):
        print(self.year)

    def car_type(self):
        print(self.type)

    def car_color(self):
        print(self.color)


car1 = Car('Красный', 'Лада Веста', 2020)
car1.car_start()
car1.car_stop()
car1.car_year()
car1.car_type()
car1.car_color()
