# Calculate the portions of actual income and taxes

def take_home(income, tax_rate):
    net_income = income * (100 - tax_rate) / 100
    return net_income

def tax_amount(income, tax_rate):
    taxes = income - take_home(income, tax_rate)
    return taxes

# Input from user
income1 = float(input("Enter your monthly salary: "))
taxes_rate = float(input("Enter your tax percentage: "))

# Output statements
print("Take-home amount: ", take_home(income1, taxes_rate), "€")
print("Taxes: ", tax_amount(income1, taxes_rate), "€")