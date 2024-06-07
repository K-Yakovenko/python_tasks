from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_button_selector = "//a[@aria-label='Search']"
        self.search_input_selector = "//input[@data-testid='search-input']"

    def click_search_button(self):
        self.page.click(self.search_button_selector)

    def enter_search_text(self, text):
        self.page.fill(self.search_input_selector, text)
