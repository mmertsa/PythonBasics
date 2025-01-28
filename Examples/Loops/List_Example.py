# This example also shows the usage of list and how to loop throug it

cities = ["Rooma", "Ateena", "Tukholma", "Lontoo", "Dublin", "Pariisi"]

for line_number, line in enumerate(cities, start=1):
    print(line_number, ":", line)
