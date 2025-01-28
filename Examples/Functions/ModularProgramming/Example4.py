# Example4

import functions

participant_list = input("Enter the event participants separated by commas:\n")  # Prompts user to input participants
print()

names = participant_list.split(",")  # Splits the input string by commas into a list
names = [name.strip() for name in names]  # Removes any leading/trailing whitespace from each name

# First call
title_1 = "Registration order:"
functions.show_numbered_list(title_1, names)  # Displays the list of names in the order they were provided
print()

# Second call
title_2 = "Alphabetical order by first name:"
alphabetical_names = sorted(names)  # Sorts the names alphabetically
functions.show_numbered_list(title_2, alphabetical_names)  # Displays the sorted list
print()

# Third call
title_3 = "Alphabetical order by last name:"
names = [" ".join(reversed(name.split(" "))) for name in names]  # Reverses the name parts to sort by last name
alphabetical_names_2 = sorted(names)  # Sorts the reversed names
functions.show_numbered_list(title_3, alphabetical_names_2)  # Displays the sorted list by last name
