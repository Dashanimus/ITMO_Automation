from selenium.webdriver.common.by import By
from selenium import webdriver


def test_site_visit():
    driver = webdriver.Chrome() # Создаётся объект драйвера
    driver.get("http://www.saucedemo.com") # Вызывается метод get и ему прередаётся url

    username = driver.find_element(By.CSS_SELECTOR, '#user-name')
    password = driver.find_element(By.CSS_SELECTOR, '#password')
    login = driver.find_element(By.CSS_SELECTOR, '#login-button')

    if username and password and login:
        print('Элементы найдены')
    else:
        print('Элементы не найдены')
