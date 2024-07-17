try:
    import utilities
    utilities.modify_system_path()
except:
    pass
import os
import requests
import base64
import time
import json
import random
import pickle

SPOTIFY_JSON = "spotify_token.json"
SPOTIFY_CACHE = "spotify_cache.pkl"
__docformat__ = "google"

__all__ = [
    'get_genres', 'get_tracks',
    'get_artists', 'get_playlists', 'get_audio_features_by_track',
    'get_related_artists', 'get_top_tracks_by_artist',
    'get_similar_tracks', 'get_playlists_by_user',
    'get_playlist_tracks',
    'generate_tracks_table',
    'generate_artists_table',
    'get_track_player_html',
    'get_playlist_player_html',
    'get_album_player_html',
]

TRACKS_JSON = """
{
    "tracks": [
        {
            "album": {
                "album_type": "ALBUM",
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/6UE7nl9mha6s8z0wFQFIZ2"
                        },
                        "href": "https://api.spotify.com/v1/artists/6UE7nl9mha6s8z0wFQFIZ2",
                        "id": "6UE7nl9mha6s8z0wFQFIZ2",
                        "name": "Robyn",
                        "type": "artist",
                        "uri": "spotify:artist:6UE7nl9mha6s8z0wFQFIZ2"
                    }
                ],
                "external_urls": {
                    "spotify": "https://open.spotify.com/album/0le9TO3kU69m6iWHTjNs9Y"
                },
                "href": "https://api.spotify.com/v1/albums/0le9TO3kU69m6iWHTjNs9Y",
                "id": "0le9TO3kU69m6iWHTjNs9Y",
                "images": [
                    {
                        "height": 640,
                        "url": "https://i.scdn.co/image/ab67616d0000b2734689597708c1b0b3dcb9ecaf",
                        "width": 640
                    },
                    {
                        "height": 300,
                        "url": "https://i.scdn.co/image/ab67616d00001e024689597708c1b0b3dcb9ecaf",
                        "width": 300
                    },
                    {
                        "height": 64,
                        "url": "https://i.scdn.co/image/ab67616d000048514689597708c1b0b3dcb9ecaf",
                        "width": 64
                    }
                ],
                "is_playable": true,
                "name": "Body Talk",
                "release_date": "2010-01-01",
                "release_date_precision": "day",
                "total_tracks": 15,
                "type": "album",
                "uri": "spotify:album:0le9TO3kU69m6iWHTjNs9Y"
            },
            "artists": [
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/6UE7nl9mha6s8z0wFQFIZ2"
                    },
                    "href": "https://api.spotify.com/v1/artists/6UE7nl9mha6s8z0wFQFIZ2",
                    "id": "6UE7nl9mha6s8z0wFQFIZ2",
                    "name": "Robyn",
                    "type": "artist",
                    "uri": "spotify:artist:6UE7nl9mha6s8z0wFQFIZ2"
                }
            ],
            "disc_number": 1,
            "duration_ms": 278080,
            "explicit": false,
            "external_ids": {
                "isrc": "SEWKZ1000009"
            },
            "external_urls": {
                "spotify": "https://open.spotify.com/track/7g13jf3zqlP5S68Voo5v9m"
            },
            "href": "https://api.spotify.com/v1/tracks/7g13jf3zqlP5S68Voo5v9m",
            "id": "7g13jf3zqlP5S68Voo5v9m",
            "is_local": false,
            "is_playable": true,
            "linked_from": {
                "external_urls": {
                    "spotify": "https://open.spotify.com/track/6aqNCrRA7vs7v6QvRpI50t"
                },
                "href": "https://api.spotify.com/v1/tracks/6aqNCrRA7vs7v6QvRpI50t",
                "id": "6aqNCrRA7vs7v6QvRpI50t",
                "type": "track",
                "uri": "spotify:track:6aqNCrRA7vs7v6QvRpI50t"
            },
            "name": "Dancing On My Own - Radio Edit",
            "popularity": 63,
            "preview_url": null,
            "track_number": 1,
            "type": "track",
            "uri": "spotify:track:7g13jf3zqlP5S68Voo5v9m"
        },
        {
            "album": {
                "album_type": "COMPILATION",
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/0LyfQWJT6nXafLPZqxe9Of"
                        },
                        "href": "https://api.spotify.com/v1/artists/0LyfQWJT6nXafLPZqxe9Of",
                        "id": "0LyfQWJT6nXafLPZqxe9Of",
                        "name": "Various Artists",
                        "type": "artist",
                        "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of"
                    },
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/2dfDjeZroUd3LWmSFrAZCD"
                        },
                        "href": "https://api.spotify.com/v1/artists/2dfDjeZroUd3LWmSFrAZCD",
                        "id": "2dfDjeZroUd3LWmSFrAZCD",
                        "name": "David Parry",
                        "type": "artist",
                        "uri": "spotify:artist:2dfDjeZroUd3LWmSFrAZCD"
                    },
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/3PfJE6ebCbCHeuqO4BfNeA"
                        },
                        "href": "https://api.spotify.com/v1/artists/3PfJE6ebCbCHeuqO4BfNeA",
                        "id": "3PfJE6ebCbCHeuqO4BfNeA",
                        "name": "London Philharmonic Orchestra",
                        "type": "artist",
                        "uri": "spotify:artist:3PfJE6ebCbCHeuqO4BfNeA"
                    }
                ],
                "external_urls": {
                    "spotify": "https://open.spotify.com/album/0bgjJ99UFbk0yBOzjJl7cq"
                },
                "href": "https://api.spotify.com/v1/albums/0bgjJ99UFbk0yBOzjJl7cq",
                "id": "0bgjJ99UFbk0yBOzjJl7cq",
                "images": [
                    {
                        "height": 640,
                        "url": "https://i.scdn.co/image/ab67616d0000b27376206bd8de3a477aafd7ba83",
                        "width": 640
                    },
                    {
                        "height": 300,
                        "url": "https://i.scdn.co/image/ab67616d00001e0276206bd8de3a477aafd7ba83",
                        "width": 300
                    },
                    {
                        "height": 64,
                        "url": "https://i.scdn.co/image/ab67616d0000485176206bd8de3a477aafd7ba83",
                        "width": 64
                    }
                ],
                "is_playable": true,
                "name": "The 50 Greatest Pieces of Classical Music",
                "release_date": "2009-11-23",
                "release_date_precision": "day",
                "total_tracks": 50,
                "type": "album",
                "uri": "spotify:album:0bgjJ99UFbk0yBOzjJl7cq"
            },
            "artists": [
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/430byzy0c5bPn5opiu0SRd"
                    },
                    "href": "https://api.spotify.com/v1/artists/430byzy0c5bPn5opiu0SRd",
                    "id": "430byzy0c5bPn5opiu0SRd",
                    "name": "Edward Elgar",
                    "type": "artist",
                    "uri": "spotify:artist:430byzy0c5bPn5opiu0SRd"
                },
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/2dfDjeZroUd3LWmSFrAZCD"
                    },
                    "href": "https://api.spotify.com/v1/artists/2dfDjeZroUd3LWmSFrAZCD",
                    "id": "2dfDjeZroUd3LWmSFrAZCD",
                    "name": "David Parry",
                    "type": "artist",
                    "uri": "spotify:artist:2dfDjeZroUd3LWmSFrAZCD"
                },
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/3PfJE6ebCbCHeuqO4BfNeA"
                    },
                    "href": "https://api.spotify.com/v1/artists/3PfJE6ebCbCHeuqO4BfNeA",
                    "id": "3PfJE6ebCbCHeuqO4BfNeA",
                    "name": "London Philharmonic Orchestra",
                    "type": "artist",
                    "uri": "spotify:artist:3PfJE6ebCbCHeuqO4BfNeA"
                }
            ],
            "disc_number": 1,
            "duration_ms": 345666,
            "explicit": false,
            "external_ids": {
                "isrc": "SEWDL9750023"
            },
            "external_urls": {
                "spotify": "https://open.spotify.com/track/5nsYZFNyMefd50yamWgMfy"
            },
            "href": "https://api.spotify.com/v1/tracks/5nsYZFNyMefd50yamWgMfy",
            "id": "5nsYZFNyMefd50yamWgMfy",
            "is_local": false,
            "is_playable": true,
            "name": "Pomp and Circumstance, Op. 39: No. 1, March in D Major",
            "popularity": 43,
            "preview_url": "https://p.scdn.co/mp3-preview/f617411fdc9c52d598ec9d5cde4baf24895598cb?cid=b800bf59070c4b52a8917d2230d25bdc",
            "track_number": 23,
            "type": "track",
            "uri": "spotify:track:5nsYZFNyMefd50yamWgMfy"
        },
        {
            "album": {
                "album_type": "ALBUM",
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/37mtx80nMDETlbsq2eFCzc"
                        },
                        "href": "https://api.spotify.com/v1/artists/37mtx80nMDETlbsq2eFCzc",
                        "id": "37mtx80nMDETlbsq2eFCzc",
                        "name": "Fleur East",
                        "type": "artist",
                        "uri": "spotify:artist:37mtx80nMDETlbsq2eFCzc"
                    }
                ],
                "external_urls": {
                    "spotify": "https://open.spotify.com/album/1nFgJpjh2doGfve56uADlm"
                },
                "href": "https://api.spotify.com/v1/albums/1nFgJpjh2doGfve56uADlm",
                "id": "1nFgJpjh2doGfve56uADlm",
                "images": [
                    {
                        "height": 640,
                        "url": "https://i.scdn.co/image/ab67616d0000b27340ab5a3c8e7e7c8f12cca2bb",
                        "width": 640
                    },
                    {
                        "height": 300,
                        "url": "https://i.scdn.co/image/ab67616d00001e0240ab5a3c8e7e7c8f12cca2bb",
                        "width": 300
                    },
                    {
                        "height": 64,
                        "url": "https://i.scdn.co/image/ab67616d0000485140ab5a3c8e7e7c8f12cca2bb",
                        "width": 64
                    }
                ],
                "is_playable": true,
                "name": "Love, Sax & Flashbacks (Track by Track)",
                "release_date": "2015-12-03",
                "release_date_precision": "day",
                "total_tracks": 32,
                "type": "album",
                "uri": "spotify:album:1nFgJpjh2doGfve56uADlm"
            },
            "artists": [
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/37mtx80nMDETlbsq2eFCzc"
                    },
                    "href": "https://api.spotify.com/v1/artists/37mtx80nMDETlbsq2eFCzc",
                    "id": "37mtx80nMDETlbsq2eFCzc",
                    "name": "Fleur East",
                    "type": "artist",
                    "uri": "spotify:artist:37mtx80nMDETlbsq2eFCzc"
                }
            ],
            "disc_number": 1,
            "duration_ms": 236440,
            "explicit": false,
            "external_ids": {
                "isrc": "GBHMU1500146"
            },
            "external_urls": {
                "spotify": "https://open.spotify.com/track/2lqgZDZnlXmVZgToWuoC0l"
            },
            "href": "https://api.spotify.com/v1/tracks/2lqgZDZnlXmVZgToWuoC0l",
            "id": "2lqgZDZnlXmVZgToWuoC0l",
            "is_local": false,
            "is_playable": true,
            "linked_from": {
                "external_urls": {
                    "spotify": "https://open.spotify.com/track/2IFl6p0LoIfIZOn5IaxZOO"
                },
                "href": "https://api.spotify.com/v1/tracks/2IFl6p0LoIfIZOn5IaxZOO",
                "id": "2IFl6p0LoIfIZOn5IaxZOO",
                "type": "track",
                "uri": "spotify:track:2IFl6p0LoIfIZOn5IaxZOO"
            },
            "name": "Sax",
            "popularity": 56,
            "preview_url": "https://p.scdn.co/mp3-preview/6d74e1c14810c12a9ccea0c523c740ab98a262fc?cid=b800bf59070c4b52a8917d2230d25bdc",
            "track_number": 1,
            "type": "track",
            "uri": "spotify:track:2lqgZDZnlXmVZgToWuoC0l"
        },
        {
            "album": {
                "album_type": "SINGLE",
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/1gALaWbNDnwS2ECV09sn2A"
                        },
                        "href": "https://api.spotify.com/v1/artists/1gALaWbNDnwS2ECV09sn2A",
                        "id": "1gALaWbNDnwS2ECV09sn2A",
                        "name": "Nightcrawlers",
                        "type": "artist",
                        "uri": "spotify:artist:1gALaWbNDnwS2ECV09sn2A"
                    }
                ],
                "external_urls": {
                    "spotify": "https://open.spotify.com/album/5JVyNX3e2hGoOttoe7B8QL"
                },
                "href": "https://api.spotify.com/v1/albums/5JVyNX3e2hGoOttoe7B8QL",
                "id": "5JVyNX3e2hGoOttoe7B8QL",
                "images": [
                    {
                        "height": 640,
                        "url": "https://i.scdn.co/image/ab67616d0000b2733b1e6a6f5aa7c01b433779fe",
                        "width": 640
                    },
                    {
                        "height": 300,
                        "url": "https://i.scdn.co/image/ab67616d00001e023b1e6a6f5aa7c01b433779fe",
                        "width": 300
                    },
                    {
                        "height": 64,
                        "url": "https://i.scdn.co/image/ab67616d000048513b1e6a6f5aa7c01b433779fe",
                        "width": 64
                    }
                ],
                "is_playable": true,
                "name": "Push The Feeling On",
                "release_date": "1995",
                "release_date_precision": "year",
                "total_tracks": 4,
                "type": "album",
                "uri": "spotify:album:5JVyNX3e2hGoOttoe7B8QL"
            },
            "artists": [
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/1gALaWbNDnwS2ECV09sn2A"
                    },
                    "href": "https://api.spotify.com/v1/artists/1gALaWbNDnwS2ECV09sn2A",
                    "id": "1gALaWbNDnwS2ECV09sn2A",
                    "name": "Nightcrawlers",
                    "type": "artist",
                    "uri": "spotify:artist:1gALaWbNDnwS2ECV09sn2A"
                },
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/1yqxFtPHKcGcv6SXZNdyT9"
                    },
                    "href": "https://api.spotify.com/v1/artists/1yqxFtPHKcGcv6SXZNdyT9",
                    "id": "1yqxFtPHKcGcv6SXZNdyT9",
                    "name": "MK",
                    "type": "artist",
                    "uri": "spotify:artist:1yqxFtPHKcGcv6SXZNdyT9"
                }
            ],
            "disc_number": 1,
            "duration_ms": 243160,
            "explicit": false,
            "external_ids": {
                "isrc": "GBANY9500081"
            },
            "external_urls": {
                "spotify": "https://open.spotify.com/track/1EWsVHU4FNAdtN4R8FETag"
            },
            "href": "https://api.spotify.com/v1/tracks/1EWsVHU4FNAdtN4R8FETag",
            "id": "1EWsVHU4FNAdtN4R8FETag",
            "is_local": false,
            "is_playable": true,
            "name": "Push The Feeling On - Mk Dub Revisited Edit",
            "popularity": 69,
            "preview_url": null,
            "track_number": 1,
            "type": "track",
            "uri": "spotify:track:1EWsVHU4FNAdtN4R8FETag"
        },
        {
            "album": {
                "album_type": "ALBUM",
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/7gAppWoH7pcYmphCVTXkzs"
                        },
                        "href": "https://api.spotify.com/v1/artists/7gAppWoH7pcYmphCVTXkzs",
                        "id": "7gAppWoH7pcYmphCVTXkzs",
                        "name": "The Vamps",
                        "type": "artist",
                        "uri": "spotify:artist:7gAppWoH7pcYmphCVTXkzs"
                    }
                ],
                "external_urls": {
                    "spotify": "https://open.spotify.com/album/69Pj3ce9XFZUi3XuQylLKf"
                },
                "href": "https://api.spotify.com/v1/albums/69Pj3ce9XFZUi3XuQylLKf",
                "id": "69Pj3ce9XFZUi3XuQylLKf",
                "images": [
                    {
                        "height": 640,
                        "url": "https://i.scdn.co/image/ab67616d0000b273f36a4e2e1687e678f29328cb",
                        "width": 640
                    },
                    {
                        "height": 300,
                        "url": "https://i.scdn.co/image/ab67616d00001e02f36a4e2e1687e678f29328cb",
                        "width": 300
                    },
                    {
                        "height": 64,
                        "url": "https://i.scdn.co/image/ab67616d00004851f36a4e2e1687e678f29328cb",
                        "width": 64
                    }
                ],
                "is_playable": true,
                "name": "Night & Day (Night Edition)",
                "release_date": "2017-07-14",
                "release_date_precision": "day",
                "total_tracks": 10,
                "type": "album",
                "uri": "spotify:album:69Pj3ce9XFZUi3XuQylLKf"
            },
            "artists": [
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/7gAppWoH7pcYmphCVTXkzs"
                    },
                    "href": "https://api.spotify.com/v1/artists/7gAppWoH7pcYmphCVTXkzs",
                    "id": "7gAppWoH7pcYmphCVTXkzs",
                    "name": "The Vamps",
                    "type": "artist",
                    "uri": "spotify:artist:7gAppWoH7pcYmphCVTXkzs"
                },
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/4YXycRbyyAE0wozTk7QMEq"
                    },
                    "href": "https://api.spotify.com/v1/artists/4YXycRbyyAE0wozTk7QMEq",
                    "id": "4YXycRbyyAE0wozTk7QMEq",
                    "name": "Matoma",
                    "type": "artist",
                    "uri": "spotify:artist:4YXycRbyyAE0wozTk7QMEq"
                }
            ],
            "disc_number": 1,
            "duration_ms": 197640,
            "explicit": false,
            "external_ids": {
                "isrc": "GBUM71605342"
            },
            "external_urls": {
                "spotify": "https://open.spotify.com/track/0dXNQ8dckG4eYfEtq9zcva"
            },
            "href": "https://api.spotify.com/v1/tracks/0dXNQ8dckG4eYfEtq9zcva",
            "id": "0dXNQ8dckG4eYfEtq9zcva",
            "is_local": false,
            "is_playable": true,
            "name": "All Night",
            "popularity": 72,
            "preview_url": null,
            "track_number": 2,
            "type": "track",
            "uri": "spotify:track:0dXNQ8dckG4eYfEtq9zcva"
        },
        {
            "album": {
                "album_type": "ALBUM",
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/6fxyWrfmjcbj5d12gXeiNV"
                        },
                        "href": "https://api.spotify.com/v1/artists/6fxyWrfmjcbj5d12gXeiNV",
                        "id": "6fxyWrfmjcbj5d12gXeiNV",
                        "name": "Denzel Curry",
                        "type": "artist",
                        "uri": "spotify:artist:6fxyWrfmjcbj5d12gXeiNV"
                    }
                ],
                "external_urls": {
                    "spotify": "https://open.spotify.com/album/42fyKPanos0Q3woi848ktg"
                },
                "href": "https://api.spotify.com/v1/albums/42fyKPanos0Q3woi848ktg",
                "id": "42fyKPanos0Q3woi848ktg",
                "images": [
                    {
                        "height": 640,
                        "url": "https://i.scdn.co/image/ab67616d0000b273166442984ba98f0a2dcaea5e",
                        "width": 640
                    },
                    {
                        "height": 300,
                        "url": "https://i.scdn.co/image/ab67616d00001e02166442984ba98f0a2dcaea5e",
                        "width": 300
                    },
                    {
                        "height": 64,
                        "url": "https://i.scdn.co/image/ab67616d00004851166442984ba98f0a2dcaea5e",
                        "width": 64
                    }
                ],
                "is_playable": true,
                "name": "Imperial",
                "release_date": "2016-10-14",
                "release_date_precision": "day",
                "total_tracks": 10,
                "type": "album",
                "uri": "spotify:album:42fyKPanos0Q3woi848ktg"
            },
            "artists": [
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/6fxyWrfmjcbj5d12gXeiNV"
                    },
                    "href": "https://api.spotify.com/v1/artists/6fxyWrfmjcbj5d12gXeiNV",
                    "id": "6fxyWrfmjcbj5d12gXeiNV",
                    "name": "Denzel Curry",
                    "type": "artist",
                    "uri": "spotify:artist:6fxyWrfmjcbj5d12gXeiNV"
                }
            ],
            "disc_number": 1,
            "duration_ms": 247054,
            "explicit": true,
            "external_ids": {
                "isrc": "USC4R1602006"
            },
            "external_urls": {
                "spotify": "https://open.spotify.com/track/5BSz8sJO2YmKfNVQG7fq2J"
            },
            "href": "https://api.spotify.com/v1/tracks/5BSz8sJO2YmKfNVQG7fq2J",
            "id": "5BSz8sJO2YmKfNVQG7fq2J",
            "is_local": false,
            "is_playable": true,
            "name": "ULT",
            "popularity": 52,
            "preview_url": null,
            "track_number": 1,
            "type": "track",
            "uri": "spotify:track:5BSz8sJO2YmKfNVQG7fq2J"
        },
        {
            "album": {
                "album_type": "ALBUM",
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/2ojlS7imGFiZ8A8tXXGEt7"
                        },
                        "href": "https://api.spotify.com/v1/artists/2ojlS7imGFiZ8A8tXXGEt7",
                        "id": "2ojlS7imGFiZ8A8tXXGEt7",
                        "name": "Library Tapes",
                        "type": "artist",
                        "uri": "spotify:artist:2ojlS7imGFiZ8A8tXXGEt7"
                    }
                ],
                "external_urls": {
                    "spotify": "https://open.spotify.com/album/43QOTxisI7tVOFZgUIWu4g"
                },
                "href": "https://api.spotify.com/v1/albums/43QOTxisI7tVOFZgUIWu4g",
                "id": "43QOTxisI7tVOFZgUIWu4g",
                "images": [
                    {
                        "height": 640,
                        "url": "https://i.scdn.co/image/ab67616d0000b2736813c2e10a4fb2a5cac8ebb0",
                        "width": 640
                    },
                    {
                        "height": 300,
                        "url": "https://i.scdn.co/image/ab67616d00001e026813c2e10a4fb2a5cac8ebb0",
                        "width": 300
                    },
                    {
                        "height": 64,
                        "url": "https://i.scdn.co/image/ab67616d000048516813c2e10a4fb2a5cac8ebb0",
                        "width": 64
                    }
                ],
                "is_playable": true,
                "name": "Fragment",
                "release_date": "2008-06-15",
                "release_date_precision": "day",
                "total_tracks": 8,
                "type": "album",
                "uri": "spotify:album:43QOTxisI7tVOFZgUIWu4g"
            },
            "artists": [
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/2ojlS7imGFiZ8A8tXXGEt7"
                    },
                    "href": "https://api.spotify.com/v1/artists/2ojlS7imGFiZ8A8tXXGEt7",
                    "id": "2ojlS7imGFiZ8A8tXXGEt7",
                    "name": "Library Tapes",
                    "type": "artist",
                    "uri": "spotify:artist:2ojlS7imGFiZ8A8tXXGEt7"
                }
            ],
            "disc_number": 1,
            "duration_ms": 240506,
            "explicit": false,
            "external_ids": {
                "isrc": "SEYTP0800202"
            },
            "external_urls": {
                "spotify": "https://open.spotify.com/track/7vv4tJIsMFm3XnDHikiwIc"
            },
            "href": "https://api.spotify.com/v1/tracks/7vv4tJIsMFm3XnDHikiwIc",
            "id": "7vv4tJIsMFm3XnDHikiwIc",
            "is_local": false,
            "is_playable": true,
            "linked_from": {
                "external_urls": {
                    "spotify": "https://open.spotify.com/track/7JQfc4yI4R8E4WOUYR7HD9"
                },
                "href": "https://api.spotify.com/v1/tracks/7JQfc4yI4R8E4WOUYR7HD9",
                "id": "7JQfc4yI4R8E4WOUYR7HD9",
                "type": "track",
                "uri": "spotify:track:7JQfc4yI4R8E4WOUYR7HD9"
            },
            "name": "Fragment II",
            "popularity": 44,
            "preview_url": null,
            "track_number": 2,
            "type": "track",
            "uri": "spotify:track:7vv4tJIsMFm3XnDHikiwIc"
        },
        {
            "album": {
                "album_type": "ALBUM",
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/163tK9Wjr9P9DmM0AVK7lm"
                        },
                        "href": "https://api.spotify.com/v1/artists/163tK9Wjr9P9DmM0AVK7lm",
                        "id": "163tK9Wjr9P9DmM0AVK7lm",
                        "name": "Lorde",
                        "type": "artist",
                        "uri": "spotify:artist:163tK9Wjr9P9DmM0AVK7lm"
                    }
                ],
                "external_urls": {
                    "spotify": "https://open.spotify.com/album/2nPokmAvYy5qYO4rFU7ZDm"
                },
                "href": "https://api.spotify.com/v1/albums/2nPokmAvYy5qYO4rFU7ZDm",
                "id": "2nPokmAvYy5qYO4rFU7ZDm",
                "images": [
                    {
                        "height": 640,
                        "url": "https://i.scdn.co/image/ab67616d0000b273e19c63f62581ab73a6589382",
                        "width": 640
                    },
                    {
                        "height": 300,
                        "url": "https://i.scdn.co/image/ab67616d00001e02e19c63f62581ab73a6589382",
                        "width": 300
                    },
                    {
                        "height": 64,
                        "url": "https://i.scdn.co/image/ab67616d00004851e19c63f62581ab73a6589382",
                        "width": 64
                    }
                ],
                "is_playable": true,
                "name": "Pure Heroine",
                "release_date": "2013-01-01",
                "release_date_precision": "day",
                "total_tracks": 13,
                "type": "album",
                "uri": "spotify:album:2nPokmAvYy5qYO4rFU7ZDm"
            },
            "artists": [
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/163tK9Wjr9P9DmM0AVK7lm"
                    },
                    "href": "https://api.spotify.com/v1/artists/163tK9Wjr9P9DmM0AVK7lm",
                    "id": "163tK9Wjr9P9DmM0AVK7lm",
                    "name": "Lorde",
                    "type": "artist",
                    "uri": "spotify:artist:163tK9Wjr9P9DmM0AVK7lm"
                }
            ],
            "disc_number": 1,
            "duration_ms": 258969,
            "explicit": false,
            "external_ids": {
                "isrc": "NZUM71300122"
            },
            "external_urls": {
                "spotify": "https://open.spotify.com/track/2MvvoeRt8NcOXWESkxWn3g"
            },
            "href": "https://api.spotify.com/v1/tracks/2MvvoeRt8NcOXWESkxWn3g",
            "id": "2MvvoeRt8NcOXWESkxWn3g",
            "is_local": false,
            "is_playable": true,
            "linked_from": {
                "external_urls": {
                    "spotify": "https://open.spotify.com/track/38WyDtxZhxm63jiythwemE"
                },
                "href": "https://api.spotify.com/v1/tracks/38WyDtxZhxm63jiythwemE",
                "id": "38WyDtxZhxm63jiythwemE",
                "type": "track",
                "uri": "spotify:track:38WyDtxZhxm63jiythwemE"
            },
            "name": "Ribs",
            "popularity": 80,
            "preview_url": null,
            "track_number": 4,
            "type": "track",
            "uri": "spotify:track:2MvvoeRt8NcOXWESkxWn3g"
        },
        {
            "album": {
                "album_type": "SINGLE",
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/0lZoBs4Pzo7R89JM9lxwoT"
                        },
                        "href": "https://api.spotify.com/v1/artists/0lZoBs4Pzo7R89JM9lxwoT",
                        "id": "0lZoBs4Pzo7R89JM9lxwoT",
                        "name": "Duran Duran",
                        "type": "artist",
                        "uri": "spotify:artist:0lZoBs4Pzo7R89JM9lxwoT"
                    }
                ],
                "external_urls": {
                    "spotify": "https://open.spotify.com/album/5NLAqcJTupUe8pUzf6Jaen"
                },
                "href": "https://api.spotify.com/v1/albums/5NLAqcJTupUe8pUzf6Jaen",
                "id": "5NLAqcJTupUe8pUzf6Jaen",
                "images": [
                    {
                        "height": 640,
                        "url": "https://i.scdn.co/image/ab67616d0000b273b35021533b9088e272ceeb90",
                        "width": 640
                    },
                    {
                        "height": 300,
                        "url": "https://i.scdn.co/image/ab67616d00001e02b35021533b9088e272ceeb90",
                        "width": 300
                    },
                    {
                        "height": 64,
                        "url": "https://i.scdn.co/image/ab67616d00004851b35021533b9088e272ceeb90",
                        "width": 64
                    }
                ],
                "is_playable": true,
                "name": "Last Night in the City (feat. Kiesza) [The Remixes]",
                "release_date": "2017-03-10",
                "release_date_precision": "day",
                "total_tracks": 4,
                "type": "album",
                "uri": "spotify:album:5NLAqcJTupUe8pUzf6Jaen"
            },
            "artists": [
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/0lZoBs4Pzo7R89JM9lxwoT"
                    },
                    "href": "https://api.spotify.com/v1/artists/0lZoBs4Pzo7R89JM9lxwoT",
                    "id": "0lZoBs4Pzo7R89JM9lxwoT",
                    "name": "Duran Duran",
                    "type": "artist",
                    "uri": "spotify:artist:0lZoBs4Pzo7R89JM9lxwoT"
                },
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/4zxvC7CRGvggq9EWXOpwAo"
                    },
                    "href": "https://api.spotify.com/v1/artists/4zxvC7CRGvggq9EWXOpwAo",
                    "id": "4zxvC7CRGvggq9EWXOpwAo",
                    "name": "Kiesza",
                    "type": "artist",
                    "uri": "spotify:artist:4zxvC7CRGvggq9EWXOpwAo"
                },
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/5c8rdJfIrtDTnRak9cuzwv"
                    },
                    "href": "https://api.spotify.com/v1/artists/5c8rdJfIrtDTnRak9cuzwv",
                    "id": "5c8rdJfIrtDTnRak9cuzwv",
                    "name": "Louis Vivet",
                    "type": "artist",
                    "uri": "spotify:artist:5c8rdJfIrtDTnRak9cuzwv"
                }
            ],
            "disc_number": 1,
            "duration_ms": 201999,
            "explicit": false,
            "external_ids": {
                "isrc": "USWB11700345"
            },
            "external_urls": {
                "spotify": "https://open.spotify.com/track/49Ux5DRv82fNGXDO7sIy4y"
            },
            "href": "https://api.spotify.com/v1/tracks/49Ux5DRv82fNGXDO7sIy4y",
            "id": "49Ux5DRv82fNGXDO7sIy4y",
            "is_local": false,
            "is_playable": true,
            "name": "Last Night in the City (feat. Kiesza) - Louis Vivet Remix",
            "popularity": 6,
            "preview_url": "https://p.scdn.co/mp3-preview/9aa4da8b4c1b17c48a1f8a6f24058ac4e47fdf7b?cid=b800bf59070c4b52a8917d2230d25bdc",
            "track_number": 3,
            "type": "track",
            "uri": "spotify:track:49Ux5DRv82fNGXDO7sIy4y"
        },
        {
            "album": {
                "album_type": "SINGLE",
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/65YhYi4Fz5Ibgq7ueev2Rm"
                        },
                        "href": "https://api.spotify.com/v1/artists/65YhYi4Fz5Ibgq7ueev2Rm",
                        "id": "65YhYi4Fz5Ibgq7ueev2Rm",
                        "name": "Frederick Delius",
                        "type": "artist",
                        "uri": "spotify:artist:65YhYi4Fz5Ibgq7ueev2Rm"
                    },
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/5Dl3HXZjG6ZOWT5cV375lk"
                        },
                        "href": "https://api.spotify.com/v1/artists/5Dl3HXZjG6ZOWT5cV375lk",
                        "id": "5Dl3HXZjG6ZOWT5cV375lk",
                        "name": "Yo-Yo Ma",
                        "type": "artist",
                        "uri": "spotify:artist:5Dl3HXZjG6ZOWT5cV375lk"
                    },
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/7JmDqds7Y1LRSWZVM8e0Og"
                        },
                        "href": "https://api.spotify.com/v1/artists/7JmDqds7Y1LRSWZVM8e0Og",
                        "id": "7JmDqds7Y1LRSWZVM8e0Og",
                        "name": "Kathryn Stott",
                        "type": "artist",
                        "uri": "spotify:artist:7JmDqds7Y1LRSWZVM8e0Og"
                    }
                ],
                "external_urls": {
                    "spotify": "https://open.spotify.com/album/5Srtg5Q52DBLYEAIEQBDyH"
                },
                "href": "https://api.spotify.com/v1/albums/5Srtg5Q52DBLYEAIEQBDyH",
                "id": "5Srtg5Q52DBLYEAIEQBDyH",
                "images": [
                    {
                        "height": 640,
                        "url": "https://i.scdn.co/image/ab67616d0000b27309516b49c785767fb6193732",
                        "width": 640
                    },
                    {
                        "height": 300,
                        "url": "https://i.scdn.co/image/ab67616d00001e0209516b49c785767fb6193732",
                        "width": 300
                    },
                    {
                        "height": 64,
                        "url": "https://i.scdn.co/image/ab67616d0000485109516b49c785767fb6193732",
                        "width": 64
                    }
                ],
                "is_playable": true,
                "name": "Romance for Cello and Piano",
                "release_date": "2015-07-24",
                "release_date_precision": "day",
                "total_tracks": 1,
                "type": "album",
                "uri": "spotify:album:5Srtg5Q52DBLYEAIEQBDyH"
            },
            "artists": [
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/65YhYi4Fz5Ibgq7ueev2Rm"
                    },
                    "href": "https://api.spotify.com/v1/artists/65YhYi4Fz5Ibgq7ueev2Rm",
                    "id": "65YhYi4Fz5Ibgq7ueev2Rm",
                    "name": "Frederick Delius",
                    "type": "artist",
                    "uri": "spotify:artist:65YhYi4Fz5Ibgq7ueev2Rm"
                },
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/7JmDqds7Y1LRSWZVM8e0Og"
                    },
                    "href": "https://api.spotify.com/v1/artists/7JmDqds7Y1LRSWZVM8e0Og",
                    "id": "7JmDqds7Y1LRSWZVM8e0Og",
                    "name": "Kathryn Stott",
                    "type": "artist",
                    "uri": "spotify:artist:7JmDqds7Y1LRSWZVM8e0Og"
                },
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/5Dl3HXZjG6ZOWT5cV375lk"
                    },
                    "href": "https://api.spotify.com/v1/artists/5Dl3HXZjG6ZOWT5cV375lk",
                    "id": "5Dl3HXZjG6ZOWT5cV375lk",
                    "name": "Yo-Yo Ma",
                    "type": "artist",
                    "uri": "spotify:artist:5Dl3HXZjG6ZOWT5cV375lk"
                }
            ],
            "disc_number": 1,
            "duration_ms": 385186,
            "explicit": false,
            "external_ids": {
                "isrc": "USQX91500821"
            },
            "external_urls": {
                "spotify": "https://open.spotify.com/track/6ufaxWhOW87EXsKh5TSxMp"
            },
            "href": "https://api.spotify.com/v1/tracks/6ufaxWhOW87EXsKh5TSxMp",
            "id": "6ufaxWhOW87EXsKh5TSxMp",
            "is_local": false,
            "is_playable": true,
            "linked_from": {
                "external_urls": {
                    "spotify": "https://open.spotify.com/track/70nMUxP46mAcjW5iRpRiyN"
                },
                "href": "https://api.spotify.com/v1/tracks/70nMUxP46mAcjW5iRpRiyN",
                "id": "70nMUxP46mAcjW5iRpRiyN",
                "type": "track",
                "uri": "spotify:track:70nMUxP46mAcjW5iRpRiyN"
            },
            "name": "Romance for Cello and Piano",
            "popularity": 33,
            "preview_url": "https://p.scdn.co/mp3-preview/59053165aa006169f88b0888a1c2d8e420d5508a?cid=b800bf59070c4b52a8917d2230d25bdc",
            "track_number": 11,
            "type": "track",
            "uri": "spotify:track:6ufaxWhOW87EXsKh5TSxMp"
        },
        {
            "album": {
                "album_type": "SINGLE",
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/137W8MRPWKqSmrBGDBFSop"
                        },
                        "href": "https://api.spotify.com/v1/artists/137W8MRPWKqSmrBGDBFSop",
                        "id": "137W8MRPWKqSmrBGDBFSop",
                        "name": "Wiz Khalifa",
                        "type": "artist",
                        "uri": "spotify:artist:137W8MRPWKqSmrBGDBFSop"
                    }
                ],
                "external_urls": {
                    "spotify": "https://open.spotify.com/album/3qv4Hjk70y70MNe9Kb9X8f"
                },
                "href": "https://api.spotify.com/v1/albums/3qv4Hjk70y70MNe9Kb9X8f",
                "id": "3qv4Hjk70y70MNe9Kb9X8f",
                "images": [
                    {
                        "height": 640,
                        "url": "https://i.scdn.co/image/ab67616d0000b273dfe0748e91928eaf21373018",
                        "width": 640
                    },
                    {
                        "height": 300,
                        "url": "https://i.scdn.co/image/ab67616d00001e02dfe0748e91928eaf21373018",
                        "width": 300
                    },
                    {
                        "height": 64,
                        "url": "https://i.scdn.co/image/ab67616d00004851dfe0748e91928eaf21373018",
                        "width": 64
                    }
                ],
                "is_playable": true,
                "name": "Pull Up (feat. Lil Uzi Vert)",
                "release_date": "2016-05-25",
                "release_date_precision": "day",
                "total_tracks": 1,
                "type": "album",
                "uri": "spotify:album:3qv4Hjk70y70MNe9Kb9X8f"
            },
            "artists": [
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/137W8MRPWKqSmrBGDBFSop"
                    },
                    "href": "https://api.spotify.com/v1/artists/137W8MRPWKqSmrBGDBFSop",
                    "id": "137W8MRPWKqSmrBGDBFSop",
                    "name": "Wiz Khalifa",
                    "type": "artist",
                    "uri": "spotify:artist:137W8MRPWKqSmrBGDBFSop"
                },
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/4O15NlyKLIASxsJ0PrXPfz"
                    },
                    "href": "https://api.spotify.com/v1/artists/4O15NlyKLIASxsJ0PrXPfz",
                    "id": "4O15NlyKLIASxsJ0PrXPfz",
                    "name": "Lil Uzi Vert",
                    "type": "artist",
                    "uri": "spotify:artist:4O15NlyKLIASxsJ0PrXPfz"
                }
            ],
            "disc_number": 1,
            "duration_ms": 207391,
            "explicit": true,
            "external_ids": {
                "isrc": "USAT21601765"
            },
            "external_urls": {
                "spotify": "https://open.spotify.com/track/6LTsvaebP6V9tJFvZxqi5M"
            },
            "href": "https://api.spotify.com/v1/tracks/6LTsvaebP6V9tJFvZxqi5M",
            "id": "6LTsvaebP6V9tJFvZxqi5M",
            "is_local": false,
            "is_playable": true,
            "name": "Pull Up (feat. Lil Uzi Vert)",
            "popularity": 50,
            "preview_url": "https://p.scdn.co/mp3-preview/644de9f6fa47954ea3b44748b345a8f5f8d3fdd7?cid=b800bf59070c4b52a8917d2230d25bdc",
            "track_number": 1,
            "type": "track",
            "uri": "spotify:track:6LTsvaebP6V9tJFvZxqi5M"
        },
        {
            "album": {
                "album_type": "ALBUM",
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/2KsP6tYLJlTBvSUxnwlVWa"
                        },
                        "href": "https://api.spotify.com/v1/artists/2KsP6tYLJlTBvSUxnwlVWa",
                        "id": "2KsP6tYLJlTBvSUxnwlVWa",
                        "name": "Mike Posner",
                        "type": "artist",
                        "uri": "spotify:artist:2KsP6tYLJlTBvSUxnwlVWa"
                    }
                ],
                "external_urls": {
                    "spotify": "https://open.spotify.com/album/6Phl1V5P0sPrWJytXHGFeO"
                },
                "href": "https://api.spotify.com/v1/albums/6Phl1V5P0sPrWJytXHGFeO",
                "id": "6Phl1V5P0sPrWJytXHGFeO",
                "images": [
                    {
                        "height": 640,
                        "url": "https://i.scdn.co/image/ab67616d0000b2731db27fa11dbafa67857da8f3",
                        "width": 640
                    },
                    {
                        "height": 300,
                        "url": "https://i.scdn.co/image/ab67616d00001e021db27fa11dbafa67857da8f3",
                        "width": 300
                    },
                    {
                        "height": 64,
                        "url": "https://i.scdn.co/image/ab67616d000048511db27fa11dbafa67857da8f3",
                        "width": 64
                    }
                ],
                "is_playable": true,
                "name": "At Night, Alone.",
                "release_date": "2016-05-06",
                "release_date_precision": "day",
                "total_tracks": 18,
                "type": "album",
                "uri": "spotify:album:6Phl1V5P0sPrWJytXHGFeO"
            },
            "artists": [
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/2KsP6tYLJlTBvSUxnwlVWa"
                    },
                    "href": "https://api.spotify.com/v1/artists/2KsP6tYLJlTBvSUxnwlVWa",
                    "id": "2KsP6tYLJlTBvSUxnwlVWa",
                    "name": "Mike Posner",
                    "type": "artist",
                    "uri": "spotify:artist:2KsP6tYLJlTBvSUxnwlVWa"
                },
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/5iNrZmtVMtYev5M9yoWpEq"
                    },
                    "href": "https://api.spotify.com/v1/artists/5iNrZmtVMtYev5M9yoWpEq",
                    "id": "5iNrZmtVMtYev5M9yoWpEq",
                    "name": "Seeb",
                    "type": "artist",
                    "uri": "spotify:artist:5iNrZmtVMtYev5M9yoWpEq"
                }
            ],
            "disc_number": 1,
            "duration_ms": 197933,
            "explicit": true,
            "external_ids": {
                "isrc": "USUM71509342"
            },
            "external_urls": {
                "spotify": "https://open.spotify.com/track/0vbtURX4qv1l7besfwmnD8"
            },
            "href": "https://api.spotify.com/v1/tracks/0vbtURX4qv1l7besfwmnD8",
            "id": "0vbtURX4qv1l7besfwmnD8",
            "is_local": false,
            "is_playable": true,
            "name": "I Took A Pill In Ibiza - Seeb Remix",
            "popularity": 83,
            "preview_url": null,
            "track_number": 13,
            "type": "track",
            "uri": "spotify:track:0vbtURX4qv1l7besfwmnD8"
        },
        {
            "album": {
                "album_type": "COMPILATION",
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/0LyfQWJT6nXafLPZqxe9Of"
                        },
                        "href": "https://api.spotify.com/v1/artists/0LyfQWJT6nXafLPZqxe9Of",
                        "id": "0LyfQWJT6nXafLPZqxe9Of",
                        "name": "Various Artists",
                        "type": "artist",
                        "uri": "spotify:artist:0LyfQWJT6nXafLPZqxe9Of"
                    }
                ],
                "external_urls": {
                    "spotify": "https://open.spotify.com/album/6lJrqUXdCpEINx1fi5EqMa"
                },
                "href": "https://api.spotify.com/v1/albums/6lJrqUXdCpEINx1fi5EqMa",
                "id": "6lJrqUXdCpEINx1fi5EqMa",
                "images": [
                    {
                        "height": 640,
                        "url": "https://i.scdn.co/image/ab67616d0000b27333d6ad1275ae8ebe156686f5",
                        "width": 640
                    },
                    {
                        "height": 300,
                        "url": "https://i.scdn.co/image/ab67616d00001e0233d6ad1275ae8ebe156686f5",
                        "width": 300
                    },
                    {
                        "height": 64,
                        "url": "https://i.scdn.co/image/ab67616d0000485133d6ad1275ae8ebe156686f5",
                        "width": 64
                    }
                ],
                "is_playable": true,
                "name": "The Twilight Saga: Breaking Dawn - Part 2 (Original Motion Picture Soundtrack)",
                "release_date": "2012-11-09",
                "release_date_precision": "day",
                "total_tracks": 14,
                "type": "album",
                "uri": "spotify:album:6lJrqUXdCpEINx1fi5EqMa"
            },
            "artists": [
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/0SbSDzM4X41hnlURed0fcV"
                    },
                    "href": "https://api.spotify.com/v1/artists/0SbSDzM4X41hnlURed0fcV",
                    "id": "0SbSDzM4X41hnlURed0fcV",
                    "name": "Carter Burwell",
                    "type": "artist",
                    "uri": "spotify:artist:0SbSDzM4X41hnlURed0fcV"
                }
            ],
            "disc_number": 1,
            "duration_ms": 255773,
            "explicit": false,
            "external_ids": {
                "isrc": "USAT21206056"
            },
            "external_urls": {
                "spotify": "https://open.spotify.com/track/1brH9m4Q2LHTuwxaKoMTn5"
            },
            "href": "https://api.spotify.com/v1/tracks/1brH9m4Q2LHTuwxaKoMTn5",
            "id": "1brH9m4Q2LHTuwxaKoMTn5",
            "is_local": false,
            "is_playable": true,
            "name": "Plus Que Ma Prope Vie",
            "popularity": 48,
            "preview_url": "https://p.scdn.co/mp3-preview/585cd6ea1265df63d349dcda19035a27893f50d2?cid=b800bf59070c4b52a8917d2230d25bdc",
            "track_number": 14,
            "type": "track",
            "uri": "spotify:track:1brH9m4Q2LHTuwxaKoMTn5"
        },
        {
            "album": {
                "album_type": "ALBUM",
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/03r4iKL2g2442PT9n2UKsx"
                        },
                        "href": "https://api.spotify.com/v1/artists/03r4iKL2g2442PT9n2UKsx",
                        "id": "03r4iKL2g2442PT9n2UKsx",
                        "name": "Beastie Boys",
                        "type": "artist",
                        "uri": "spotify:artist:03r4iKL2g2442PT9n2UKsx"
                    }
                ],
                "external_urls": {
                    "spotify": "https://open.spotify.com/album/11oR0ZuqB3ucZwb5TGbZxb"
                },
                "href": "https://api.spotify.com/v1/albums/11oR0ZuqB3ucZwb5TGbZxb",
                "id": "11oR0ZuqB3ucZwb5TGbZxb",
                "images": [
                    {
                        "height": 640,
                        "url": "https://i.scdn.co/image/ab67616d0000b273a7ea08ab3914c5fb2084a8ac",
                        "width": 640
                    },
                    {
                        "height": 300,
                        "url": "https://i.scdn.co/image/ab67616d00001e02a7ea08ab3914c5fb2084a8ac",
                        "width": 300
                    },
                    {
                        "height": 64,
                        "url": "https://i.scdn.co/image/ab67616d00004851a7ea08ab3914c5fb2084a8ac",
                        "width": 64
                    }
                ],
                "is_playable": true,
                "name": "Licensed To Ill",
                "release_date": "1986-11-15",
                "release_date_precision": "day",
                "total_tracks": 13,
                "type": "album",
                "uri": "spotify:album:11oR0ZuqB3ucZwb5TGbZxb"
            },
            "artists": [
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/03r4iKL2g2442PT9n2UKsx"
                    },
                    "href": "https://api.spotify.com/v1/artists/03r4iKL2g2442PT9n2UKsx",
                    "id": "03r4iKL2g2442PT9n2UKsx",
                    "name": "Beastie Boys",
                    "type": "artist",
                    "uri": "spotify:artist:03r4iKL2g2442PT9n2UKsx"
                }
            ],
            "disc_number": 1,
            "duration_ms": 157440,
            "explicit": false,
            "external_ids": {
                "isrc": "USDJ28600011"
            },
            "external_urls": {
                "spotify": "https://open.spotify.com/track/2tY1gxCKslfXLFpFofYmJQ"
            },
            "href": "https://api.spotify.com/v1/tracks/2tY1gxCKslfXLFpFofYmJQ",
            "id": "2tY1gxCKslfXLFpFofYmJQ",
            "is_local": false,
            "is_playable": true,
            "name": "Brass Monkey",
            "popularity": 68,
            "preview_url": null,
            "track_number": 11,
            "type": "track",
            "uri": "spotify:track:2tY1gxCKslfXLFpFofYmJQ"
        },
        {
            "album": {
                "album_type": "ALBUM",
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/5Q81rlcTFh3k6DQJXPdsot"
                        },
                        "href": "https://api.spotify.com/v1/artists/5Q81rlcTFh3k6DQJXPdsot",
                        "id": "5Q81rlcTFh3k6DQJXPdsot",
                        "name": "Mura Masa",
                        "type": "artist",
                        "uri": "spotify:artist:5Q81rlcTFh3k6DQJXPdsot"
                    }
                ],
                "external_urls": {
                    "spotify": "https://open.spotify.com/album/0NBTBo1qrg554sAj79nEqD"
                },
                "href": "https://api.spotify.com/v1/albums/0NBTBo1qrg554sAj79nEqD",
                "id": "0NBTBo1qrg554sAj79nEqD",
                "images": [
                    {
                        "height": 640,
                        "url": "https://i.scdn.co/image/ab67616d0000b2736818aa231aa543cf87e1374a",
                        "width": 640
                    },
                    {
                        "height": 300,
                        "url": "https://i.scdn.co/image/ab67616d00001e026818aa231aa543cf87e1374a",
                        "width": 300
                    },
                    {
                        "height": 64,
                        "url": "https://i.scdn.co/image/ab67616d000048516818aa231aa543cf87e1374a",
                        "width": 64
                    }
                ],
                "is_playable": true,
                "name": "Mura Masa",
                "release_date": "2017-07-14",
                "release_date_precision": "day",
                "total_tracks": 13,
                "type": "album",
                "uri": "spotify:album:0NBTBo1qrg554sAj79nEqD"
            },
            "artists": [
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/5Q81rlcTFh3k6DQJXPdsot"
                    },
                    "href": "https://api.spotify.com/v1/artists/5Q81rlcTFh3k6DQJXPdsot",
                    "id": "5Q81rlcTFh3k6DQJXPdsot",
                    "name": "Mura Masa",
                    "type": "artist",
                    "uri": "spotify:artist:5Q81rlcTFh3k6DQJXPdsot"
                },
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/7pFeBzX627ff0VnN6bxPR4"
                    },
                    "href": "https://api.spotify.com/v1/artists/7pFeBzX627ff0VnN6bxPR4",
                    "id": "7pFeBzX627ff0VnN6bxPR4",
                    "name": "Desiigner",
                    "type": "artist",
                    "uri": "spotify:artist:7pFeBzX627ff0VnN6bxPR4"
                }
            ],
            "disc_number": 1,
            "duration_ms": 164013,
            "explicit": true,
            "external_ids": {
                "isrc": "GBUM71701364"
            },
            "external_urls": {
                "spotify": "https://open.spotify.com/track/4x8874idDYp8yxgKsyb4xG"
            },
            "href": "https://api.spotify.com/v1/tracks/4x8874idDYp8yxgKsyb4xG",
            "id": "4x8874idDYp8yxgKsyb4xG",
            "is_local": false,
            "is_playable": true,
            "name": "All Around The World (feat. Desiigner)",
            "popularity": 42,
            "preview_url": null,
            "track_number": 5,
            "type": "track",
            "uri": "spotify:track:4x8874idDYp8yxgKsyb4xG"
        },
        {
            "album": {
                "album_type": "SINGLE",
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/61lyPtntblHJvA7FMMhi7E"
                        },
                        "href": "https://api.spotify.com/v1/artists/61lyPtntblHJvA7FMMhi7E",
                        "id": "61lyPtntblHJvA7FMMhi7E",
                        "name": "Duke Dumont",
                        "type": "artist",
                        "uri": "spotify:artist:61lyPtntblHJvA7FMMhi7E"
                    }
                ],
                "external_urls": {
                    "spotify": "https://open.spotify.com/album/4SQqe6ACemVTNNOcq7Ql4A"
                },
                "href": "https://api.spotify.com/v1/albums/4SQqe6ACemVTNNOcq7Ql4A",
                "id": "4SQqe6ACemVTNNOcq7Ql4A",
                "images": [
                    {
                        "height": 640,
                        "url": "https://i.scdn.co/image/ab67616d0000b273be165dd0973a0db9607b3938",
                        "width": 640
                    },
                    {
                        "height": 300,
                        "url": "https://i.scdn.co/image/ab67616d00001e02be165dd0973a0db9607b3938",
                        "width": 300
                    },
                    {
                        "height": 64,
                        "url": "https://i.scdn.co/image/ab67616d00004851be165dd0973a0db9607b3938",
                        "width": 64
                    }
                ],
                "is_playable": true,
                "name": "The Giver (Reprise)",
                "release_date": "2015-03-17",
                "release_date_precision": "day",
                "total_tracks": 1,
                "type": "album",
                "uri": "spotify:album:4SQqe6ACemVTNNOcq7Ql4A"
            },
            "artists": [
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/61lyPtntblHJvA7FMMhi7E"
                    },
                    "href": "https://api.spotify.com/v1/artists/61lyPtntblHJvA7FMMhi7E",
                    "id": "61lyPtntblHJvA7FMMhi7E",
                    "name": "Duke Dumont",
                    "type": "artist",
                    "uri": "spotify:artist:61lyPtntblHJvA7FMMhi7E"
                }
            ],
            "disc_number": 1,
            "duration_ms": 195756,
            "explicit": false,
            "external_ids": {
                "isrc": "GBUM71501517"
            },
            "external_urls": {
                "spotify": "https://open.spotify.com/track/0ccSl4LZ7dksMNmJgkN7NO"
            },
            "href": "https://api.spotify.com/v1/tracks/0ccSl4LZ7dksMNmJgkN7NO",
            "id": "0ccSl4LZ7dksMNmJgkN7NO",
            "is_local": false,
            "is_playable": true,
            "name": "The Giver (Reprise)",
            "popularity": 43,
            "preview_url": null,
            "track_number": 1,
            "type": "track",
            "uri": "spotify:track:0ccSl4LZ7dksMNmJgkN7NO"
        },
        {
            "album": {
                "album_type": "ALBUM",
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/4NHQUGzhtTLFvgF5SZesLK"
                        },
                        "href": "https://api.spotify.com/v1/artists/4NHQUGzhtTLFvgF5SZesLK",
                        "id": "4NHQUGzhtTLFvgF5SZesLK",
                        "name": "Tove Lo",
                        "type": "artist",
                        "uri": "spotify:artist:4NHQUGzhtTLFvgF5SZesLK"
                    }
                ],
                "external_urls": {
                    "spotify": "https://open.spotify.com/album/1tuekzsMZQOuiMejKP6t2Y"
                },
                "href": "https://api.spotify.com/v1/albums/1tuekzsMZQOuiMejKP6t2Y",
                "id": "1tuekzsMZQOuiMejKP6t2Y",
                "images": [
                    {
                        "height": 640,
                        "url": "https://i.scdn.co/image/ab67616d0000b2739f0c014998bac13d3181474c",
                        "width": 640
                    },
                    {
                        "height": 300,
                        "url": "https://i.scdn.co/image/ab67616d00001e029f0c014998bac13d3181474c",
                        "width": 300
                    },
                    {
                        "height": 64,
                        "url": "https://i.scdn.co/image/ab67616d000048519f0c014998bac13d3181474c",
                        "width": 64
                    }
                ],
                "is_playable": true,
                "name": "Lady Wood",
                "release_date": "2016-10-28",
                "release_date_precision": "day",
                "total_tracks": 12,
                "type": "album",
                "uri": "spotify:album:1tuekzsMZQOuiMejKP6t2Y"
            },
            "artists": [
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/4NHQUGzhtTLFvgF5SZesLK"
                    },
                    "href": "https://api.spotify.com/v1/artists/4NHQUGzhtTLFvgF5SZesLK",
                    "id": "4NHQUGzhtTLFvgF5SZesLK",
                    "name": "Tove Lo",
                    "type": "artist",
                    "uri": "spotify:artist:4NHQUGzhtTLFvgF5SZesLK"
                }
            ],
            "disc_number": 1,
            "duration_ms": 234474,
            "explicit": true,
            "external_ids": {
                "isrc": "SEUM71601201"
            },
            "external_urls": {
                "spotify": "https://open.spotify.com/track/073A1FsNWqMxmdcRMeU57t"
            },
            "href": "https://api.spotify.com/v1/tracks/073A1FsNWqMxmdcRMeU57t",
            "id": "073A1FsNWqMxmdcRMeU57t",
            "is_local": false,
            "is_playable": true,
            "name": "Don’t Talk About It",
            "popularity": 39,
            "preview_url": null,
            "track_number": 8,
            "type": "track",
            "uri": "spotify:track:073A1FsNWqMxmdcRMeU57t"
        },
        {
            "album": {
                "album_type": "SINGLE",
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/6y02TEMv71ArWB2qhIaQ5m"
                        },
                        "href": "https://api.spotify.com/v1/artists/6y02TEMv71ArWB2qhIaQ5m",
                        "id": "6y02TEMv71ArWB2qhIaQ5m",
                        "name": "Kaiydo",
                        "type": "artist",
                        "uri": "spotify:artist:6y02TEMv71ArWB2qhIaQ5m"
                    }
                ],
                "external_urls": {
                    "spotify": "https://open.spotify.com/album/0oeJCHQwiz5dQhMuiFlhhM"
                },
                "href": "https://api.spotify.com/v1/albums/0oeJCHQwiz5dQhMuiFlhhM",
                "id": "0oeJCHQwiz5dQhMuiFlhhM",
                "images": [
                    {
                        "height": 640,
                        "url": "https://i.scdn.co/image/ab67616d0000b2731927f0378a81361fb80e20d6",
                        "width": 640
                    },
                    {
                        "height": 300,
                        "url": "https://i.scdn.co/image/ab67616d00001e021927f0378a81361fb80e20d6",
                        "width": 300
                    },
                    {
                        "height": 64,
                        "url": "https://i.scdn.co/image/ab67616d000048511927f0378a81361fb80e20d6",
                        "width": 64
                    }
                ],
                "is_playable": true,
                "name": "Fruit Punch",
                "release_date": "2016-08-12",
                "release_date_precision": "day",
                "total_tracks": 1,
                "type": "album",
                "uri": "spotify:album:0oeJCHQwiz5dQhMuiFlhhM"
            },
            "artists": [
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/6y02TEMv71ArWB2qhIaQ5m"
                    },
                    "href": "https://api.spotify.com/v1/artists/6y02TEMv71ArWB2qhIaQ5m",
                    "id": "6y02TEMv71ArWB2qhIaQ5m",
                    "name": "Kaiydo",
                    "type": "artist",
                    "uri": "spotify:artist:6y02TEMv71ArWB2qhIaQ5m"
                }
            ],
            "disc_number": 1,
            "duration_ms": 221622,
            "explicit": true,
            "external_ids": {
                "isrc": "TCACR1606159"
            },
            "external_urls": {
                "spotify": "https://open.spotify.com/track/0lpRp9KzzMbC0w1uiL7H7f"
            },
            "href": "https://api.spotify.com/v1/tracks/0lpRp9KzzMbC0w1uiL7H7f",
            "id": "0lpRp9KzzMbC0w1uiL7H7f",
            "is_local": false,
            "is_playable": true,
            "name": "Fruit Punch",
            "popularity": 48,
            "preview_url": "https://p.scdn.co/mp3-preview/62b43baeb1993236dfc7e78557996514f64a3d9f?cid=b800bf59070c4b52a8917d2230d25bdc",
            "track_number": 1,
            "type": "track",
            "uri": "spotify:track:0lpRp9KzzMbC0w1uiL7H7f"
        },
        {
            "album": {
                "album_type": "SINGLE",
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/21dooacK2WGBB5amYvKyfM"
                        },
                        "href": "https://api.spotify.com/v1/artists/21dooacK2WGBB5amYvKyfM",
                        "id": "21dooacK2WGBB5amYvKyfM",
                        "name": "Smokepurpp",
                        "type": "artist",
                        "uri": "spotify:artist:21dooacK2WGBB5amYvKyfM"
                    }
                ],
                "external_urls": {
                    "spotify": "https://open.spotify.com/album/2TeGNWZYaj9yeM0mjiO8zL"
                },
                "href": "https://api.spotify.com/v1/albums/2TeGNWZYaj9yeM0mjiO8zL",
                "id": "2TeGNWZYaj9yeM0mjiO8zL",
                "images": [
                    {
                        "height": 640,
                        "url": "https://i.scdn.co/image/ab67616d0000b273069c2ee3bae4205c1fed2981",
                        "width": 640
                    },
                    {
                        "height": 300,
                        "url": "https://i.scdn.co/image/ab67616d00001e02069c2ee3bae4205c1fed2981",
                        "width": 300
                    },
                    {
                        "height": 64,
                        "url": "https://i.scdn.co/image/ab67616d00004851069c2ee3bae4205c1fed2981",
                        "width": 64
                    }
                ],
                "is_playable": true,
                "name": "Nephew (feat. Lil Pump)",
                "release_date": "2018-07-27",
                "release_date_precision": "day",
                "total_tracks": 1,
                "type": "album",
                "uri": "spotify:album:2TeGNWZYaj9yeM0mjiO8zL"
            },
            "artists": [
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/21dooacK2WGBB5amYvKyfM"
                    },
                    "href": "https://api.spotify.com/v1/artists/21dooacK2WGBB5amYvKyfM",
                    "id": "21dooacK2WGBB5amYvKyfM",
                    "name": "Smokepurpp",
                    "type": "artist",
                    "uri": "spotify:artist:21dooacK2WGBB5amYvKyfM"
                },
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/3wyVrVrFCkukjdVIdirGVY"
                    },
                    "href": "https://api.spotify.com/v1/artists/3wyVrVrFCkukjdVIdirGVY",
                    "id": "3wyVrVrFCkukjdVIdirGVY",
                    "name": "Lil Pump",
                    "type": "artist",
                    "uri": "spotify:artist:3wyVrVrFCkukjdVIdirGVY"
                }
            ],
            "disc_number": 1,
            "duration_ms": 202962,
            "explicit": true,
            "external_ids": {
                "isrc": "USUM71810095"
            },
            "external_urls": {
                "spotify": "https://open.spotify.com/track/67KvputYgCRghvDQYj5FMq"
            },
            "href": "https://api.spotify.com/v1/tracks/67KvputYgCRghvDQYj5FMq",
            "id": "67KvputYgCRghvDQYj5FMq",
            "is_local": false,
            "is_playable": true,
            "linked_from": {
                "external_urls": {
                    "spotify": "https://open.spotify.com/track/0ibOcbkp2XG46Do8jcy0bL"
                },
                "href": "https://api.spotify.com/v1/tracks/0ibOcbkp2XG46Do8jcy0bL",
                "id": "0ibOcbkp2XG46Do8jcy0bL",
                "type": "track",
                "uri": "spotify:track:0ibOcbkp2XG46Do8jcy0bL"
            },
            "name": "Nephew (feat. Lil Pump)",
            "popularity": 50,
            "preview_url": "https://p.scdn.co/mp3-preview/bc901043dd4bcb1c43f6e7b1642e2d9d93b9539a?cid=b800bf59070c4b52a8917d2230d25bdc",
            "track_number": 1,
            "type": "track",
            "uri": "spotify:track:67KvputYgCRghvDQYj5FMq"
        },
        {
            "album": {
                "album_type": "ALBUM",
                "artists": [
                    {
                        "external_urls": {
                            "spotify": "https://open.spotify.com/artist/5xtqw2B8z8JGfDYi2eAZHI"
                        },
                        "href": "https://api.spotify.com/v1/artists/5xtqw2B8z8JGfDYi2eAZHI",
                        "id": "5xtqw2B8z8JGfDYi2eAZHI",
                        "name": "Sonique",
                        "type": "artist",
                        "uri": "spotify:artist:5xtqw2B8z8JGfDYi2eAZHI"
                    }
                ],
                "external_urls": {
                    "spotify": "https://open.spotify.com/album/4LX27S3cszKEJW84BGa1Ff"
                },
                "href": "https://api.spotify.com/v1/albums/4LX27S3cszKEJW84BGa1Ff",
                "id": "4LX27S3cszKEJW84BGa1Ff",
                "images": [
                    {
                        "height": 640,
                        "url": "https://i.scdn.co/image/ab67616d0000b2732b30281b18d808c60135837c",
                        "width": 640
                    },
                    {
                        "height": 300,
                        "url": "https://i.scdn.co/image/ab67616d00001e022b30281b18d808c60135837c",
                        "width": 300
                    },
                    {
                        "height": 64,
                        "url": "https://i.scdn.co/image/ab67616d000048512b30281b18d808c60135837c",
                        "width": 64
                    }
                ],
                "is_playable": true,
                "name": "Hear My Cry",
                "release_date": "2000-08-24",
                "release_date_precision": "day",
                "total_tracks": 13,
                "type": "album",
                "uri": "spotify:album:4LX27S3cszKEJW84BGa1Ff"
            },
            "artists": [
                {
                    "external_urls": {
                        "spotify": "https://open.spotify.com/artist/5xtqw2B8z8JGfDYi2eAZHI"
                    },
                    "href": "https://api.spotify.com/v1/artists/5xtqw2B8z8JGfDYi2eAZHI",
                    "id": "5xtqw2B8z8JGfDYi2eAZHI",
                    "name": "Sonique",
                    "type": "artist",
                    "uri": "spotify:artist:5xtqw2B8z8JGfDYi2eAZHI"
                }
            ],
            "disc_number": 1,
            "duration_ms": 240866,
            "explicit": false,
            "external_ids": {
                "isrc": "USUR10300602"
            },
            "external_urls": {
                "spotify": "https://open.spotify.com/track/4Y8q64VnhD0vFYy9g2WFpi"
            },
            "href": "https://api.spotify.com/v1/tracks/4Y8q64VnhD0vFYy9g2WFpi",
            "id": "4Y8q64VnhD0vFYy9g2WFpi",
            "is_local": false,
            "is_playable": true,
            "name": "It Feels So Good",
            "popularity": 67,
            "preview_url": "https://p.scdn.co/mp3-preview/028068f83d3d988b1661c03e93ab0651f6dd5957?cid=b800bf59070c4b52a8917d2230d25bdc",
            "track_number": 1,
            "type": "track",
            "uri": "spotify:track:4Y8q64VnhD0vFYy9g2WFpi"
        }
    ],
    "seeds": [
        {
            "initialPoolSize": 378,
            "afterFilteringSize": 378,
            "afterRelinkingSize": 378,
            "id": "4NHQUGzhtTLFvgF5SZesLK",
            "type": "ARTIST",
            "href": "https://api.spotify.com/v1/artists/4NHQUGzhtTLFvgF5SZesLK"
        },
        {
            "initialPoolSize": 400,
            "afterFilteringSize": 400,
            "afterRelinkingSize": 400,
            "id": "0c6xIDDpzE81m2q797ordA",
            "type": "TRACK",
            "href": "https://api.spotify.com/v1/tracks/0c6xIDDpzE81m2q797ordA"
        },
        {
            "initialPoolSize": 404,
            "afterFilteringSize": 404,
            "afterRelinkingSize": 404,
            "id": "classical",
            "type": "GENRE",
            "href": null
        },
        {
            "initialPoolSize": 369,
            "afterFilteringSize": 369,
            "afterRelinkingSize": 369,
            "id": "hip-hop",
            "type": "GENRE",
            "href": null
        }
    ]
}
"""

