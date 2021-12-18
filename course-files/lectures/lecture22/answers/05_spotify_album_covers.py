import requests #need to install it from the command line using pip
import utilities
import time

# How do you download some sample audio from the tracks data?
def search_for_tracks(search_term:str):
    search_term = search_term.replace(' ', '%20')
    # create query url:
    url = 'https://www.apitutor.org/spotify/simple/v1/search?type=track&q=' + search_term

    # retrieve the data:
    response = requests.get(url)
    return response.json()

term = input('Enter a search term to look for some tracks: ')
tracks = search_for_tracks(term)

for track in tracks:
    album_url = track.get('album').get('image_url')
    album_name = track.get('album').get('name')
    if album_url is None:
        continue
 
    file_name = album_name.lower().replace(' ', '') + '.jpg'
    file_name = file_name.replace('/', '')
    file_name = file_name.replace('\'', '')
    response = requests.get(album_url, stream=True)
    f = open(utilities.get_file_path(file_name), 'wb')
    for bytes in response.raw:
        f.write(bytes)
    f.close()

    time.sleep(1)