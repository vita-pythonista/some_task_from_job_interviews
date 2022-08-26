import logging
import datetime

from selenium.webdriver.support.events import AbstractEventListener  # биб-ка для задачи для определенных действий

logging.basicConfig(level=logging.INFO)


class DriverListener(AbstractEventListener):
    """Получение логгинга действий вебдрайвера"""

    def before_navigate_forward(self, driver):
        logging.info("Я перехожу вперед через ->")

    def after_navigate_forward(self, driver):
        logging.info("Я перешёл вперед через ->")

    def before_find(self, by, value, driver):
        logging.info(f"Я ищу веб-элемент по следующему значению локатора {value}")

    def after_find(self, by, value, driver):
        logging.info(f"Я нашел веб-элемент по следующему значению локатора {value}")

    def before_click(self, element, driver):
        logging.info(f"Я собираюсь кликнуть на элемент с локатором {element}")

    def after_click(self, element, driver):
        logging.info(f"Я кликнул на элемент с локатором {element}")

    def before_change_value_of(self, element, driver):
        pass

    def after_change_value_of(self, element, driver):
        pass

    def before_execute_script(self, script, driver):
        logging.info(f"Я собираюсь выполнить js-скрипт {script}")

    def after_execute_script(self, script, driver):
        logging.info(f"Я выполнил js-скрипт {script}")

    def before_close(self, driver):
        logging.info("Я закрываю браузер")

    def after_close(self, driver):
        logging.info("Я закрыл браузер")

    def before_quit(self, driver):
        logging.info("Я выхожу из выполнения кода")

    def after_quit(self, driver):
        logging.info("Я вышел из выполнения кода")

    def on_exception(self, exception, driver):
        logging.info(f"Упс...произошла ошибка {exception}!")
