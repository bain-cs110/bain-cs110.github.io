# note: you need to install requests on the command line: 
# pip install requests or pip3 install requests
import requests
from utilities import get_file_path

song_url = 'https://p.scdn.co/mp3-preview/0b6da17f858f104337fac626c4bac972d3947564?cid=9697a3a271d24deea38f8b7fbfa0e13c'
response = requests.get(song_url, stream=True)
f = open(get_file_path('song.mp3'), 'wb')
for bytes in response.raw:
    f.write(bytes)
f.close()
