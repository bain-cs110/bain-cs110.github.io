import helpers
helpers.modify_system_path()

import unittest
import time
from apis import audio
from unittest.mock import MagicMock
import json
class TestAudio(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        self.artist_id = '6vWDO969PvNqNYHIOW5v0m'
        self.track_id = '4JehYebiI9JE8sR8MisGVb'
        self.playlist_id = '6fnAkPYsgU8ZrNXAHqxheU'
        self.user_id = '21msewzqkeltozhd5ps24xuki'
        self.album_id = '2Gq0ERke26yxdGuRvrqFTD'
        self.artist_ids = [self.artist_id]
        self.track_ids = [self.track_id]
        self.genres = ['pop', 'rock', 'indie']
        self.track_urls = [
            'https://api.spotify.com/v1/search?q=beyonce&type=track',
            'https://api.spotify.com/v1/artists/' + self.artist_id + '/top-tracks?country=us',
            'https://api.spotify.com/v1/playlists/' + self.playlist_id + '/tracks',
        ]
        self.playlist_urls = [
            'https://api.spotify.com/v1/search?q=beyonce&type=playlist',
            'https://api.spotify.com/v1/users/' + self.user_id + '/playlists'
        ]
        self.artist_urls = [
            'https://api.spotify.com/v1/search?q=beyonce&type=artist',
            'https://api.spotify.com/v1/artists/' + self.artist_id + '/related-artists'
        ]
        self.album_urls = [
            'https://api.spotify.com/v1/search?q=beyonce&type=album',
            'https://api.spotify.com/v1/artists/' + self.artist_id + '/albums'

        ]
        self.urls = self.track_urls + self.playlist_urls + \
            self.artist_urls + self.album_urls

        super(TestAudio, self).__init__(*args, **kwargs)

    # Private Functions:
    def test__issue_get_request(self):
        print()
        for url in self.urls:
            data = audio._issue_get_request(url, debug=False)
            print('Loading:', url)
            self.assertEqual(type(data), dict)
            time.sleep(1)

    def test__issue_get_request_only_one(self):
        print()
        #url = self.urls[0]
        data = audio.search_for_artists("Rihanna")
        #print('Loading:', url)
        self.assertEqual(type(data), dict)

    def test__simplify_tracks(self):
        for url in self.track_urls:
            data = audio._issue_get_request(url, debug=False)
            if data.get('tracks'):
                data = audio._simplify_tracks(tracks = data['tracks'], debug=False)
            else:
                tracks = []
                for item in data['items']:
                    if item.get('track'):
                        tracks.append(item.get('track'))
                    else:
                        tracks.append(item)
                data = audio._simplify_tracks(tracks=tracks, debug=False)
            self.assertGreaterEqual(len(data), 3)

    def test__simplify_playlists(self):
        for url in self.playlist_urls:
            data = audio._issue_get_request(url, debug=False)
            if data.get('items'):
                data = audio._simplify_playlists(data['items'])
            else:
                data = audio._simplify_playlists(data['playlists']['items'])
            self.assertGreaterEqual(len(data), 3)

    def test__simplify_playlists_error_message(self):
        with self.assertRaises(Exception) as cm:
            audio._simplify_playlists({'a': 'b'})

        self.assertEqual(
            'The following playlist data structure could not be flattened:\n{\'a\': \'b\'}', str(cm.exception)
        )
        with self.assertRaises(Exception) as cm:
            audio._simplify_playlists(['a', 'b'])
        self.assertEqual(
            'The following playlist data structure could not be flattened:\n[\'a\', \'b\']', str(cm.exception)
        )

    def test_get_genres(self):
        genres = [
            "alternative", "ambient", "blues", 
            "chill", "country", "dance", "electronic", "folk", 
            "funk", "happy", "hip-hop", "indie-pop", "jazz", "k-pop", "metal", 
            "new-release", "pop", "punk", "reggae", "rock",
            "soul", "study", "trance", "work-out", "world-music"
        ]
        self.assertEqual(audio.get_genres(), genres)

    def test_search_for_tracks_simplified(self):
        url = 'https://api.spotify.com/v1/search?q=Beyonce&type=track'
        data = {'tracks': {'items': [{}] }}

        # spoof _issue_get_request and _simplify_tracks
        audio._issue_get_request = MagicMock(return_value=data)
        audio._simplify_tracks = MagicMock()

        # call function:
        audio.search_for_tracks(search_term="Beyonce", simplify=True, debug=False)

        # check that spoofed functions called with correct data:
        audio._issue_get_request.assert_called_with(url, debug=False)
        audio._simplify_tracks.assert_called_with(data["tracks"]["items"], debug=False)

    def test_search_for_tracks_not_simplified(self):
        url = 'https://api.spotify.com/v1/search?q=Beyonce&type=track'
        data = {'tracks': {'items': [{}] }}

        # spoof _issue_get_request and _simplify_tracks
        audio._issue_get_request = MagicMock(return_value=data)
        audio._simplify_tracks = MagicMock()

        # call function:
        audio.search_for_tracks(search_term="Beyonce", simplify=False, debug=False)

        # check that spoofed functions called with correct data:
        audio._issue_get_request.assert_called_with(url, debug=False)
        audio._simplify_tracks.assert_not_called()

    def test_search_for_tracks_default(self):
        url = 'https://api.spotify.com/v1/search?q=Depeche Mode&type=track'
        data = {'tracks': {'items': [{}] }}

        # spoof _issue_get_request and _simplify_tracks
        audio._issue_get_request = MagicMock(return_value=data)
        audio._simplify_tracks = MagicMock()

        # call function:
        audio.search_for_tracks(search_term="Depeche Mode", debug=False)

        # check that spoofed functions called with correct data:
        audio._issue_get_request.assert_called_with(url, debug=False)
        audio._simplify_tracks.assert_called_with(data["tracks"]["items"], debug=False)

    def test_get_top_tracks_by_artist(self):
        # call function:
        result = audio.get_top_tracks_by_artist(self.artist_id, debug=False)
        
        for track in result:
            self.assertIsInstance(track, dict)
            self.assertIn("name", track)
            self.assertIn("share_url", track)
            self.assertIn("id", track)

    def test_get_top_tracks_by_artist_not_simplified(self):
        # call function:
        result = audio.get_top_tracks_by_artist(self.artist_id, simplify=False, debug=False)

        self.assertIsInstance(result, dict)

    def test_generate_mixtape_validation(self):

        with self.assertRaises(Exception) as cm:
            audio.generate_mixtape(practice=False, debug=False)
        self.assertEqual(
            "Either artist_ids or track_ids or genres required", str(cm.exception)
        )

        with self.assertRaises(Exception) as cm:
            audio.generate_mixtape(artist_ids=["Beyonce"], practice=False, debug=False, simplify=True)
        with self.assertRaises(Exception) as cm:
            audio.generate_mixtape(
                track_ids=["No One Mourns the Wicked"], practice=False, debug=False, simplify=True
            )

    def test_generate_mixtape_simplify_default(self):

        audio._simplify_tracks = MagicMock()

        audio._get_top_tracks_by_artist = MagicMock()
        audio._get_several_tracks = MagicMock()
        audio._search_by_genres = MagicMock()

        # call function:
        result = audio.generate_mixtape(
            artist_ids=[self.artist_id],
            track_ids=[self.track_id],
            genres=self.genres,
            practice=False,
            debug=False,
            simplify=True
        )
        # check that spoofed functions called with correct data:
        audio._get_top_tracks_by_artist.assert_called_once_with(artist_id = self.artist_id, debug=False, simplify=True)
        audio._get_several_tracks.assert_called_once_with(
            [self.track_id], debug=False, simplify=True
        )
        audio._search_by_genres.assert_called_once_with(
            self.genres, debug=False, simplify=True
        )

        self.assertIsInstance(result, list)

        for track in result:
            self.assertIsInstance(track, dict)
            self.assertIn("name", track)
            self.assertIn("share_url", track)
            self.assertIn("id", track)


def test_generate_mixtape_practice(self):

    audio._simplify_tracks = MagicMock()

    audio._get_top_tracks_by_artist = MagicMock()
    audio._get_several_tracks = MagicMock()
    audio._search_by_genres = MagicMock()

    # call function:
    result = audio.generate_mixtape(
        practice=True,
        debug=False,
    )
    # check that spoofed functions called with correct data:
    audio._get_top_tracks_by_artist.assert_not_called()
    audio._get_several_tracks.assert_not_called()
    audio._search_by_genres.assert_not_called()

    self.assertIsEqual(result, audio._simplify_tracks(json.loads(audio.TRACKS_JSON)["tracks"]))


if __name__ == '__main__':
    unittest.main()
