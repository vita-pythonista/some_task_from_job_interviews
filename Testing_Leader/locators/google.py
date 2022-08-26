from selenium.webdriver.common.by import By


class MainPage:

    search = (By.CSS_SELECTOR, "[name='q']")
    mvideo = (By.PARTIAL_LINK_TEXT, "М.Видео")