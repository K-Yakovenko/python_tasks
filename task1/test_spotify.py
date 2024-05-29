import pytest

class TestSpotifyClient:
  def test_artists_have_specific_genres(self, spotify_client, test_data):
    artists_genres = test_data['artists_genres']

    for artist_name, expected_genres in artists_genres.items():
      artist = spotify_client.get_artist(artist_name)
      actual_genres = [genre.lower() for genre in artist.genres]
      for genre in expected_genres:
        assert genre.lower() in actual_genres, f"{artist_name} should have genre {genre}"

  def test_artists_have_popular_songs(self, spotify_client, test_data):
    artists_popular_songs = test_data['artists_popular_songs']

    for artist_name, expected_songs in artists_popular_songs.items():
      artist = spotify_client.get_artist(artist_name)
      top_tracks = spotify_client.get_artist_top_tracks(artist.id)
      top_track_names = [track.name.lower() for track in top_tracks]
      for song in expected_songs:
        assert song.lower() in top_track_names, f"{artist_name} should have song {song}"

if __name__ == "__main__":
  pytest.main()
