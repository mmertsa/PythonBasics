import math

a = int(input("Enter the value of variable a:\n"))
b = int(input("Enter the value of variable b:\n"))
c = int(input("Enter the value of variable c:\n"))

discriminant = b**2 - 4*a*c

if discriminant < 0:
    print("The equation has no real solutions.")
elif discriminant == 0:
    x = (-b + math.sqrt(discriminant)) / (2 * a)
    print("The equation has one real solution: ", x)
else:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print("The equation has two distinct real solutions: ", round(x1, 2), " and ", round(x2,2))
