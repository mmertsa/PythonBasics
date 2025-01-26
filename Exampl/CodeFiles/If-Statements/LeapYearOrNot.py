# A simple program that checks whether a given year is a leap year or not.

year = int(input("Enter a year: "))

if year % 4 == 0 and year % 100 != 0:
    print("Leap year.")
elif year % 400 == 0:
    print("Leap year.")
else:
    print("Not a leap year.")
