# Example5

import functions

while True:
    try:
        choice = float(input("Select an operation (1-3), 0 to exit the program:\n"))  # Prompts the user to select an operation
        if choice == 0:
            print("Thank you for using the program!")  # Exits the program
            break
        elif choice < 0 or choice > 3:
            print("Input must be 0, 1, 2, or 3.")  # Validates the input
            print()
        elif choice == 1:
            width = float(input("Enter the box width:\n"))  # Gets the box dimensions from the user
            height = float(input("Enter the box height:\n"))
            depth = float(input("Enter the box depth:\n"))
            print("Box volume:", functions.box_volume(width, height, depth), "m³")  # Calculates and displays the box volume
            print()
        elif choice == 2:
            radius = float(input("Enter the sphere radius:\n"))  # Gets the sphere radius from the user
            print("Sphere volume:", functions.ball_volume(radius), "m³")  # Calculates and displays the sphere volume
            print()
        elif choice == 3:
            radius = float(input("Enter the pipe radius:\n"))  # Gets the pipe dimensions from the user
            length = float(input("Enter the pipe length:\n"))
            print("Pipe volume:", functions.pipe_volume(radius, length), "m³")  # Calculates and displays the pipe volume
            print()
    except ValueError:
        print("Input must be a number.")  # Handles non-numeric input
        print()
