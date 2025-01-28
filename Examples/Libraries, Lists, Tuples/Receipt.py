shopcart = [
    {"name": "Lokki lamp", "price": 349.9},
    {"name": "Stockholm rug", "price": 129.9},
    {"name": "Malm chest of drawers", "price": 49.9},
    {"name": "Vienna sofa bed", "price": 799.9},
    {"name": "Ritz armchair", "price": 369.9}
]

print("Receipt of purchases: ")

# Loop through each item in the shopping cart and print the item name
for item in shopcart:
    print("-", item["name"])

print()

# Initialize a variable to hold the sum of prices
total = 0

# Loop through the shopping cart to calculate the total price
for item in shopcart:
    total += item["price"]


print(f"Total: {total} €.")
print("Welcome back!")
