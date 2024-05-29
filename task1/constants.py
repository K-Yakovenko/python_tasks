TOKEN_URL = 'https://accounts.spotify.com/api/token'
SEARCH_URL = 'https://api.spotify.com/v1/search'
TOP_TRACKS_URL_TEMPLATE = 'https://api.spotify.com/v1/artists/{artist_id}/top-tracks'

TOKEN_HEADERS = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
TOKEN_DATA = {
    'grant_type': 'client_credentials'
}
MARKET = 'US'

ERROR_FETCHING_TOKEN = 'Error fetching access token'
ERROR_FETCHING_ARTIST = 'Error fetching artist data'
ERROR_FETCHING_TOP_TRACKS = 'Error fetching top tracks'
