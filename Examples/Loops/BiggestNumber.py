biggest_number = []

for i in range(5):
    while True:
        try:
            number = int(input("Enter a positive integer:\n"))
            if number > 0:
                biggest_number.append(number)
                break
            elif number <= 0:
                print("The number must be a positive integer.")
                continue
        except ValueError:
            print("Valid input. Please enter a positive iteger.")

if biggest_number:
    print(f"The biggest number user entered: {max(biggest_number)}")
else:
    print("The user did not enter any positive numbers.")
