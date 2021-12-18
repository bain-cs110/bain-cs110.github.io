import pprint
import requests #need to install it from the command line using pip

'''
1. Prompt the user for a search term 
2. Query the Spotify tracks endpoint for the search term
3. Print the song name and the artist(s) who wrote it. 
'''

search_term = 'Beyonce'

# create query url:
url = 'https://www.apitutor.org/spotify/simple/v1/search?type=track&q='
url += search_term

# print it:
print(url)

# retrieve the data:
response = requests.get(url)
tracks = response.json()

pprint.pprint(tracks) # print all the tracks to the screen