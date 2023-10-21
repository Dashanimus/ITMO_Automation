from selenium.webdriver.common.by import By
from selenium import webdriver


def test_site_visit():
    driver = webdriver.Chrome()
    driver.get("http://www.saucedemo.com")

    a = driver.find_element(By.CSS_SELECTOR, '#user-name')
    b = driver.find_element(By.CSS_SELECTOR, '#password')
    c = driver.find_element(By.CSS_SELECTOR, '#login-button')

    if a and b and c:
        print('Элементы найдены')
    else:
        print('Элементы не найдены')
