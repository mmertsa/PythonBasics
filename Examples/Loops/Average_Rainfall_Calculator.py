# By using for loop this small program calculates the average rainfall for
# the year

total = 0
for i in range(12):
    rain = int(input("Enter the monthly rainfall: "))
    total = total + rain

rainfall_average = round(total / 12, 1)
print("The average rainfall for the year is: ", rainfall_average, "mm")
