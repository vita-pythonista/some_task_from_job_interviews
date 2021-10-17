import time

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

language_picker = (By.CSS_SELECTOR, ".global-footer [name='language-picker']")
header_text = (By.CSS_SELECTOR, "#hero .col-lg-7 h1")


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find(self, by, selector):
        return self.driver.find_element(by, selector)

    def wait_of_finish_complete(self):
        self.driver.set_page_load_timeout(0.5)
        self.driver.execute_script("return document.readyState == 'complete'")

    def stop_load(self):
        self.driver.set_page_load_timeout(0.5)

    def scroll_to_element(self, by, selector):
        element = self.find(by, selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click(self, by, selector):
        self.find(by, selector).click()

    def select_by_text(self, by, selector, text):
        selected = Select(self.find(by, selector))
        selected.select_by_visible_text(text)

class Main(BaseAction):

    with allure.step("Загрузка списка языка"):
        def wait_language_picker(self):
            self.wait_of_finish_complete()

    def scroll_to_footer(self):
        self.scroll_to_element(*language_picker)

    def click_for_change(self):
        self.click(*language_picker)

    def select_by_language(self, language):
        self.select_by_text(*language_picker, language)

    def language_text_validation(self, text):
        self.stop_load()
        language_header_text = self.find(*header_text)
        assert language_header_text.text == text



class TestLanguage:

    with allure.step("Тест для немецкого языка"):
        def test_deutsch(self, browser):
            browser.get("https://trello.com")
            main = Main(browser)
            main.wait_language_picker()
            main.scroll_to_footer()
            main.click_for_change()
            time.sleep(5)
            main.select_by_language('Deutsch')
            main.language_text_validation("Trello hilft Teams, ihre Arbeit voranzutreiben.")

    def test_russian(self, browser):
        browser.get("https://trello.com")
        main = Main(browser)
        main.wait_language_picker()
        main.scroll_to_footer()
        main.click_for_change()
        main.select_by_language('Русский')
        main.language_text_validation("Trello помогает командам эффективно решать рабочие задачи.")

    def test_ucrain(self, browser):
        browser.get("https://trello.com")
        main = Main(browser)
        main.wait_language_picker()
        main.scroll_to_footer()
        main.click_for_change()
        main.select_by_language('Українська')
        main.language_text_validation("Trello допомагає командам виконувати роботу.")