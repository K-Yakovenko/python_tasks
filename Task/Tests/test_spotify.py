from ..Pages.home_page import HomePage
from ..Pages.search_results_page import SearchResultsPage
from ..Utils.utils import Utils

def test_search_song(page):
    home_page = HomePage(page)
    search_results_page = SearchResultsPage(page)
    test_data = Utils.load_test_data()
    home_page.click_search_button()
    home_page.enter_search_text(test_data["artist_name"])
    assert search_results_page.check_song_exists(test_data["song_name"]), f"Song '{test_data['song_name']}' not found in search results."
