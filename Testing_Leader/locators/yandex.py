from selenium.webdriver.common.by import By

class MainPage:

    section_mail = (By.CSS_SELECTOR, '.home-link.desk-notif-card__login-new-item_mail')


class LoginPage:

    tab_login = (By.CSS_SELECTOR, 'button[data-type="login"]')
    login_input = (By.CSS_SELECTOR, ".Field[data-t='field:input-login']")
    password_input = (By.CSS_SELECTOR, ".Field[data-t='field:input-passwd']")
    button_sign_in = (By.CSS_SELECTOR, '#passp:sign-in')