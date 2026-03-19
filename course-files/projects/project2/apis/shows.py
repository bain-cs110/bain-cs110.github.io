VERSION = 2026.1 # initial version!

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
import math
from urllib.parse import quote

from apis import secret_tokens

TMDB_CACHE = "tmdb_cache.pkl"
__docformat__ = "google"

__all__ = [
    "get_genres",
    "get_on_air",
    "get_popular",
    "get_recommendations",    
    "get_reviews",
    "get_streamers",
    "lookup_show",
    "generate_show_table",
    "generate_watchlist"
]


def get_on_air(limit: int = 10,
                    language: str = "en-US", 
                    region: str = "US", 
                    debug: bool = True, 
                    **kwargs):
    """
    Retrieves a list of the shows (dictionaries) currently playing in theaters.

    Args:
        limit (`int`): The number of shows to include in the response.
        language (`str`): Which spoken language to prioritize.
        region (`str`): Which release region to prioritize.
        debug (`bool`): Whether or not you want debug text to be printed.

    Returns:
        a `list` of shows.
    """
    
    url = f"https://api.themoviedb.org/3//tv/on_the_air?language={language}&region={region}"
    response = _issue_get_request(url, debug=debug, limit=limit, **kwargs)
    return _simplify_shows_list(response['results'], debug=debug)


def get_popular(
    limit: int = 10,
    language: str = "en-US",
    region: str = "US",
    debug: bool = True,
    **kwargs,
):
    """
    Retrieves a list of the shows (dictionaries) that are currently popular.

    Args:
        limit (`int`): The number of shows to include in the response.
        language (`str`): Which spoken language to prioritize.
        region (`str`): Which release region to prioritize.
        debug (`bool`): Whether or not you want debug text to be printed.

    Returns:
        a `list` of shows.
    """

    url = f"https://api.themoviedb.org/3/tv/popular?language={language}&region={region}"
    response = _issue_get_request(url, debug=debug, limit=limit, **kwargs)
    return _simplify_shows_list(response['results'], debug=debug)


def get_reviews(
    show_id: int,
    limit: int = 20,
    language: str = "en-US",
    debug: bool = True,
    **kwargs,
):
    """
    Retrieves a list of reviews (dictionaries) for a show with the given `show_id`. Note that some tv shows
    won't have any reviews!

    Args:
        show_id (`int`): A unique string that corresponds to a particular show.
        limit (`int`): The number of tv shows to include in the response.
        language (`str`): Which spoken language to prioritize.
        debug (`bool`): Whether or not you want debug text to be printed.

    Returns:
        a `list` of show reviews where each is a dictionary
    """

    url = f"https://api.themoviedb.org/3/tv/{show_id}/reviews?language={language}"
    response = _issue_get_request(url, debug=debug, limit=limit, **kwargs)
    if len(response['results']) == 0:
        return [ { "author": "n/a",
                   "author_details": {
                        "name": "",
                        "username": "n/a",
                        "avatar_path": "n/a",
                        "rating": "n/a"
                    },
                "content": "n/a",
                "created_at": "n/a",
                "id": "n/a",
                "updated_at": "n/a",
                "url": "n/a"}]
        
    return response['results']


def get_streamers(show_id: int, debug: bool=True, **kwargs):
    """
    Retrieves a list of streaming services (dictionaries) the given show is available on (powered by JustWatch).

    Args:
        show_id (`int`): A unique id that corresponds to a particular show.
        debug (`bool`): Whether or not you want debug text to be printed.

    Returns:
        a `list` of streaming service names where the given show is available
    """
    
    url = f"https://api.themoviedb.org/3/tv/{show_id}/watch/providers"
    response = _issue_get_request(url, debug=debug, **kwargs)
    return [x['provider_name'] for x in response['results']['US']['flatrate']]


def get_recommendations(
    show_id: int,
    limit: int = 20,
    language: str = "en-US",
    debug: bool = True,
    **kwargs,
):
    """
    Retrieves a list of the shows (dictionaries) similar to the show with given `show_id`.

    Args:
        show_id (`int`): A unique int that corresponds to a particular show.
        limit (`int`): The number of shows to include in the response.
        language (`str`): Which spoken language to prioritize.
        debug (`bool`): Whether or not you want debug text to be printed.

    Returns:
        a `list` of shows (dictionaries)
    """
    url = f"https://api.themoviedb.org/3/tv/{show_id}/recommendations?language={language}"
    response = _issue_get_request(url, debug=debug, limit=limit, **kwargs)
    return _simplify_shows_list(response["results"], debug=debug)


def get_genres(language: str="en-US", debug: bool=True):
    """
    Provides a list of available movie genres genres.

    Args:
        language (`str`): The predominant language for the tv shows you're interested in.
        debug (`bool`): whether or not you want the debug messages to be printed.

    Returns:
        a `list` of `str` representing valid genres.
    """

    raw_genres = _lookup_genres(language=language, debug=debug)
    simple_genres = []
    for item in raw_genres:
        simple_genres.append(raw_genres[item])

    return simple_genres


