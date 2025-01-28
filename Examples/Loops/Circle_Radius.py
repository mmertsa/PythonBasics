# Small program that calculates the area of a circle based on a user-provided radius.

import math

while True:
    try:
        radius = float(input("Enter the radius: "))
        area = math.pi * radius ** 2
        print("The area of the circle is: ", round(area, 2))
    except ValueError:
        print("The radius must be a number: ")
        continue

    while True:
        try:
            continue_program = input("Do you want to continue? (y/n):\n").lower()
            if continue_program == "y":
                break
            elif continue_program == "n":
                exit()
            else:
                print("Invalid input. Please enter y or n.")
        except Exception as e:
            print("An unexpected error occurred:", str(e))