def get_genres(abridged:bool = True, debug = True):
    '''
    Asks Spotify for a list of available genres. If `abridged` is True,
    returns a shortened hard-coded list rather than asking Spotify for the complete list.

    Args:
        abridged (`bool`): whether or not you want the shorter list of genres.
        debug (`bool`): whether or not you want the debug messages to be printed.

    Returns:
        a `list` of `str` representing valid genres.
    '''
    if abridged:
        return [
            "alternative", "ambient", "blues",
            "chill", "country", "dance", "electronic", "folk",
            "funk", "happy", "hip-hop", "indie-pop", "jazz", "k-pop", "metal",
            "new-release", "pop", "punk", "reggae", "rock",
            "soul", "study", "trance", "work-out", "world-music"
        ]

    url = 'https://api.spotify.com/v1/recommendations/available-genre-seeds'
    data = _issue_get_request(url, debug=debug)
    return data['genres']

def get_tracks(search_term: str, debug:bool = True, simplify: bool = True):
    '''
    Retrieves a list of Spotify tracks, given the search term passed in.

    Args:
        search_term (`str`): A search term (for a song), represented as a string.
        debug (`bool`): Whether or not you want debug text to be printed.
        simplify (`bool`): Indicates whether you want to simplify the data that is returned.

    Returns:
        a `list` of tracks.
    '''
    url = 'https://api.spotify.com/v1/search?q=' + search_term + '&type=track'
    data = _issue_get_request(url, debug=debug)
    if not simplify:
        return data
    return _simplify_tracks(data['tracks']['items'], debug=debug)


