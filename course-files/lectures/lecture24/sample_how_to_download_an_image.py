# note: you need to install requests on the command line: 
# pip install requests or pip3 install requests
import requests
from utilities import get_file_path

image_url = 'https://i.scdn.co/image/ab67616d0000b2737dfd2e089cf69a5fd40d2c84'

response = requests.get(image_url, stream=True)
f = open(get_file_path('image.jpg'), 'wb')
for bytes in response.raw:
    f.write(bytes)
f.close()