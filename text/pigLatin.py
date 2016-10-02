# Pig Latin
# Pig Latin is a game of alterations played on the English language game. To create the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay). 

while(True):
    print("\n\t\tWelcome to Pig Latin\n")
    str = input("Enter a word/sentence to convert it to Pig latin: ")
    print(">>>", end=" ")
    for word in str.split():
        print(word[1:]+word[0]+"ay", end=" ")

    input("\n\nPress enter to continue...")

