# This very simple program demostartes how if-elif stucture works
# It compares two given number using conditional statements (if-elif)

# Prompt the user to input two integers
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

# Compare the two numbers and print the larger one or their equality
if first_number > second_number:
    print("Larger number: ", first_number)
elif second_number > first_number:
    print("Larger number: ", second_number)
elif first_number == second_number:
    print("The numbers are equal.")
    