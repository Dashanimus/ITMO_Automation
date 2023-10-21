class Soda:
    def __init__(self, ing=None):
        self.ing = ing

    def show_my_drink(self):
        if self.ing:
            print(f'Газировка со вкусом {self.ing}')
        else:
            print('Обычная газировка')

drink1 = Soda()
drink2 = Soda('WildBerry')
drink1.show_my_drink()
drink2.show_my_drink()
