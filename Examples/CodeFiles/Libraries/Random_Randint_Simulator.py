# This small program demonstrates the use of built-in module called random
import random

# Print a randomly generated number between 1 and 10 using random.randint
print("Random number: ", random.randint(1, 10))

# Generate two random sides for a rectangle
side1 = random.randint(2, 10)
side2 = random.randint(2, 10)
area = side1 * side2

# Print the randomly generated sides and the calculated area
print("Random 1st side: ", side1)
print("Random 2nd side: ", side2)
print("Calculated area from the random sides: ", area)
