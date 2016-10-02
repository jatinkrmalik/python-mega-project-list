# Count vowels
# Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.


print("\n\t\tLet's count the vowels\n")
str = input("Enter a string to count the vowels: ")

vowels = {"a":0, "e":0, "i":0, "o":0, "u":0}

for alpha in str.lower():
    if alpha == "a":
        vowels["a"] += 1

    elif alpha == "e":
            vowels["e"] += 1

    elif alpha == "i":
            vowels["i"] += 1

    elif alpha == "o":
            vowels["o"] += 1

    elif alpha == "u":
            vowels["u"] += 1

print(vowels)




    

