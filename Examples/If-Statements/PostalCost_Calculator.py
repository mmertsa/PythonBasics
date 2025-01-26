# A postal cost calculator that determines the price for sending a letter or 
# a package based on weight and other conditions. 
# This code could be improved majorly by adding functions etc.

import math

# Initialize variables
choice = ()
letter_weight = ()
package_weight = ()

while True:
    try:
        choice = (input("Are you sending a letter or a package?\nPlease respond with either 'letter' or 'package': "))
    except NameError:
        print("Error encountered.")
    # Validate input
    if choice.lower() != "letter" and choice.lower() != "package":
        print("Please respond with either 'letter' or 'package'.")
        continue
    else:
        break

if choice.lower() == "letter":
    while True:
        try:
            letter_weight = float(input("Enter the weight of the letter in grams: "))
        except ValueError:
            print("Weight must be a number.")
            continue

        if letter_weight <= 0:
            print("The letter must weigh more than zero grams.")
        else:
            break

    # Determine price based on weight
    if 0 < letter_weight < 200:
        print("Price: 50 cents")
    elif 200 <= letter_weight < 500:
        price = (math.floor(letter_weight / 100) * 4) + 50
        print("Price: ", price, "cents")
    elif letter_weight >= 500:
        fits_in_mailbox = (input("Does the letter fit in the mailbox?\nAnswer yes or no: "))
        if fits_in_mailbox.lower() == "no":
            price = (math.floor(letter_weight / 100) * 7) + 50 + 200
            print(price / 100, "€")
        elif fits_in_mailbox.lower() == "yes":
            price = (math.floor(letter_weight / 100) * 7) + 50
            print(price / 100, "€")
    else:
        print("Please respond with yes or no.")

if choice.lower() == "package":
    while True:
        try:
            package_weight = float(input("Enter the weight of the package: "))
        except ValueError:
            print("Weight must be a number.")
            continue
        if package_weight <= 0:
            print("The package must weigh more than zero.")
            continue
        else:
            break

    # Determine price based on weight for packages
    if 0 < package_weight < 200:
        print("Price: 2 euros")
    elif 200 <= package_weight < 500:
        price = (math.floor(package_weight / 100) * 8) + 200
        print("Price: ", price / 100, "€")
    else:
        price = (math.floor(package_weight / 100) * 14) + 200
        print("Price: ", price / 100, "€")