def get_top_tracks_by_artist(artist_id: str, debug:bool = True, simplify: bool = True):
    '''
    Retrieves a list of Spotify "top tracks" by an artist

    Args:a
        artist_id (`str`): The Spotify id of the artist.
        debug (`bool`): Whether or not you want debug text to be printed.
        simplify (`bool`): Indicates whether you want to simplify the data that is returned.

    Returns:
        a `list` of tracks.
    '''
    if len(artist_id) != 22:
        raise TypeError(f"This function expects an Artist ID but you gave it {artist_id}.")
    
    url = 'https://api.spotify.com/v1/artists/' + \
        artist_id + '/top-tracks?country=us'
    data = _issue_get_request(url, debug=debug)
    if not simplify:
        return data
    return _simplify_tracks(data['tracks'], debug=debug)


def get_playlist_tracks(playlist_id: str, debug:bool = True, simplify: bool = True):
    '''
    Retrieves a list of the tracks associated with a playlist_id.

    Args:
        playlist_id (`str`): The id of the Spotify playlist.
        debug (`bool`): Whether or not you want debug text to be printed.
        simplify (`bool`):  Whether you want to simplify the data that is returned.

    Returns:
        a `list` of tracks.
    '''
    url = 'https://api.spotify.com/v1/playlists/' + playlist_id + '/tracks'
    data = _issue_get_request(url, debug=debug)
    if not simplify:
        return data

    def get_track(item):
        return item['track']
    tracks = list(map(get_track, data['items']))
    return _simplify_tracks(tracks, debug=debug)


