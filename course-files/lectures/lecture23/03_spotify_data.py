import requests #need to install it from the command line using pip

# This is the file we made in lecture on Monday 
def search_for_tracks(search_term:str):
    # create query url:
    endpoint = 'https://www.apitutor.org/spotify/simple/v1/search' # internet function

    # formulate your query here:
    url = endpoint + '?' + 'type=track&q=' + search_term

    # print it:
    print(url)

    # retrieve the data:
    response = requests.get(url)
    tracks = response.json()
    return tracks



search_term = input('What do you want to listen to? ')
track_list = search_for_tracks(search_term)

for track in track_list:
    print(track.get('name'), '(' + track.get('album').get('name') + ')')