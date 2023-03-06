import urllib.request
import json
import ssl
import pprint

def print_data_and_type(description, data):
    print('{} ({}):\n{}\n'.format(description, type(data), data))

def search_for_tweet(search_term):
    """
    Function to search for a given tweet on Twitter.

    Parameters:
      * search_term (str): the string that reprents what to search for

    Returns:
      * list of results (dictionaries)
    """
    
    # Necessary for accessing data via https protocol
    context = ssl._create_unverified_context()
    # Think of it like a handshake saying "I am not a robot"

    # Ever notice URLs don't have spaces?
    search_term = search_term.replace(' ', '+')

    function_url = 'https://www.apitutor.org/twitter/simple/1.1/search/tweets.json'

    parameter_name = '?q='

    url = function_url + parameter_name + search_term

    # First ask Python to call the function on the endpoint using our URL
    response = urllib.request.urlopen(url, context=context)
    #print_data_and_type("Response", response)

    # Ask Python to read the special file we've gotten back
    raw_data = response.read()
    #print_data_and_type("Raw Data", raw_data)

    # Ask python to convert that file into a string
    decoded_data = raw_data.decode()
    #print_data_and_type("Decoded Data", decoded_data)

    # Ask Python to turn that string into a list of dictionaries
    results = json.loads(decoded_data)
    
    return results

search_results = search_for_tweet("south carolina basketball")

for result in search_results:
    print(result)
