from apis import spotify

artists = spotify.get_artists("Rihanna")

counter = 0
for artist in artists:
    print(counter, artist)
    print("*"*10)
    counter += 1

an_artist = artists[0]

print(an_artist['name'], an_artist['id'])

related_artists = spotify.get_related_artists(an_artist['id'])
print(related_artists)
nice_table = spotify.generate_artists_table(related_artists)
print(nice_table)
