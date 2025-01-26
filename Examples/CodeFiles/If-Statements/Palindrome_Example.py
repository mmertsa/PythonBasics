# Get input from the user
text = input("Please enter a sentence: ")

# Reverse the input text
reversed_text = text[::-1]

# Check if the input text is empty
if len(text) == 0:
    print("The text you provided is empty.")
# Check if the reversed text is equal to the original text
elif reversed_text == text:
    print(reversed_text)
    print("Palindrome: YES")
# If the reversed text is not equal to the original text
elif reversed_text != text:
    print(text[::-1], "\nPalindrome: NO")
