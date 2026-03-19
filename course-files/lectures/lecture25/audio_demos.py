from apis import audio

possible_matches = audio.search_for_artists("Rihanna")

counter = 0
for artist in possible_matches:
    print(counter, artist)
    print("*"*10)
    counter = counter + 1

nice_table = audio.generate_artists_table(possible_matches)
print(nice_table)

an_artist = possible_matches[0]
print(an_artist["name"], an_artist["id"])

favorite_artists = {an_artist["name"]: an_artist["id"]}

some_tracks = audio.get_top_tracks_by_artist(favorite_artists["Rihanna"])

table_of_tracks = audio.generate_tracks_table(some_tracks)
print(table_of_tracks)