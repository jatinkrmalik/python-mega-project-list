# Number Names
# Show how to spell out a number in English. You can use a preexisting implementation or roll your own, but you should support inputs up to at least one million

def spellMe(num):
    singles = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    tensInitial = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Fourty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    tens_power = ["", "", "Hundred", "Thousand"]

    while(True):
        
        # To-DO: Implement logic to name numbers upto a million

        if(num<9999): # For now till 9999 only
            if(num>999):
                temp = num//1000
                num = num%1000
                print(str(singles[temp])+" "+str(tens_power[3]), end=" ")

            if(num>99):
                temp = num//100
                num = num%100
                print(str(singles[temp])+" "+str(tens_power[2]), end=" ")

            if(num>9 and num<20): # For numbers 10 to 19
                temp = num%10
                print(str(tensInitial[temp]), end=" ")
                break
            
            elif(num>=20 and num<=99): # For rest of 2 digit numbers
                temp = num//10
                print(str(tens[temp]), end=" ")
            
            if(num%10 != 0): # To avoid 20 = Twenty Zero, 30 = Thirty Zero
                num = num%10
                temp = num
                print(str(singles[temp]), end=" ")
                break
            
            elif(num==0): # For Zero, because Aryabhata!
                print(str(singles[0]), end=" ")

        else:
            print("Numbers above 9999 not supported")

        break # because everything has to end one day -_-

while(True):
    print("\n\t\tWelcome to Number names\n")
    num = int(input("Enter the number to name: "))
    print("\nYour answer is: ", end="")
    spellMe(num)
    input("\n\nPress enter to continue...")
