# This small program demonstrates string manipulation, user interaction, 
# and basic text formatting in Python.

# Initial text that contains a sentence
text = ("The quick brown fox jumps over the lazy dog.\n"
        "That sentence contains every letter in the English alphabet. Isn't that neat!\n")

# Print the original text
print(text)

# Replace the word "fox" with "duck"
new_text = text.replace("fox", "duck")
print(new_text)

# Ask user for a word to remove from the modified text
word_to_remove = input("Please enter a word to remove:\n")
new_text1 = new_text.replace(word_to_remove, "")

# Check if the word to remove is in the original text
if word_to_remove in text:
    print(new_text1)
else:
    print("Word not found.")

# Calculate the length of the modified text without the removed word
length = len(new_text1)
word_count = len(new_text1.split())  # Count words in the modified text
print("Words: ", word_count)
print("Characters: ", length)

# Replace periods with newlines in the modified text
new_text2 = new_text1.replace(".", "\n")
print("\n", new_text2)

# Check length of the new text and print accordingly
if len(new_text2) > 20:
    # If the text is longer than 20 characters, print the first 20 characters followed by "..."
    print(new_text2[:20], "...")
else:
    # If the text is 20 or fewer characters, print the text as is
    print(new_text2)