def get_related_artists(artist_id: str, debug:bool = True, simplify: bool = True):
    '''
    Retrieves a list of artists who are "related" to the artist you specify (according to Spotify).

    Args:
        artist_id (`str`): [Required] The Spotify id of the artist, represented as a string.
        debug (`bool`): Whether or not you want debug text to be printed.
        simplify (`bool`):   Indicates whether you want to simplify the data that is returned.

    Returns:
        a `list` of artists.
    '''
    if len(artist_id) != 22:
        raise TypeError(f"This function expect an Artist ID but you gave it {artist_id}.")
    url = 'https://api.spotify.com/v1/artists/' + artist_id + '/related-artists'
    data = _issue_get_request(url, debug=debug)
    if not simplify:
        return data
    return _simplify_artists(data['artists'], debug=debug)


def get_artists(search_term: str, debug:bool = True, simplify: bool = True):
    '''
    Retrieves a list of Spotify artists, given the search term passed in.

    Args:
        search_term (`str`): A search term (for an artist), represented as a string.
        debug (`bool`): Whether or not you want debug text to be printed.
        simplify (`bool`): Indicates whether you want to simplify the data that is returned.

    Returns:
        a `list` of artists.
    '''
    url = 'https://api.spotify.com/v1/search?q=' + search_term + '&type=artist'
    data = _issue_get_request(url, debug=debug)
    if not simplify:
        return data
    return _simplify_artists(data['artists']['items'], debug=debug)


