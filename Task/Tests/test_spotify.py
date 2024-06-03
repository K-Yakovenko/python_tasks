from Task.Pages.home_page import HomePage
from Task.Pages.search_results_page import SearchResultsPage
from Task.Utils.utils import Utils

def test_search_song():
  home_page = HomePage()
  search_results_page = SearchResultsPage()

  test_data = Utils.load_test_data()

  home_page.click_search_button()
  home_page.enter_search_text(test_data["artist_name"])
  assert search_results_page.check_song_exists(test_data["song_name"])
