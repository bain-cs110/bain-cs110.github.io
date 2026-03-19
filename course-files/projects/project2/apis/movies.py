VERSION = 2026.4 # fix limit bug for tmdb
# 2026.3 fix for windows f-string bug

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
    "get_now_playing",
    "get_upcoming",
    "get_recommendations",    
    "get_reviews",
    "get_streamers",
    "lookup_movie",
    "generate_movie_table",
    "generate_watchlist"
]

def get_now_playing(limit: int = 10, 
                    language: str = "en-US", 
                    region: str = "US", 
                    debug: bool = True, 
                    **kwargs):
    """
    Retrieves a list of the movies (dictionaries) currently playing in theaters.

    Args:
        limit (`int`): The number of movies to include in the response.
        language (`str`): Which spoken language to prioritize.
        region (`str`): Which release region to prioritize.
        debug (`bool`): Whether or not you want debug text to be printed.

    Returns:
        a `list` of movies.
    """
    
    url = f"https://api.themoviedb.org/3/movie/now_playing?language={language}&region={region}"
    response = _issue_get_request(url, debug=debug, limit=limit, **kwargs)
    return _simplify_movies_list(response['results'], debug=debug)


def get_upcoming(
    limit: int = 10,
    language: str = "en-US",
    region: str = "US",
    debug: bool = True,
    **kwargs,
):
    """
    Retrieves a list of the movies (dictionaries) that will be playing in movies soon.

    Args:
        limit (`int`): The number of movies to include in the response.
        language (`str`): Which spoken language to prioritize.
        region (`str`): Which release region to prioritize.
        debug (`bool`): Whether or not you want debug text to be printed.

    Returns:
        a `list` of movies.
    """

    url = f"https://api.themoviedb.org/3/movie/upcoming?language={language}&region={region}"
    response = _issue_get_request(url, debug=debug, limit=limit, **kwargs)
    return _simplify_movies_list(response['results'], debug=debug)


def get_reviews(
    movie_id: int,
    limit: int = 20,
    language: str = "en-US",
    debug: bool = True,
    **kwargs,
):
    """
    Retrieves a list of reviews (dictionaries) for a movie with the given `movie_id`. Note that some movies
    won't have any reviews!

    Args:
        movie_id (`int`): A unique string that corresponds to a particular movie.
        limit (`int`): The number of movies to include in the response.
        language (`str`): Which spoken language to prioritize.
        debug (`bool`): Whether or not you want debug text to be printed.

    Returns:
        a `list` of movie reviews where each is a dictionary
    """

    url = f"https://api.themoviedb.org/3/movie/{movie_id}/reviews?language={language}"
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


def get_streamers(movie_id: int, debug: bool=True, **kwargs):
    """
    Retrieves a list of streaming services (dictionaries) the given movie is available on (powerd by JustWatch).

    Args:
        movie_id (`int`): A unique string that corresponds to a particular movie.
        debug (`bool`): Whether or not you want debug text to be printed.

    Returns:
        a `list` of streaming service names where the given movie is available
    """
    
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/watch/providers"
    response = _issue_get_request(url, debug=debug, **kwargs)
    return [x['provider_name'] for x in response['results']['US']['flatrate']]


def get_recommendations(
    movie_id: int,
    limit: int = 20,
    language: str = "en-US",
    debug: bool = True,
    **kwargs,
):
    """
    Retrieves a list of the movies (dictionaries) similar to the movie with given `movie_id`.

    Args:
        movie_id (`int`): A unique int that corresponds to a particular movie.
        limit (`int`): The number of movies to include in the response.
        language (`str`): Which spoken language to prioritize.
        debug (`bool`): Whether or not you want debug text to be printed.

    Returns:
        a `list` of movies (dictionaries)
    """
    url = f"https://api.themoviedb.org/3/movie/{movie_id}/recommendations?language={language}"
    response = _issue_get_request(url, debug=debug, limit=limit, **kwargs)
    return _simplify_movies_list(response["results"], debug=debug)


def get_genres(language: str="en-US", debug: bool=True):
    """
    Provides a list of available movie genres genres.

    Args:
        language (`str`): The predominant language for the movies you're interested in.
        debug (`bool`): whether or not you want the debug messages to be printed.

    Returns:
        a `list` of `str` representing valid genres.
    """

    raw_genres = _lookup_genres(language=language, debug=debug)
    simple_genres = []
    for item in raw_genres:
        simple_genres.append(raw_genres[item])

    return simple_genres


def lookup_movie(movie_id: int, debug: bool = True, **kwargs):
    """
    Lookup the details of a movie with a given id.

    Args:
        movie_id (`int`): The id of the movie you'd like to get the details of.
        debug (`bool`): whether or not you want the debug messages to be printed.

    Returns:
        a `dictionary` that represents the movie in question
    """
    
    url = f"https://api.themoviedb.org/3/movie/{movie_id}"
    movie = _issue_get_request(url, debug=debug, **kwargs)
    
    simple_movie = {
            'id': movie['id'],
            'title': movie['title'],
            'language': movie['original_language'],
            'genres': [x['name'] for x in movie['genres']],
            'overview': movie['overview'],
            'popularity': movie['popularity'],
            'release-date': movie['release_date'],
            'poster_path': movie['poster_path'],
            'rating': movie['vote_average'],
            'num_votes': movie['vote_count']
            }
    
    return simple_movie


