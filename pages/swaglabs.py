from selenium.common.exceptions import NoSuchElementException
from pages.saucedemo import SauseDemo


class SwagLabs(SauseDemo):
    def exist_icon(self):
        try:
            self.find_element(locator='div.login_logo')
        except NoSuchElementException:
            return False
        return True
