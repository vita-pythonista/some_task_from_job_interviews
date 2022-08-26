from pages.main_google import MainPageAction


def test_search_bork_mvideo(browser):
    browser.get("https://www.google.com")
    search = MainPageAction(browser)
    search.search_it("купить кофемашину bork c804")
    search.exist_mvideo()