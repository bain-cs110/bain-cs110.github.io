# note: you need to install requests on the command line: 
# pip install requests or pip3 install requests
import requests
from utilities import get_file_path

image_url = 'https://p.scdn.co/mp3-preview/ed0edd20da985c6a21ae1125e9a3d9072a08e3d1?cid=9697a3a271d24deea38f8b7fbfa0e13c'

response = requests.get(image_url, stream=True)
f = open(get_file_path('song.mp3'), 'wb')
for bytes in response.raw:
    f.write(bytes)
f.close()