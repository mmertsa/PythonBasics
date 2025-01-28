# This file contains all functions that are used in other examples.
# It is imported at the beginning of every example to provide access
# to these functions, enabling modular and reusable code throughout the project.

import math

# Example 1
def show_personal_info():
    print("Matti Meikäläinen")  
    print("Rovaniemi")          
    print("Nurse")              

# Example 2
def count_seconds(hours, minutes, seconds):
    total_seconds = (hours * 3600) + (minutes * 60) + seconds  
    return total_seconds

# Example 3
def magazine_serial_check(serial):
    if len(serial) < 9 or serial[4] != "-":
        return "Invalid ISSN."  
    elif serial[4] == "-":
        cleaned_serial = serial.replace("-", "")
        if len(cleaned_serial) == 8 and cleaned_serial.isdigit():
            return "Valid ISSN."
        else:
            return "Invalid ISSN."

# Example 4
def show_numbered_list(title, data):
    print(title) 
    for line_number, name in enumerate(data, start=1):
        print(line_number, ".", name)  
    return title

# Example 5
def box_volume(width, height, depth):
    volume = width * height * depth  
    return round(volume, 2)           

def ball_volume(radius):
    volume = (4 * math.pi * radius ** 3) / 3  
    return round(volume, 2)                   

def pipe_volume(radius, length):
    volume = math.pi * radius ** 2 * length  
    return round(volume, 2)                   