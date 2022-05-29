from selenium.webdriver.common.by import By

class MainPage:

    btn_enter = (By.CSS_SELECTOR, ".menu-wrapper .login-wrapper")

class WindowsEnterOrRegistration:

    enter_with_email = (By.CSS_SELECTOR, ".auth-link[data-form='email']")
    email_input = (By.CSS_SELECTOR, "input.input[name='email']")
    password_input = (By.CSS_SELECTOR, "input.input[name='password']")
    btn_submit = (By.CSS_SELECTOR, "button.auth-button[name='submit']")