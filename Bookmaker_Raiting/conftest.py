import pytest
import logging

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FFWebDriver
from selenium.webdriver.support.events import EventFiringWebDriver
from helper.listener import DriverListener

logging.basicConfig(level=logging.INFO)

def pytest_addoption(parser):
    parser.addoption("--browser", action='store', default='firefox',
                     help="Choose name browse^ chrome, firefox or headless")

@pytest.fixture()
def browser(request):
    """Fixture for browser calling°"""
    browser_name = request.config.getoption("browser")
    if browser_name == 'chrome':
        logging.info("Starting browser Chrome")
        chromer = ChromeDriverManager().install()
        driver = EventFiringWebDriver(driver=WebDriver(chromer), event_listener=DriverListener())
        driver.maximize_window()
    elif browser_name == 'firefox':
        logging.info("Starting browser Firefox")
        firefox = GeckoDriverManager().install()
        driver = EventFiringWebDriver(driver=FFWebDriver(executable_path=firefox), event_listener=DriverListener())
        driver.maximize_window()
    else:
        logging.info("This browser is not supported")
    yield driver
    driver.quit()