# At the beginnig math library is imported and later pi-function
# is utilized in code using math.pi
import math

def prism_volume(side1, side2, side3):
    return round(side1 * side2 * side3, 1)

side_1 = float(input("Enter the length of the first side of the prism:\n"))
side_2 = float(input("Enter the length of the second side of the prism:\n"))
side_3 = float(input("Enter the length of the third side of the prism:\n"))

print("Prism volume: ", prism_volume(side_1, side_2, side_3), "m³")

def sphere_volume(radius):
    return round((4 / 3) * math.pi * radius ** 3, 2)

sphere_radius = float(input("Enter the radius of the sphere:\n"))
print("Sphere volume: ", sphere_volume(sphere_radius), "m³")