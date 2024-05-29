import pytest
from spotify_client import SpotifyClient

@pytest.fixture(scope="module")
def spotify_client():
    return SpotifyClient()
