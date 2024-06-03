import pytest
from ...Framework.browser_factory import BrowserFactory
from browser.py_quality_services import PyQualityServices

@pytest.fixture(scope="session", autouse=True)
def prepare_browser_factory():
  PyQualityServices.browser_factory = BrowserFactory()

@pytest.fixture(scope="session")
def browser():
  factory = BrowserFactory()
  driver = factory.get_driver()
  yield driver
  driver.quit()

@pytest.fixture(scope="function", autouse=True)
def setup_browser(browser):
  browser.get("https://www.spotify.com/")
