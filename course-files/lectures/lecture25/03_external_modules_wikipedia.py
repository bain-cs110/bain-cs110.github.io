# To get this program to work, you must install wikipedia using pip:
# pip3 install wikipedia

import wikipedia

term = input('What do you want to search for? ')
results = wikipedia.search(term)

print(results)

page = wikipedia.page('Chicago')
print(page.content)
