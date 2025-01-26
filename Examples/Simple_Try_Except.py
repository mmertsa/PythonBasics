try:
    # Prompt the user to enter the first number
    number1 = float(input("Please enter the first number: "))
    # Prompt the user to enter the second number
    number2 = float(input("Please enter the second number: "))
    # Perform the division
    calculation = number1 / number2
    # Print the result of the division
    print(calculation)
except ValueError:
    # Handle the case where the input cannot be converted to a float
    print("Invalid format!")
except ZeroDivisionError:
    # Handle the case where division by zero is attempted
    print("Cannot divide by zero.")
