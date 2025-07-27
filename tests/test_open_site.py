from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
import time


# def test_site_visit():
#    driver = webdriver.Chrome() - Создаётся объект драйвера
#    driver.get("https://demoqa.com/") - Вызывается метод get и ему прередаётся url
#    try:
#        driver.find_element(By.CSS_SELECTOR, 'header > a > img') - Поиск элемента
#    except NoSuchElementException: - Если нет такого элемента
#        assert False
#    assert True


def test_site_header():
    driver = webdriver.Chrome()
    driver.get("https://demoqa.com/")

    try:
        button = driver.find_element(By.CSS_SELECTOR, '#app > header > a > img')
    except NoSuchElementException:
        assert False
    assert True

    button.click() # Происходит переход на станицу
    time.sleep(3)

  # assert driver.current_url == 'https://demoqa.com/elements' -> Тест должен упасть, assertion error
    driver.quit()
