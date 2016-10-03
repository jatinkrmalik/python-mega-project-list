# Check if Palindrome
# Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like "racecar"

print("\n\t\tPalindrome checker\n")
word = input("Enter a word to check palindrome for: ")

word = word.lower() # to avoid case complications

if word == word[::-1]:
    print("Yes *", word, "* is a palindrome!")

else:
    print("Nope *", word, "* is not a palindrome!")

print()
