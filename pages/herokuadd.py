from components.components import WebElement
from pages.basepage import BasePage


class HerokuAdd(BasePage):
    def __init__(self, driver):
        self.base_url = 'http://the-internet.herokuapp.com/add_remove_elements/'
        super().__init__(driver, self.base_url)

        self.btn_add = WebElement(driver, '#content > div > button')
        self.btns_delete = WebElement(driver, '#elements > button')
