import ssl # for https requests
from urllib.request import urlopen


# 1. get it from the internet
context = ssl._create_unverified_context()
response = urlopen('https://www.apitutor.org/twitter/1.1/search/tweets.json?q=cats', context=context)
file_data = response.read().decode('utf-8', 'ignore')

# 2. print it to the screen
# print(file_data)

# 3. write it to a file
f = open('data.json', 'w')
f.write(file_data)
f.close()
print('Data file written to results/data.json. Go take a look!')