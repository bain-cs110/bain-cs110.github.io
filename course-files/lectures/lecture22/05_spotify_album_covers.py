import requests #need to install it from the command line using pip

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
    print(track.get('album').get('name'), track.get('album').get('image_url'))