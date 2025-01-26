# This function calculates the total fuel consumption based on two types of 
# driving: highway driving and city driving. Fuel consumption for highway 
# driving is estimated at 5.1/100km and for city driving at 7.5/100km. These
# are hardcoded inside the function.

def fuel_consumption(highway_distance, city_distance):
    consumption_highway = (5.1 * highway_distance) / 100
    consumption_city = (7.5 * city_distance) / 100
    return round(consumption_highway + consumption_city, 2)

# Input from user
driving_distance = float(input("Highway distance in kilometers: "))
city_distance = float(input("City distance in kilometers: "))

# Output statement
print("Fuel consumption: ", fuel_consumption(driving_distance, city_distance), "l")
