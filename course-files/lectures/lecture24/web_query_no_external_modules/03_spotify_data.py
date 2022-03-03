import ssl
import json
import urllib.request

# This is the file we made in lecture on Monday 
def search_for_tracks(search_term:str):
    # create query url:
    endpoint = 'https://www.apitutor.org/spotify/simple/v1/search' # internet function

    # formulate your query here:
    search_term = search_term.replace(' ', '%20')
    url = endpoint + '?' + 'type=track&q=' + search_term

    # print it:
    print(url)

    # retrieve the data:
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(url, context=context)
    file_data = response.read()

    tracks = json.loads(file_data)
    return tracks



search_term = input('What do you want to listen to? ')
track_list = search_for_tracks(search_term)

for track in track_list:
    print(track.get('name'), '(' + track.get('album').get('name') + ')')