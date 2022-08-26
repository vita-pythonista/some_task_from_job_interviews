from pages.main_yandex import MainPageAction, AuthorizePage


def test_yandex_mail_authorize(browser):
    browser.get("https://www.yandex.ru")
    main = MainPageAction(browser)
    main.click_mail()
    authorize = AuthorizePage(browser)
    authorize.input_login('test-vitaly-aduchiev')
    authorize.click_btn_sign_in()
    authorize.input_password()