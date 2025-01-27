# The first section demonstrates straightforward access to dictionary values
# without iteration.
# The second section effectively shows how to access dictionary values using 
# a loop, making it easier to manage larger dictionaries dynamically. 
# This method is especially useful when dealing with dictionaries that 
# have many entries, as it reduces redundancy in your code.
# The output looks the same but the code differs a lot!

library = {
    "name": "Pulp Fiction",
    "year": 1994,
    "director": "Quentin Tarantino",
    "genre": "Crime, Drama",
    "duration": 154
}

print("Without a loop:\n")

print(library["name"])
print(library["year"])
print(library["director"])
print(library["genre"])
print(library["duration"])

print("\nWith a loop:\n")
for key in library:
    print(library[key])
