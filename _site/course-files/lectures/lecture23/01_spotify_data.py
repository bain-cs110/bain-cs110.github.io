import requests  # need to install it from the command line using pip on the
# command line or using install_python_packages.py


def write_url_to_file(url: str, file_name: str):
    '''
    A function that that takes as input a URL to a file and a file name and
    downloads the requested url and saves it into the requested file.

    Inputs:
        url (str): the url to download
        file_name (str): the file name to save the download to

    Outputs:
        None. (saves download to file)
    '''
    # Get rid of characters that can't be in file names
    file_name = file_name.replace(" ", "")
    file_name = file_name.replace('/', '')
    file_name = file_name.replace('\'', '')

    # Request the file from the server
    response = requests.get(url, stream=True)

    # Write it to the file
    f = open(file_name, 'wb')
    for bytes in response.raw:
        f.write(bytes)
    f.close()


def search_for_tracks(search_term: str):

    ## TODO - Fill in the endpoint for the Spotify API on APITutor
    endpoint = ''  # internet function

    ## TODO - Fill in the parameter names and values for Tracks on the Spotify API on APITutor
    url = endpoint + '' + search_term

    # print it:
    print(url)

    # retrieve the data:
    response = requests.get(url)
    tracks = response.json()
    return tracks


search_term = input('What do you want to listen to? ')
search_term.replace(" ", "+")

track_list = search_for_tracks(search_term)

print("I got back a", type(track_list))
print("made up of different", type(track_list[0]))

## TODO - Write a for loop that for each track you get back, prints out the
## track name and album name

## TODO - Ask the user to pick a track from the ones you printed out and allow
## them to download an mp3 preview

## TODO - Ask the user to pick a track from the ones you printed out and allow
## them to download an jpg of the album cover
