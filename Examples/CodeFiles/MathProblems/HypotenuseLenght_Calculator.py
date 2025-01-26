# This function calculates the length of the hypotenuse of a triangle given its sides.
# In this code negative or zero inputs from user are noted and handled
import math

def length_of_hypotenuse(side1, side2):
    return round(math.sqrt((side1 ** 2) + (side2 ** 2)), 2)
    
try:
    cathetus1 = float(input("Enter the length of the first cathetus of the triangle: "))
    cathetus2 = float(input("Enter the length of the second cathetus of the triangle: "))
    if cathetus1 <= 0 or cathetus2 <= 0 :
        print("Lenght of a cathetus cannot be zero or negative!")
    else:
        print("Length of the hypotenuse: ", length_of_hypotenuse(cathetus1, cathetus2), "m")
except ValueError:
    print("Input must be a number.")

