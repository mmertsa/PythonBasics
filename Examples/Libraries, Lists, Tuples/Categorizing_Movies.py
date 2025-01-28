# List of movies
movies = [
    {"name": "The Misadventures of Inspector Palmu", "year": 1960},
    {"name": "Away We Go", "year": 1996},
    {"name": "The Man Without a Past", "year": 2002},
    {"name": "Harry Potter", "year": 1999},
    {"name": "Mean Girls", "year": 2004},
    {"name": "The Unknown Soldier", "year": 2017}
]

old_movies = []  # Movies before the year 2000
new_movies = []   # Movies from 2000 onwards

# Categorizing movies based on their release year
for movie in movies:
    if movie["year"] < 2000:
        old_movies.append(movie)
    else:
        new_movies.append(movie)

# Outputting the results
print("The following movies were released before the year 2000:")
for movie in old_movies:
    print("-", movie["name"])

print()  # Print a blank line for better readability

print("The following movies were released in the 2000s:")
for movie in new_movies:
    print("-", movie["name"])
