# Small lottery program

import random

def draw_numbers():
    # Generate a random sample of 7 unique numbers from 1 to 39
    numbers = random.sample(range(1, 40), 7)
    numbers.sort()  # Sort the numbers in ascending order
    for number in numbers:
        print(number, end=" ")  # Print each number on the same line
    print()  # Move to the next line after printing all numbers

def additional_numbers():
    # Generate a random sample of 3 unique numbers from 1 to 39
    numbers = random.sample(range(1, 40), 3)
    numbers.sort()  # Sort the additional numbers in ascending order
    for additional_number in numbers:
        print(additional_number, end=" ")  # Print each additional number on the same line
    print()  # Move to the next line after printing all additional numbers

# Main program execution
print("Lottery numbers are:")
draw_numbers()  # Call the function to draw lottery numbers
print()  # Print a blank line for spacing
print("Additional numbers are:")
additional_numbers()  # Call the function to draw additional numbers
