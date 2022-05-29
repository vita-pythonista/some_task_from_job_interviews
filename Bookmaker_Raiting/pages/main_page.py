from locators.main_page import MainPage, WindowsEnterOrRegistration as W_Enter
from helper.base_actions import BaseAction

class Main(BaseAction):

    def click_blue_button_enter(self):
        self.click(*MainPage.btn_enter)

    def click_auth_with_email(self):
        self.click(*W_Enter.enter_with_email)

    def input_email(self, email):
        self.input(*W_Enter.email_input, email)

    def input_password(self, password):
        self.input(*W_Enter.password_input, password)

    def click_submit_enter(self):
        self.click(*W_Enter.btn_submit)