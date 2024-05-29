import pytest
from spotify_client import SpotifyClient
from utils import Utils

@pytest.fixture(scope="module")
def spotify_client():
    return SpotifyClient()

@pytest.fixture(scope="module")
def test_data():
    return Utils.load_test_data()
