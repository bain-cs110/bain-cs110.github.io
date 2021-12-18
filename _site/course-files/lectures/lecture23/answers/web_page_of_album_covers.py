import utilities
import requests #need to install it from the command line using pip
import utilities

template = '''
    <html>
        <head><title>{name}</title></head>
        <body>
            <h1>{name}</h1>
            {album_covers}
        </body>
    </html>
'''



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

images = ''
for track in tracks:
    album_url = track.get('album').get('image_url')
    album_name = track.get('album').get('name')
    if album_url is None:
        continue

    images += '<img src="{url}" />\n'.format(url=album_url)

html = template.format(name=term, album_covers=images)
f = open(utilities.get_file_path('album_covers.html'), 'w')
f.write(html)
f.close()
