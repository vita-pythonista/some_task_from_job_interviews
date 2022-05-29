import logging
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, TimeoutException

logging.basicConfig(level=logging.INFO)

TIME_WAITING = 10

class BaseAction:
    """Простые действия для работы со страницами"""

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, type_locator, locator):
        """Поиск элемента по локатору"""
        try:
            element = WebDriverWait(self.driver, TIME_WAITING).until(EC.presence_of_element_located((type_locator, locator)))
            return element
        except TimeoutException:
            return self.driver.execute_script("return document.querySelector(arguments[0]);", locator)

    def find_elements(self, type_locator, locator):
        """Поиск элементов по локатору"""
        try:
            elements = WebDriverWait(self.driver, TIME_WAITING).until(EC.presence_of_all_elements_located((type_locator, locator)))
            return elements
        except TimeoutException:
            return self.driver.execute_script("return document.querySelectorAll(arguments[0]);", locator)

    def click(self,type_locator, locator):
        """Клик по элементу"""
        try:
            element = WebDriverWait(self.driver, TIME_WAITING).until(EC.element_to_be_clickable((type_locator, locator)))
            element.click()
        except WebDriverException:
            self.driver.execute_script("return document.querySelectorAll(arguments[0]);", locator)

    def wait_elem(self, type_locator, locator):
        """Ожидание элемента"""
        init = time.process_time()
        try:
            element = WebDriverWait(self.driver, TIME_WAITING).until(EC.visibility_of_element_located((type_locator, locator)))
            return element
        except TimeoutException:
            self.wait_of_finish_active_functions_on_page()
        end = time.process_time()
        return end - init

    def wait_of_finish_active_functions_on_page(self):
        """Счетчик ожидания окончания действия активных запросов на странице"""
        count = 0
        while count < 5:
            count += 1
            active_request = self.driver.execute_script("return $.active")
            while active_request != 0:
                active_request = self.driver.execute_script("return $.active")
                time.sleep(0.1)

    def input(self, type_locator, locator, text):
        element = self.find_element(type_locator, locator)
        element.clear()
        logging.info(f"Я собираюсь вводить текст {text} в поле веб элемента с таким локатором {locator}")
        element.send_keys(text)
        logging.info(f"Я ввёл текст {text} в поле веб элемента с таким локатором {locator}")