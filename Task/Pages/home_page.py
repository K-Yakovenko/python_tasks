from selenium.webdriver.common.by import By
from browser.py_quality_services import PyQualityServices

class HomePage:
  def __init__(self):
    self.__search_button = PyQualityServices.element_factory.get_button((By.XPATH, "//a[@aria-label='Search']"), "Search button")
    self.__search_input = PyQualityServices.element_factory.get_text_box((By.XPATH, "//input[@data-testid='search-input']"), "Search input")

  def click_search_button(self):
    self.__search_button.click()

  def enter_search_text(self, text):
    self.__search_input.send_keys(text)
