from locators.main_page import MainPage, WindowsEnterOrRegistration as W_Enter
from helper.base_actions import BaseAction
import time

class Main(BaseAction):

    def click_blue_button_enter(self):
        self.click(*MainPage.btn_enter)
        time.sleep(1)

    def click_auth_with_email(self):
        self.click(*W_Enter.enter_with_email)
        time.sleep(1)

    def input_email(self, email):
        self.input(*W_Enter.email_input, email)
        time.sleep(1)

    def input_password(self, password):
        self.input(*W_Enter.password_input, password)
        time.sleep(1)

    def click_submit_enter(self):
        self.click(*W_Enter.btn_submit)
        time.sleep(1)
