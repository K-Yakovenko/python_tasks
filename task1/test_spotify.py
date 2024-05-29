import pytest

class TestSpotifyClient:
    @pytest.mark.parametrize("artist_name, expected_genres", [
        ("Drake", ["Rap"]),
        ("The Beatles", ["British Invasion"]),
    ])
    def test_artists_have_specific_genres(self, spotify_client, artist_name, expected_genres):
        artist = spotify_client.get_artist(artist_name)
        actual_genres = [genre.lower() for genre in artist.genres]
        for genre in expected_genres:
            assert genre.lower() in actual_genres, f"{artist_name} should have genre {genre}"

    @pytest.mark.parametrize("artist_name, expected_songs", [
        ("Drake", ["One Dance"]),
        ("The Beatles", ["Here Comes The Sun - Remastered 2009"]),
    ])
    def test_artists_have_popular_songs(self, spotify_client, artist_name, expected_songs):
        artist = spotify_client.get_artist(artist_name)
        top_tracks = spotify_client.get_artist_top_tracks(artist.id)
        top_track_names = [track.name.lower() for track in top_tracks]
        for song in expected_songs:
            assert song.lower() in top_track_names, f"{artist_name} should have song {song}"

if __name__ == "__main__":
    pytest.main()
