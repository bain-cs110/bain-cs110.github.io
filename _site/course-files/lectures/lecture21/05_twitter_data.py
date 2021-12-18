# NOTE: You need to install requests for this to work by:
# pip3 install requests
# pip install requests

import requests
import pprint # module for making dictionaries more readable

# write a program that:
# 1. Prompts the user for a search term
# 2. Queries Twitter for status updates based on the search term
# 3. Iterates through the resulting data dictionary and
# 4. Prints the text of the status and the number of times it has been retweeted

search_term = input('Please enter a search term: ')
search_term = search_term.replace(' ', '+')
url = 'https://www.apitutor.org/twitter/simple/1.1/search/tweets.json?q='
url += search_term
response = requests.get(url)
statuses = response.json()
print(type(statuses), type(statuses[0]))
pprint.pprint(statuses)