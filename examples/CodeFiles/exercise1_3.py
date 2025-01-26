def consumption(distance):
    fuel = (6.5 * distance) / 100
    return round(fuel, 1)

distanceinput = int(input("Enter the distance: "))
print(consumption(distanceinput), "l/100km")
