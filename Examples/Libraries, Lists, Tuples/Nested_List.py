# A nested list

fruits = ["apple", "pear", "banana"]
berries = ["strawberry", "blueberry", "blackberry"]
vegetables = ["carrot", "kale", "cucumber"]

inventory = [fruits, berries, vegetables]

for listat in inventory:
    for asiat in listat:
     print(asiat)
