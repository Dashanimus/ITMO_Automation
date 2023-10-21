import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# def test_site_visit():
#    driver = webdriver.Chrome()
#    driver.get("https://demoqa.com/")
#    try:
#        driver.find_element(By.CSS_SELECTOR, 'header > a > img')
#    except NoSuchElementException:
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

    button.click()
    time.sleep(3)

  # assert driver.current_url == 'https://demoqa.com/elements' -> Тест должен упасть, assertion error
    driver.quit()
