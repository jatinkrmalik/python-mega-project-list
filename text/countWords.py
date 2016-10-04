# Count words in a string
# Counts the number of individual words in a string. For added complexity read these strings in from a text file and generate a summary.

def wordSummary(str):
    wordDict = {}
    initVal = 1
    for word in str.split():
        try: # to check if word already exists in the dictionary
            wordDict[word] += 1
            continue
        except KeyError: # to add a new word in dictionary
            wordDict[word] = initVal
    print("\n>>> Word summary:\n\n",wordDict,"\n")

print("\n\t\tWord counter!\n")
str = input("Enter a string to generate word summary: ")
wordSummary(str)

# To do:
# Print dictionary in descending order
# Read from a file