def lookup_show(show_id: int, debug: bool = True, **kwargs):
    """
    Lookup the details of a show with a given id.

    Args:
        show_id (`int`): The id of the show you'd like to get the details of.
        debug (`bool`): whether or not you want the debug messages to be printed.

    Returns:
        a `dictionary` that represents the show in question
    """
    
    url = f"https://api.themoviedb.org/3/tv/{show_id}"
    show = _issue_get_request(url, debug=debug, **kwargs)
    simple_show = {
            'id': show['id'],
            'name': show['name'],
            'language': show['original_language'],
            'genres': [x['name'] for x in show['genres']],
            'overview': show['overview'],
            'popularity': show['popularity'],
            'first_air_date': show['first_air_date'],
            'poster_path': show['poster_path'],
            'rating': show['vote_average'],
            'num_votes': show['vote_count']
            }
    
    return simple_show


def search_for_shows(genres: list = [], language: str = "en-US", debug: bool = True, length: int = 10, **kwargs):
    
    if len(genres) < 1:
        raise Exception(f"No genre provided in the list given: {genres}")
    
    genres_dict = _lookup_genres(language=language, debug=debug)
    
    genre_ids = []
    
    for genre in genres:
        if genre not in genres_dict.values():
            raise Exception(f"{genre} is not a valid TV Show genre!")
        the_id = [key for key, value in genres_dict.items() if value == genre][0]
        genre_ids.append(str(the_id))
    
    url = f"https://api.themoviedb.org/3/discover/tv?include_adult=false&include_video=false&language={language}&page=1&sort_by=popularity.desc&with_origin_country=US&with_genres={'|'.join(genre_ids)}"
    
    response = _issue_get_request(url, limit=length, debug=debug, **kwargs)
    return _simplify_shows_list(response["results"], debug=debug)


def generate_watchlist(show_ids: list = [], genres: list = [], length: int = 10, debug: bool = True, simplify: bool = True):
    """
    Generate a watch list based off the inputted tv shows and genres. You must provide at least 1 genre for this function to work.
    <mark>Keep in mind it does not accept show names.</mark> Specifying multiple genres might result in getting zero results.</mark>

    Args:
        show_ids (`list`): A list show ids (list of ints). Example: `[ 594767, 76600 ]`
        genres (`list`): A list of genres. <b>Has to have</b> at least length 1. Example: `[ 'Adventure' ]`
        length (`int`): How many shows to return as part of the watchlist
        debug (`bool`): Whether or not you want debug text to be printed.
        
    Returns:
        * a `list` of tv shows (dictionaries)
    """

    if not genres:
        raise Exception('You MUST provide a genre in order to generate a watch list')

    show_list = []

    for show in show_ids:
        if not isinstance(show, int):
            raise TypeError(f"{show} is not a valid movie id!")
        
        the_show = lookup_show(show, debug = debug)
        show_list.append(the_show)

        recs = get_recommendations(the_show["id"], limit = 5, debug=debug)
        show_list = show_list + recs
        

    if genres:
        show_list = show_list + search_for_shows(genres=genres, length=length, debug=debug)
                
    show_list = _remove_duplicate_tv_shows(show_list)
    random.shuffle(show_list)

    return show_list[:length]

def _remove_duplicate_tv_shows(tv_shows):
    
    unique_series_ids = []
    unique_shows = []
    for show in tv_shows:
        if show['id'] in unique_series_ids:
            continue
        else:
            unique_series_ids.append(show['id'])
            unique_shows.append(show)

    return unique_shows


def _simplify_shows_list(shows, language="en-US", debug=True):
    
    genres_dict = _lookup_genres(language=language, debug=debug)
    simplified_shows = []
    for show in shows:
        simplified_shows.append(
            {
                'id': show['id'],
                'name': show['name'],
                'language': show['original_language'],
                'genres': [genres_dict[x] for x in show['genre_ids']],
                'overview': show['overview'],
                'popularity': show['popularity'],
                'first_air_date': show['first_air_date'],
                'poster_path': show['poster_path'],
                'rating': show['vote_average'],
                'num_votes': show['vote_count'],
            }
        )
        
    return simplified_shows

def _lookup_genres(language="en", debug: bool = True):
    
    url = f"https://api.themoviedb.org/3/genre/tv/list?language={language}"
    response = _issue_get_request(url, debug=debug)
    return {item['id']: item['name'] for item in response['genres']}


def _save_to_cache(url: str, response: str):

    if os.path.isfile(TMDB_CACHE):
        with open(TMDB_CACHE, "rb") as file:
            cache = pickle.load(file)
    else:
        cache = {}

    cache[url] = response

    with open(TMDB_CACHE, "wb") as file:
        pickle.dump(cache, file)


def _check_cache_for(url: str, debug=False, **kwargs):
    # Check cache
    if "skip_cache" in kwargs:
        print(
            f"DEBUG - {'_check_cache_for'}: skip_cache flag set, returning None."
        )
        return None

    if os.path.isfile(TMDB_CACHE):
        with open(TMDB_CACHE, "rb") as file:
            cache = pickle.load(file)
    else:
        cache = {}

    if url in cache:
        if debug:
            print(
                f"DEBUG - {'_check_cache_for'}: Found previous request! Returning cached result."
            )
        return cache[url]
    else:
        print(
                f"DEBUG - {'_check_cache_for'}: No cache hit, issuing new request."
            )
        return None


