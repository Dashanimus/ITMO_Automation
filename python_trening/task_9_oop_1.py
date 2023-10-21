class Input:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

search = Input('ПОИСК', 'input#search')
print('Здесь просто выводится локатор', search.loc)


class Button:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

click = Button('КНОПКА', 'button#loc')
print(click.text, click.loc)


class Title:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

title = Title('ТАЙТЛ', 'title#loc')
print(title.text, title.loc)


class Link:
    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

link = Link('ССЫЛКА', 'link#loc')
print(link.text, click.loc)
