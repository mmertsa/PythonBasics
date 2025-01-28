# Prompt the user to input the week's working hours and hourly wage
hours_worked = float(input("Enter the week's working hours: "))
hourly_wage = float(input("Enter your hourly wage: "))

# Define functions to calculate regular and overtime pay
def calculate_pay(hours, hourly_wage):
    return hours * hourly_wage

def calculate_overtime_pay(hours, hourly_wage):
    regular_pay = hourly_wage * 40
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * hourly_wage * 1.5
    return regular_pay + overtime_pay

# Determine whether the user worked regular or overtime hours and print the corresponding total pay
if hours_worked <= 40:
    print("Your week's earnings are: ", calculate_pay(hours_worked, hourly_wage), "€")
elif hours_worked > 40:
    print("Your week's earnings are: ", calculate_overtime_pay(hours_worked, hourly_wage), "€")