from playwright.sync_api import Page

class SearchResultsPage:
    def __init__(self, page: Page):
        self.page = page

    def search_song(self, song_name: str):
        return self.page.locator(f"//div[contains(@class, 'encore-text') and contains(text(), '{song_name}')]")

    def check_song_exists(self, song_name: str) -> bool:
        song_element = self.search_song(song_name)
        return song_element.is_visible()
