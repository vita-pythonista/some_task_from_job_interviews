from locators.yandex import MainPage, LoginPage
from helper.base_actions import BaseAction


class MainPageAction(BaseAction):

    def click_mail(self):
        self.click(*MainPage.section_mail)


class AuthorizePage(BaseAction):

    def input_login(self, login):
        self.click(*LoginPage.tab_login)
        self.input(*LoginPage.login_input, login)

    def click_btn_sign_in(self):
        self.click(*LoginPage.button_sign_in)

    def input_password(self, password):
        self.input(*LoginPage.password_input, password)