def get_playlists(search_term: str, debug:bool = True, simplify: bool = True):
    '''
    Retrieves a list of Spotify playlists, given the search term passed in.

    Args:
        search_term (`str`): A search term (for a song), represented as a string.
        debug (`bool`): Whether or not you want debug text to be printed.
        simplify (`bool`): Indicates whether you want to simplify the data that is returned.

    Returns:
        a `list` of playlists.
    '''
    url = 'https://api.spotify.com/v1/search?q=' + search_term + '&type=playlist'
    data = _issue_get_request(url, debug=debug)
    if not simplify:
        return data
    return _simplify_playlists(data['playlists']['items'], debug=debug)


def get_playlists_by_user(user_id: str, debug:bool = True, simplify: bool = True):
    '''
    Retrieves a list of Spotify playlists belonging to a particular user.

    Args:
        user_id (`str`): A valid Spotify user id, represented as a string.
        debug (`bool`): Whether or not you want debug text to be printed.
        simplify (`bool`): Indicates whether you want to simplify the data that is returned.

    Returns:
        a `list` of playlists belonging to the user.
    '''
    url = 'https://api.spotify.com/v1/users/' + user_id + '/playlists'
    data = _issue_get_request(url, debug=debug)
    if not simplify:
        return data
    return _simplify_playlists(data['items'], debug=debug)


