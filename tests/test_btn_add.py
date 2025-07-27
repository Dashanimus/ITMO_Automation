from pages.herokuadd import HerokuAdd
from pages.herokuapp import HerokuApp


def test_herokuapp_add(browser):
    heroku_page = HerokuApp(browser)
    heroku_btn = HerokuAdd(browser)

    heroku_page.visit()
    assert heroku_page.link_add.get_text() == 'Add/Remove Elements'
    heroku_page.link_add.click()

    assert heroku_btn.btn_add.get_text() == 'Add Element'

    assert heroku_btn.btn_add.get_dom_attribute('onclick') == 'addElement()'

    # Кликнуть на кнопку 4 раза
    for i in range(4):
        heroku_btn.btn_add.click()

    assert heroku_btn.btns_delete.check_count_elements(4)

    # Проверка для всех элементов
    for element in heroku_btn.btns_delete.find_elements():
        assert element.text == 'Delete'

    # Проверка только для первого элемента
    # assert koup_add.btns_delete.get_text() == 'Delete'

    # Кликнуть на каждую кнопку -> Delete, клик, пока есть кнопка
    while heroku_btn.btns_delete.exist():
        heroku_btn.btns_delete.click()

    assert not heroku_btn.btns_delete.exist()
