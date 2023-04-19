# Palindrome Checker in Python

# Get user input for a word or phrase
word = input("Enter a word or phrase: ")

# Remove spaces and convert to lowercase
word = word.replace(" ", "").lower()

# Reverse the word
reversed_word = word[::-1]

# Check if the word is a palindrome
if word == reversed_word:
    print("Yes, it is a palindrome!")
else:
    print("No, it is not a palindrome.")