def get_audio_features_by_track(track_id: str, debug:bool = True):
    '''
    Retrieves Spotify's audio analysis of the track.

    Args:
        track_id` (`str`): [Required] The id of the Spotify track.
        debug (`bool`): Whether or not you want debug text to be printed.

    Returns:
        a `list` of audio features.
    '''
    url = 'https://api.spotify.com/v1/audio-features/' + track_id
    return _issue_get_request(url, debug=debug)


def get_similar_tracks(artist_ids: list = [], track_ids: list = [], genres: list = [], debug: bool = True, practice:bool = True, simplify: bool = True):
    '''
    Spotify's way of providing recommendations. One or more params is required:
    artist_ids, track_ids, or genres. Up to 5 seed values may be provided in
    any combination of seed_artists, seed_tracks and seed_genres. In other words:
    len(artist_ids) + len(track_ids) + len(genres) between 1 and 5. You MUST provide
    at least one seed artist or track.

    Args:
        artist_ids (`list`): A list of artist ids (list of strings). Example: `[ '06HL4z0CvFAxyc27GXpf02', '3Nrfpe0tUJi4K4DXYWgMUX' ]`
        track_ids (`list`): A list of track ids. Example: `[ '5ZBeML7Lf3FMEVviTyvi8l', '29U7stRjqHU6rMiS8BfaI9' ]`
        genres (`list`): A list of genres. Example: `[ 'chill' ]`
        debug (`bool`): Whether or not you want debug text to be printed.
        practice (`bool`): Whether or not you want real data <mark>ONLY DO THIS IF YOU HAVE SUCCESSFULLY GOTTEN PRACTICE DATA WORKING</mark>

    Returns:
        a `list` of tracks that are similar
    '''
    if not artist_ids and not track_ids and not genres:
        raise Exception('Either artist_ids or track_ids or genres required')

    # check if seeds <= 5:
    artist_ids = list(artist_ids) or []
    track_ids = list(track_ids) or []
    genres = list(genres) or []
    if len(artist_ids) + len(track_ids) + len(genres) > 5:
        error = 'You can only have 5 "seed values" in your recommendations query.\n' + \
            'In other words, (len(artist_ids) + len(track_ids) + len(genres)) must be less than or equal to 5.'
        raise Exception(error)

    params = []
    if artist_ids:
        artist_ids = sorted(artist_ids)
        for i in artist_ids:
            if len(i) != 22:
                raise TypeError(f"This input requires Artist IDs but you gave it {i}.")
        params.append('seed_artists=' + ','.join(artist_ids))
    if track_ids:
        track_ids = sorted(track_ids)
        for i in track_ids:
            if len(i) != 22:
                raise TypeError(f"This input requires Track IDs but you gave it {i}.")
        params.append('seed_tracks=' + ','.join(track_ids))
    if genres:
        genres = sorted(genres)
        params.append('seed_genres=' + ','.join(genres))

    url = 'https://api.spotify.com/v1/recommendations?' + '&'.join(params)
        
    data = _issue_get_request(url, debug=debug, practice=practice)
    
    if not simplify:
        return data

    if 'tracks' not in data:
        raise Exception("We didn't get any track data back from Spotify. Double check the debugging URL to see you're using valid inputs!")
    
    return _simplify_tracks(data['tracks'], debug=debug)