#############################
# Some formatting utilities #
#############################


def generate_show_table(shows: list, to_html: bool = False):
    """
    Function that builds a string representation of a list shows (dictionaries).

    Args:
        shows (`list`): List of shows (dictionaries).
        to_html (`bool`): If `True` it will generate an HTML version (for an email or web page) and if `False` (default) will generate a string to print in Python.

    Returns:
        * a `str` that has a table in it for tracks
    """

    if to_html:
        return _get_show_table_html(shows)

    line_width = 95
    text = ""
    template = "{0:2} | {1:<22.22} | {2:<40.40} | {3:<30.30}\n"

    # header section:
    text += "-" * line_width + "\n"
    text += template.format("", "Name", "Genres", "First Air Date")
    text += "-" * line_width + "\n"


    # data section:
    counter = 1
    for show in shows:
        text += template.format(
            counter,
            show.get("name"),
            ", ".join(show.get("genres", [])),
            show.get("first_air_date", "N/A")
        )
        counter += 1
    text += "-" * line_width + "\n"
    return text


def _get_show_table_html(shows : list):
    template = """
        <tr>
            <td {css}>{name}</td>
            <td {css}><img src="{image_url}" /></td>
            <td {css}>{genres}</td>
            <td {css}>{first_air_date}</td>
            <td {css}><p>{overview}</p></td>
        </tr>
    """
    cell_css = (
        'style="padding:3px;border-bottom:solid 1px #CCC;border-right:solid 1px #CCC;"'
    )
    table_css = 'style="width:100%;border:solid 1px #CCC;border-collapse:collapse;margin-bottom:10px;"'

    rows = []

    # data section:
    for show in shows:        
        full_path = show.get("poster_path", "Unavailable")
        
        if full_path != "Unavailable":
            full_path = f"http://image.tmdb.org/t/p/w92{full_path}"
        
        rows.append(
            template.format(
                css=cell_css,
                name=show.get("name", "Unknown"),
                image_url=full_path,
                genres=",".join(show.get("genres", [])),
                first_air_date=show.get("first_air_date", "N/A"),
                overview=show.get("overview", "Unavailable"),
            )
        )

    return """
        <table {table_css}>
            <tr>
                <th {css}>Name</th>
                <th {css}>Poster</th>
                <th {css}>Genres</th>
                <th {css}>First Air Date</th>
                <th {css}>Overview</th>
            </tr>
            {rows}
        </table>
    """.format(
        css=cell_css, table_css=table_css, rows="".join(rows)
    )


############################################
# Some private, helper functions utilities #
############################################

def _generate_authentication_header(backup=False, debug=True):

    headers = {
        "Authorization": "Bearer " + secret_tokens.TMDB_TOKEN,
        "accept": "application/json",
    }

    return headers


def _issue_get_request(url: str, debug: bool=True, limit:int = 20, practice: bool=True, **kwargs):
    """
    Private function. Retrieves data from any TMDB endpoint using the requisite headers.

    * url (str): The API Endpoint + query parameters.
    * debug (bool): Whether or not to print debug messages.
    * practice (bool): Whether or not to return real data or practice data

    Returns whatever TMDB's API endpoint gives back.
    """
    pages_requested = math.ceil(limit / 20)

    headers = _generate_authentication_header(debug=debug)
    url = quote(url, safe="/:?&,=-")

    MAX_PAGE_LIMIT = pages_requested if pages_requested < 5 else 5 # Limits paged requests to 5

    current_page = 1
    all_responses = []
    while current_page <= MAX_PAGE_LIMIT:
        request_url = url if current_page == 1 else url + f"&page={current_page}"

        if debug:
            print(
                f"DEBUG - {'_issue_get_request'}:\n",
                request_url,
                "\nYou can't access this in a browser, but you can double check the inputs you gave the function are part of the URL.",
            )

        response = _check_cache_for(request_url, debug=debug, **kwargs)

        if response is None: # No cache hit
            response = requests.get(request_url, headers=headers, verify=True)

        if response.status_code == 429:
            retry_length = response.headers["Retry-After"]

            if int(retry_length) < 10:
                print(
                    f"Warning: TMDB API is overloaded! It asked us to try again in {retry_length} seconds so we're going to wait that long and try again."
                )
                time.sleep(retry_length)
            else:
                print(
                    f"ERROR: TMDB API is overloaded! It asked us to try again in {retry_length} seconds."
                )
                return None

        _save_to_cache(request_url, response)
        
        all_responses.append(response)
        current_page += 1

    if len(all_responses) == 1:
        return all_responses[0].json()

    combined_response = all_responses[0].json()
    for response in all_responses[1:]: # if this was paginated, take all results and combine them   
        combined_response['results'] += response.json()['results']
        return combined_response

    return None # Should never get here
