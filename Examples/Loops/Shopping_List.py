# A list containing fruits and vegetables
basket = ["apple", "banana", "cherry",
          "carrot", "potato", "tomato", "cabbage"]

# Prompt the user to enter a word
# #The program then iterates over each item in the basket
# If the entered word matches an item in the basket, it prints 
# "Word found!" and exits the loop
# If the word doesn't match, it prints "Searching..."
word = input("Enter a word:\n")
for i in range(len(basket)):
    if word == basket[i]:
        print("Word found!")
        break
    else:
        print("Searching...")

# Prompt the user to enter a word or a number
# If the search_input is not a digit (indicating it is a word),
# the program iterates through all items in the basket and prints 
# each item except the one that matches search_input
search_input = input("Enter a word or number:\n")
if not search_input.isdigit():
    for item in basket:
        if item == search_input:
            continue
        print(item)
        
# If the search_input is a digit, the input is converted to an integer.
# If number is within valid range, all items in the basket except for the one 
# located at the index (number - 1) are printed
else:
    number = int(search_input)
    if 1 <= number <= len(basket):  # Check if the number is within valid range
        for item in basket:
            if item == basket[number - 1]:
                continue
            print(item)
    else:
        print("Number out of range.")