#############################
# Some formatting utilities #
#############################

def get_track_player_html(track_id: str):
    '''
    Creates the HTML tags for a Spotify player.

    Args:
        track_id (`str`): The id of a track.

    Returns:
      a `str` with an HTML iframe corresponding to a Spotify player for the track.
    '''
    return '''
    <iframe src="https://open.spotify.com/embed?uri=spotify:track:{track_id}&amp;theme=white" width="300" height="80" frameborder="0" allowtransparency="true" allow="encrypted-media" data-testid="audio-player">
    </iframe>
    '''.format(track_id=track_id)


def get_playlist_player_html(playlist_id: str, width: int = 400, height: int = 280):
    '''
    Generates an Spotify playlist player.

    Args:
        playlist_id (`str`): The Spotify playlist id.
        width (`int`): The width of the player.
        height (`int`): The height of the player.

    Returns:
        a `str` representation of an HTML iframe corresponding to the playlist.
    '''
    return '''
    <iframe src="https://open.spotify.com/embed/playlist/{playlist_id}"
        width="{width}" height="{height}" frameborder="0" allowtransparency="true"
        allow="encrypted-media">
    </iframe>'''.format(playlist_id=playlist_id, width=width, height=height)


def get_album_player_html(album_id: str, width: int = 300, height: int = 380):
    '''
    Generates an Spotify album player.

    Args:
        album_id (`str`): The Spotify album id.
        width (`int`): The width of the player.
        height (`int`): The height of the player.

    Returns:
        a `str` representation of an HTML iframe corresponding to the album.
    '''
    return '''
    <iframe src="https://open.spotify.com/embed/album/{album_id}"
        width="{width}" height="{height}" frameborder="0" allowtransparency="true"
        allow="encrypted-media">
    </iframe>'''.format(album_id=album_id, width=width, height=height)


def generate_tracks_table(tracks: list, to_html: bool = False):
    '''
    Function that builds a string representation of the tracks.

    Args:
        tracks (`list`): List of tracks.
        to_html (`bool`): If `True` it will generate an HTML version (for an email or web page) and if `False` (default) will generate a string to print in Python.

    Returns:
        a table as a `str`
    '''
    
    if to_html:
        return _get_formatted_tracklist_table_html(tracks)

    line_width = 95
    text = ''
    template = '{0:2} | {1:<22.22} | {2:<30.30} | {3:<30.30}\n'

    # header section:
    text += '-' * line_width + '\n'
    text += template.format(
        '', 'Name', 'Artist', 'Album'
    )
    text += '-' * line_width + '\n'

    # data section:
    counter = 1
    for track in tracks:
        text += template.format(
            counter,
            track.get('name'),
            track.get('artist').get('name'),
            track.get('album').get('name')
        )
        counter += 1
    text += '-' * line_width + '\n'
    return text


