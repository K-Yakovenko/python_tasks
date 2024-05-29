import requests
import base64
from typing import List
from models import Artist, Song
from config import client_id, client_secret
from constants import (
    TOKEN_URL, SEARCH_URL, TOP_TRACKS_URL_TEMPLATE,
    TOKEN_HEADERS, TOKEN_DATA, MARKET,
    ERROR_FETCHING_TOKEN, ERROR_FETCHING_ARTIST, ERROR_FETCHING_TOP_TRACKS
)

class SpotifyClient:
    def __init__(self):
        self.access_token = self._get_access_token()

    def _get_access_token(self) -> str:
        auth_str = f"{client_id}:{client_secret}"
        b64_auth_str = base64.b64encode(auth_str.encode()).decode()

        headers = {
            'Authorization': f'Basic {b64_auth_str}',
            **TOKEN_HEADERS
        }

        response = requests.post(TOKEN_URL, headers=headers, data=TOKEN_DATA)
        if response.status_code != 200:
            raise Exception(ERROR_FETCHING_TOKEN)
        response_data = response.json()
        return response_data['access_token']

    def get_artist(self, artist_name: str) -> Artist:
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        params = {
            'q': f'artist:{artist_name}',
            'type': 'artist',
            'limit': 1
        }

        response = requests.get(SEARCH_URL, headers=headers, params=params)
        if response.status_code != 200:
            raise Exception(ERROR_FETCHING_ARTIST)
        response_data = response.json()
        item = response_data['artists']['items'][0]

        return Artist(
            id=item['id'],
            name=item['name'],
            genres=item['genres'],
            popularity=item['popularity'],
            followers=item['followers']['total'],
            spotify_url=item['external_urls']['spotify']
        )

    def get_artist_top_tracks(self, artist_id: str) -> List[Song]:
        url = TOP_TRACKS_URL_TEMPLATE.format(artist_id=artist_id)
        headers = {
            'Authorization': f'Bearer {self.access_token}'
        }
        params = {
            'market': MARKET
        }

        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            raise Exception(ERROR_FETCHING_TOP_TRACKS)
        response_data = response.json()

        return [
            Song(
                id=track['id'],
                name=track['name'],
                popularity=track['popularity'],
                preview_url=track['preview_url']
            ) for track in response_data['tracks']
        ]
