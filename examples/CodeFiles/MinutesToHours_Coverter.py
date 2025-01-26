def time_conversion(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours}h {remaining_minutes}minutes"


input_time = int(input("Enter minutes as an integer: "))
print(time_conversion(input_time))