def search_for_movies(genres: list = [], language: str = "en-US", debug: bool = True, length: int = 10, **kwargs):
    
    if len(genres) < 1:
        raise Exception(f"No genre provided in the list given: {genres}")
    
    genres_dict = _lookup_genres(language=language, debug=debug)
    
    genre_ids = []
    
    for genre in genres:
        if genre not in genres_dict.values():
            raise Exception(f"{genre} is not a valid Movie genre!")
        the_id = [key for key, value in genres_dict.items() if value == genre][0]
        genre_ids.append(str(the_id))
    
    url = f"https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language={language}&page=1&sort_by=popularity.desc&with_origin_country=US&with_genres={'|'.join(genre_ids)}"
    
    response = _issue_get_request(url, limit=length, debug=debug, **kwargs)
    return _simplify_movies_list(response["results"], debug=debug)


def generate_watchlist(movie_ids: list = [], genres: list = [], length: int = 10, debug: bool = True, simplify: bool = True):
    """
    Generate a watch list based off the inputted movies and genres. You must provide at least 1 genre for this function to work.
    <mark>Keep in mind it does not accept movie names.</mark> Specifying multiple genres might result in getting zero results.</mark>

    Args:
        movie_ids (`list`): A list movie ids (list of ints). Example: `[ 594767, 76600 ]`
        genres (`list`): A list of genres. <b>Has to have</b> at least length 1. Example: `[ 'Adventure' ]`
        length (`int`): How many tracks to return as part of the watchlist
        debug (`bool`): Whether or not you want debug text to be printed.
        
    Returns:
        * a `list` of movies (dictionaries)
    """

    if not genres:
        raise Exception('You MUST provide a genre in order to generate a watch list')

    movie_list = []

    for movie in movie_ids:
        if not isinstance(movie, int):
            raise TypeError(f"{movie} is not a valid movie id!")
        
        the_movie = lookup_movie(movie, debug = debug)
        movie_list.append(the_movie)

        recs = get_recommendations(the_movie["id"], limit = 5, debug=debug)
        movie_list = movie_list + recs
        

    if genres:
        movie_list = movie_list + search_for_movies(genres=genres, length=length, debug=debug)
                
    movie_list = _remove_duplicate_movies(movie_list)
    random.shuffle(movie_list)

    return movie_list[:length]

def _remove_duplicate_movies(movies):
    
    unique_movie_ids = []
    unique_movies = []
    for movie in movies:
        if movie['id'] in unique_movie_ids:
            continue
        else:
            unique_movie_ids.append(movie['id'])
            unique_movies.append(movie)

    return unique_movies

def _simplify_movies_list(movies, language="en-US", debug=True):
    
    genres_dict = _lookup_genres(language=language, debug=debug)
    simplified_movies = []
    for movie in movies:
        simplified_movies.append(
            {
                'id': movie['id'],
                'title': movie['title'],
                'language': movie['original_language'],
                'genres': [genres_dict[x] for x in movie['genre_ids']],
                'overview': movie['overview'],
                'popularity': movie['popularity'],
                'release-date': movie['release_date'],
                'poster_path': movie['poster_path'],
                'rating': movie['vote_average'],
                'num_votes': movie['vote_count'],
            }
        )
        
    return simplified_movies

def _lookup_genres(language="en", debug: bool = True):
    
    url = f"https://api.themoviedb.org/3/genre/movie/list?language={language}"
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


def generate_movie_table(movies: list, to_html: bool = False):
    """
    Function that builds a string representation of a list movies (dictionaries).

    Args:
        movies (`list`): List of movies.
        to_html (`bool`): If `True` it will generate an HTML version (for an email or web page) and if `False` (default) will generate a string to print in Python.

    Returns:
        * a `str` that has a table in it for tracks
    """

    if to_html:
        return _get_movie_table_html(movies)

    line_width = 95
    text = ""
    template = "{0:2} | {1:<22.22} | {2:<40.40} | {3:<30.30}\n"

    # header section:
    text += "-" * line_width + "\n"
    text += template.format("", "Title", "Genres", "Release Date")
    text += "-" * line_width + "\n"


    # data section:
    counter = 1
    for movie in movies:
        text += template.format(
            counter,
            movie.get("title"),
            ", ".join(movie.get("genres", [])),
            movie.get("release-date", "N/A")
        )
        counter += 1
    text += "-" * line_width + "\n"
    return text

def _get_movie_table_html(movies: list):
    template = """
        <tr>
            <td {css}>{title}</td>
            <td {css}><img src="{image_url}" /></td>
            <td {css}>{genres}</td>
            <td {css}>{release_date}</td>
            <td {css}><p>{overview}</p></td>
        </tr>
    """
    cell_css = (
        'style="padding:3px;border-bottom:solid 1px #CCC;border-right:solid 1px #CCC;"'
    )
    table_css = 'style="width:100%;border:solid 1px #CCC;border-collapse:collapse;margin-bottom:10px;"'

    rows = []

    # data section:
    for movie in movies:        
        full_path = movie.get("poster_path", "Unavailable")
        
        if full_path != "Unavailable":
            full_path = f"http://image.tmdb.org/t/p/w92{full_path}"
        
        rows.append(
            template.format(
                css=cell_css,
                title=movie.get("title", "Unknown"),
                image_url=full_path,
                genres=",".join(movie.get("genres", [])),
                release_date=movie.get("release-date", "N/A"),
                overview=movie.get("overview", "Unavailable"),
            )
        )

    return """
        <table {table_css}>
            <tr>
                <th {css}>Title</th>
                <th {css}>Poster</th>
                <th {css}>Genres</th>
                <th {css}>Release Date</th>
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
