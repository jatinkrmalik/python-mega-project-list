# Count words in a string
# Counts the number of individual words in a string. For added complexity read these strings in from a text file and generate a summary.

import operator # to sort the dictionary

def wordSummary(str):
    wordDict = {}
    initVal = 1
    for word in str.split():
        try: # to check if word already exists in the dictionary
            wordDict[word] += 1
            continue
        except KeyError: # to add a new word in dictionary
            wordDict[word] = initVal
    wordDict = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True) # sorting the dictionary using operator lib and converting it to a tuple

    print("\n>>> Word summary:\n")
    for word in wordDict: # pretty print
        print(word[1],"count(s)\t: ", word[0])

print("\n\t\tWord counter!\n")
str = input("Enter a string to generate word summary: ")
wordSummary(str)
print() # asthetics

# To do:
# Read from a file

