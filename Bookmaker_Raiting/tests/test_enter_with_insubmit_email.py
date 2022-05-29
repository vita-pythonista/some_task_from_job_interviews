from pages.main_page import Main

class TestEnterWithInsubmitEmail:

    def test_1(self, browser):
        browser.get("https://bookmaker-ratings.ru/")
        main = Main(browser)
        main.click_blue_button_enter()
        main.click_auth_with_email()
        main.input_email(email="kahap37224@nifect.com")
        main.input_password(password="7wNb5qSz2iBShH7wNb5qSz2iBShH")
        main.click_submit_enter()