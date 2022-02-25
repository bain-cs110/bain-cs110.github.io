# NOTE: You need to install requests for this to work by:
# pip3 install requests
# pip install requests

import requests
import shutil
import pprint
from utilities import get_file_path

# Write a program that only prints the text of the most popular 
# tweet (given the search results).

# necessary for accessing data via https protocol:

# search for tracks: https://www.apitutor.org/spotify/simple/v1/search?type=track&q=beyonce
# search for artists: https://www.apitutor.org/spotify/simple/v1/search?type=artist&q=beyonce
# search albums: https://www.apitutor.org/spotify/simple/v1/search?type=album&q=beyonce

search_term = input('Please enter a search term: ')

url = 'https://www.apitutor.org/spotify/simple/v1/search?type=track&q='
url += search_term
print(url)
response = requests.get(url)
data = response.json()

pprint.pprint(data, depth=3) # The first value is another dictionary, the second is a list of dictionaries