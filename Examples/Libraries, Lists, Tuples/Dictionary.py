# how to access data in a dictionary

cafe = {
     "name": "Imaginary Cafe Oy",
     "website": "https://edu.frostbit.fi/sites/cafe",
     "categories": [
         "cafe",
         "tea",
         "lunch",
         "breakfast"
        ],
     "location": {
         "city": "Rovaniemi",
         "address": "Homeroad 1",
         "zip_code": "96200"
     }
}

print(cafe["name"], "\n", cafe["location"]["address"], "\n",
      cafe["location"]["zip_code"])
print()
print(cafe["website"])
print("Palvelut:", ', '.join(cafe["categories"]))
