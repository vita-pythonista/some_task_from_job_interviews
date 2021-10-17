import pytest
import time

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default='chrome',
                     help="Choose name browse: chrome, firefox or headless")

@pytest.fixture()
def browser(request):
    """Фикстура для вызова браузера"""
    browser_name = request.config.getoption("browser")
    if browser_name == 'chrome':
        chromer = ChromeDriverManager().install()
        driver = webdriver.Chrome(chromer)
        driver.maximize_window()
    elif browser_name == 'firefox':
        time.sleep(5)
        firefox = GeckoDriverManager().install()
        driver = webdriver.Firefox(executable_path=firefox)
        driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def remote_browser(request):
    browser_name = request.config.getoption('browser')
    if browser_name == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.headless = True
        chrome_options.add_argument("window-size=1920,1080")
        chrome_options.add_argument("--disable-gpu")
        driver = webdriver.Remote(options=chrome_options)
    elif browser_name == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.headless = True
        driver = webdriver.Remote(options=firefox_options)
    yield driver
    driver.quit()