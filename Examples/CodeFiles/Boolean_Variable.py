# This small program demonstrates the usage of boolean variable by checking
# if the number given by the user is divisible by 15. The program would
# work without good_division variable, but it is used just to demonstrate
# how booleans work.

number = int(input("Please enter a number: "))

good_division = True
if number % 15 != 0:
    good_division = False
    print("The number is not suitable.")
elif good_division:
    print("The number is suitable.")
