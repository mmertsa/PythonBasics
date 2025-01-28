# This small program serves as a simple month lookup based on the user's input.
# It utilizes tuple as a way to storage data

months = ("January", "February", "March", "April", "May",
          "June", "July", "August", "September", "October", "November", "December")

month_number = int(input("Enter the month's number: "))
if month_number <= 0:
    print("The month cannot be less than one!")
elif month_number > 12:
    print("There are only 12 months!")
else:
    print(months[month_number - 1])
