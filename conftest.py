# Тестовые фреймворки предоставляют хуки - специальные функции, запускающиеся до и после тестов
# В Pytest называются фикстурами, conftest - зарезервированное слово, файл общий для всех тестов
from selenium import webdriver
import pytest


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(width=1000, height=600)
    yield driver # yield - возвращает последовательность значений по одному за раз, сохраняя свое состояние между вызовами
    driver.quit()
