# A short program that checks if the year the user entered matches any codes
# in the list and prints the codes matching the year.

codes = ["T1565_2020",
         "T2432_2019",
         "T8551_2018",
         "T3342_2019",
         "T9814_2018",
         "T7733_2020"]

year = input("Enter the year:\n")
print()

found = False  # Variable to track if any code matches the year

for code in codes:
    if year in code:
        new_codes = code.split("_")
        print(new_codes[0])
        found = True  # Set the flag to True if a match is found
        
if not found:
    print("No codes matching the year.")
