fave_things = {
    "fave_cookie": "chocolate chip",
    "fave_song": "Baby Shark",
    "fave_num": 9,
    "fave_bool": True,
    "fave_emoji": "🐍"
}

for key in fave_things:
    print(key, "->", fave_things.get(key))

fave_things["fave_emoji"]  = "😱"
fave_things["fave_color"]  = "orange"

for key in fave_things:
    print(key, "->", fave_things.get(key))
