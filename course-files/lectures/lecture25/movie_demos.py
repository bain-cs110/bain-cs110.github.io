from apis import movies

upcoming_movies = movies.get_upcoming()

counter = 0
for movie in upcoming_movies:
    print(counter, movie)
    print("*"*10)
    counter = counter + 1

nice_table = movies.generate_movie_table(movies)
print(nice_table)

a_movie = upcoming_movies[0]
print(a_movie["title"], a_movie["id"])

anticipated_movies = {a_movie["name"]: a_movie["id"]}

some_movies = movies.get_recommendations(
    anticipated_movies["Super Mario Galaxy"])

table_of_movies = movies.generate_movie_table(some_movies)
print(table_of_movies)