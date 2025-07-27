class Page:
    def __init__(self, url):  # Класс Page принимает 1 аргумент при инициализации url
        self.url = url
    def get(self):  # Метод get, который выводит на печать url
        print(self.url)

home = Page('https://demoqa.com')  # Объект класса Page
home.get()
