from selenium.webdriver.common.by import By
from browser.py_quality_services import PyQualityServices

class SearchResultsPage:
    @classmethod
    def search_song(cls, song_name):
        return PyQualityServices.element_factory.get_label((By.XPATH, f"//div[contains(@class, 'encore-text') and contains(text(), '{song_name}')]"), f"Song name: {song_name}")

    def check_song_exists(self, song_name):
        song_element = SearchResultsPage.search_song(song_name)
        return song_element.state.wait_for_displayed()
