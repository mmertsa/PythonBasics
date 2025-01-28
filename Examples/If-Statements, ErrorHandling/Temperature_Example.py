# Prompt the user to input the day's temperature
temperature = float(input("Enter the day's temperature: "))

# Determine the temperature range and print the corresponding description
if 0 <= temperature <= 10:
    print("COLD")
elif 11 <= temperature <= 15:
    print("CHILLY")
elif 16 <= temperature <= 20:
    print("FAIRLY WARM")
elif 21 <= temperature <= 25:
    print("WARM")
elif 26 <= temperature <= 30:
    print("HEAT")
elif temperature > 30:
    print("It is way too hot.")
else:
    print("It is freezing!")
