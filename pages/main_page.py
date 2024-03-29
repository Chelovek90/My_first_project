from .base_page import BasePage

from .locators import MainPageLocators
from .locators import LoginPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.is_element_present(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "login link is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"
