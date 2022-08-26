from selenium.webdriver.common.keys import Keys
from locators.google import MainPage
from helper.base_actions import BaseAction


class MainPageAction(BaseAction):

    def search_it(self, text):
        self.wait_elem(*MainPage.search)
        self.input(*MainPage.search, text + Keys.ENTER)

    def exist_mvideo(self):
        self.wait_elem(*MainPage.mvideo)
        element = self.find_element(*MainPage.mvideo)
        assert 'mvideo' in element.get_attribute("href")