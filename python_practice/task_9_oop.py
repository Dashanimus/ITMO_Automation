class Button:
    def __init__(self, text, link):
        self.text = text
        self.link = link

home = Button('ДОМОЙ', '/home')
catalog_msk = Button('КАТАЛОГ', '/msk/catalog')

print(home.text)
print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)

print('\n')

print(catalog_msk.text)
print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)


class ButtonTwo:
    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc
    def click(self):
        return "Клик по локатору - {}".format(self.loc)

home_two = ButtonTwo('ДОМОЙ', '/home', 'Button#home')

print(home_two.click())