def generate_artists_table(artists: list, to_html:bool=False):
    '''
    Makes a nice formatted table of artists. Good for writing to an
    HTML file or showing on the screen.

    Args:
        artists (`list`): A list of artists.
        to_html (`bool`): Whether or not you want the HTML version.

    Returns:
        a `str` with an HTML table in it.
    '''
    if not artists:
        raise TypeError(f"A list of artists is required but you gave us a {type(artists)}: {artists}")

    if to_html:
        return _get_artist_table_html(artists)

    line_width = 118
    text = ''
    template = '{0:2} | {1:<22.22} | {2:<30.30} | {3:<60.60}\n'

    # header section:
    text += '-' * line_width + '\n'
    text += template.format(
        '', 'Name', 'Genres', 'URL'
    )
    text += '-' * line_width + '\n'

    # data section:
    counter = 1
    for artist in artists:
        text += template.format(
            counter,
            artist.get('name'),
            artist.get('genres'),
            artist.get('share_url')
        )
        counter += 1
    text += '-' * line_width + '\n'
    return text

    

def _get_artist_table_html(artists: list):
    template = '''
        <tr>
            <td {css}>{name}</td>
            <td {css}><img src="{image_url}" /></td>
            <td {css}>{genres}</td>
            <td {css}><a href="{share_url}">Listen on Spotify</a></td>
        </tr>
    '''
    cell_css = 'style="padding:3px;border-bottom:solid 1px #CCC;border-right:solid 1px #CCC;"'
    table_css = 'style="width:100%;border:solid 1px #CCC;border-collapse:collapse;margin-bottom:10px;"'

    rows = []

    # data section:
    ['name', 'image_url_small', 'genres', 'share_url']
    for artist in artists:
        rows.append(
            template.format(
                css=cell_css,
                name=artist.get('name'),
                image_url=artist.get('image_url_small'),
                genres=artist.get('genres'),
                share_url=artist.get('share_url')
            )
        )

    return '''
        <table {table_css}>
            <tr>
                <th {css}>Name</th>
                <th {css}>Image</th>
                <th {css}>Genres</th>
                <th {css}>More</th>
            </tr>
            {rows}
        </table>
    '''.format(css=cell_css, table_css=table_css, rows=''.join(rows))


def _get_formatted_tracklist_table_html(tracks: list):
    '''
    Makes a nice formatted HTML table of tracks. Good for writing to an
    HTML file or for sending in an email.

    Args:
        tracks (`list`): [Required] A list of tracks.

    Returns:
        a `str` with an HTML table in it.
    '''
    if not tracks:
        raise TypeError(f"A list of tracks is required but you gave us a {type(tracks)}: {tracks}")

    template = '''
        <tr>
            <td {css}>{name}</td>
            <td {css}><img src="{image_url}" /></td>
            <td {css}>{artist_name}</td>
            <td {css}>{album_name}</td>
            <td {css}><a href="{share_url}">Listen on Spotify</a></td>
        </tr>
    '''
    cell_css = 'style="padding:3px;border-bottom:solid 1px #CCC;border-right:solid 1px #CCC;"'
    table_css = 'style="width:100%;border:solid 1px #CCC;border-collapse:collapse;margin-bottom:10px;"'

    rows = []

    # data section:
    ['name', 'album_image_url_small', 'artist_name', 'album_name', 'share_url']
    for track in tracks:
        rows.append(
            template.format(
                css=cell_css,
                name=track.get('name'),
                image_url=track.get('album').get('image_url_small'),
                artist_name=track.get('artist').get('name'),
                album_name=track.get('album').get('name'),
                share_url=track.get('share_url')
            )
        )

    return '''
        <table {table_css}>
            <tr>
                <th {css}>Name</th>
                <th {css}>Image</th>
                <th {css}>Artist</th>
                <th {css}>Album</th>
                <th {css}>More</th>
            </tr>
            {rows}
        </table>
    '''.format(css=cell_css, table_css=table_css, rows=''.join(rows))


############################################
# Some private, helper functions utilities #
############################################

def _generate_authentication_header(backup=False, debug=True):
    not_cached = True
    alt_in_use = False
    shoud_i_remove = False
    if os.path.isfile(SPOTIFY_JSON):
        with open(SPOTIFY_JSON) as json_file:
            data = json.load(json_file)
            if time.time() >= float(data['expires']):
                if debug:
                    print("DEBUG: Auth token expired, time to refresh!")
                should_i_remove = True
            else:
                token = data['token']
                not_cached = False
    
    if shoud_i_remove:
        time.sleep(0.2)
        os.remove(SPOTIFY_JSON)

    if not_cached:
        if debug:
            print("DEBUG: Generating new Spotify Authentication Token...") 
        from apis import secret_tokens
        
        current_timestamp = int(time.time())
        if current_timestamp % 10 < 7:
            alt_in_use = True
            client_id = secret_tokens.ALT_SPOTIFY_CLIENT_ID
            client_secret = secret_tokens.ALT_SPOTIFY_CLIENT_SECRET
        else:
            client_id = secret_tokens.SPOTIFY_CLIENT_ID
            client_secret = secret_tokens.SPOTIFY_CLIENT_SECRET

        # Step 1 - Authorization
        auth_url = "https://accounts.spotify.com/api/token"
        headers = {}
        data = {}

        # Encode as Base64
        message = f"{client_id}:{client_secret}"
        messageBytes = message.encode('ascii')
        base64Bytes = base64.b64encode(messageBytes)
        base64Message = base64Bytes.decode('ascii')

        headers['Authorization'] = f"Basic {base64Message}"
        data['grant_type'] = "client_credentials"

        if not backup:
            try:
                r = requests.post(auth_url, headers=headers, data=data)
                token = r.json()['access_token']
                with open(SPOTIFY_JSON, "w") as outfile:
                    json_object = json.dumps({ 'token': token, 'expires': time.time() + 3540, 'alt?':alt_in_use }, indent=4)
                    outfile.write(json_object)
                
            except:
                if debug:
                    print("DEBUG: Couldn't use either default API Key. Trying backup!")
                backup = True

    if backup:
        if debug:
            print("DEBUG: Using backup...")
        time.sleep(1)
        if os.path.isfile(SPOTIFY_JSON):
            os.remove(SPOTIFY_JSON)
        
        from apis import authentication
        try:
            token = authentication.get_token(
                'https://www.apitutor.org/spotify/key')
        except Exception as e:
            print("ERROR: COULD NOT COMMUNICATE WITH SPOTIFY. I even tried the backup. Did you run the setup tests?")
            raise Exception(e)
    
    headers = {
        'Authorization': 'Bearer ' + token
    }

    return headers

def _issue_get_request(url, debug = True, practice = True):
    '''
    Private function. Retrieves data from any Spotify endpoint using the authentication key.

    * url (str): [Required] The API Endpoint + query parameters.
    * debug (bool): Whether or not to print debug messages.
    * practice (bool): Whether or not to return real data or practice data

    Returns whatever Spotify's API endpoint gives back.
    '''
    if debug:
        print("DEBUG: Here's the request we're going to make.\n", url, "\nYou can't access it in a browser, but you can double check the inputs you gave the function are part of the URL.")
    
    headers = _generate_authentication_header()
    
    url = url.replace(" ", "%20")
    
    # Check cache
    if os.path.isfile(SPOTIFY_CACHE):
        with open(SPOTIFY_CACHE, 'rb') as file:
            cache = pickle.load(file)
    else:
        cache = {}
    
    if url in cache:
        if debug:
            print("DEBUG: Found previous request! Returning cached result.")
        return cache[url]
    
    if "recommendations" in url and practice:
        if debug:
            print("DEBUG: We're going to give you some practice data since you specified practice mode!")
        returnValue = json.loads(TRACKS_JSON)
        random.shuffle(returnValue['tracks'])
        return returnValue
    
    response = requests.get(url, headers=headers, verify=True)
    if response.status_code == 429:
        retry_length = response.headers['Retry-After']
        if debug:
            print(f"ERROR: Spotify API is overloaded! It asked us to try again in {retry_length} seconds.")
        
        if "recommendations" in url:
            if debug:
                print("DEBUG: We're going to give you some practice data so you can keep working!")
            returnValue = json.loads(TRACKS_JSON)
            random.shuffle(returnValue['tracks'])
            return returnValue
        
        if os.path.isfile(SPOTIFY_JSON):
            os.remove(SPOTIFY_JSON)
        
        if debug:
            print("DEBUG: We're going to try to use the backup...")
        headers = _generate_authentication_header(backup=True)
        response = requests.get(url, headers=headers, verify=True)
        if response.status_code != 200:
            raise Exception("Uh oh. Couldn't use the backup either. It's likely you've given this function invalid inputs!")

    json_response = response.json()
    
    # Save it in the cache
    cache[url] = json_response
    
    with open(SPOTIFY_CACHE, 'wb') as file:
        pickle.dump(cache, file)

    return json_response

def _simplify_tracks(tracks: list, debug=True):
    '''
    Private function. Simplifies the Spotify track data so that each dictionary only contains
    a few key features (the original dictionary is quite large).

    * tracks (list): The original tracks data structure returned from Spotify.

    Returns a list of simplified tracks.
    '''
    try:
        tracks[0]
    except Exception:
        return tracks

    simplified = []
    for item in tracks:
        track = {
            'id': item['id'],
            'name': item['name'],
            'preview_url': item['preview_url'],
            'share_url': 'https://open.spotify.com/track/' + item['id']
        }
        try:
            track['album'] = {
                'id': item['album']['id'],
                'name': item['album']['name'],
                'image_url': item['album']['images'][0]['url'],
                'image_url_small': item['album']['images'][-1]['url'],
                'share_url': 'https://open.spotify.com/album/' + item['album']['id']
            }
        except Exception:
            pass
        try:
            artists = item.get('album').get('artists')
            artist = artists[0]
            track['artist'] = {
                'id': artist['id'],
                'name': artist['name'],
                'share_url': 'https://open.spotify.com/artist/' + item['album']['artists'][0]['id']
            }
        except Exception:
            pass
        simplified.append(track)
    return simplified


def _simplify_artists(artists: list, debug=True):
    '''
    Private function. Simplifies the Spotify artist data so that each dictionary only contains
    a few key features (the original dictionary is quite large).

    * artists (list): The original artists data structure returned from Spotify.

    Returns a list of simplified artists.
    '''
    try:
        artists[0]
    except Exception:
        return artists

    simplified = []
    for item in artists:
        artist = {
            'id': item['id'],
            'name': item['name'],
            'genres': ', '.join(item['genres']),
            'share_url': 'https://open.spotify.com/artist/' + item['id']
        }
        try:
            artist['image_url'] = item['images'][0]['url']
            artist['image_url_small'] = item['images'][-1]['url']
        except Exception:
            pass
        simplified.append(artist)
    return simplified


def _simplify_playlists(playlists: list, debug=True):
    '''
    Private function. Simplifies the Spotify playlist data so that each dictionary only contains
    a few key features (the original dictionary is quite large).

    * playlists (list): The original playlist data structure returned from Spotify.

    Returns a list of simplified playlist entries.
    '''
    try:
        simplified = []
        for item in playlists:
            simplified.append({
                'id': item['id'],
                'name': item['name'],
                'owner_display_name': item['owner']['display_name'],
                'owner_id': item['owner']['id'],
                'share_url': 'https://open.spotify.com/playlist/' + item['id']
            })
        return simplified
    except Exception as e:
        # give a good error message:
        error = 'The following playlist data structure could not be simplified:\n' + \
            str(playlists)
        # print(error)
        raise Exception(error)
