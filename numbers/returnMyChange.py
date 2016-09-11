# Change Return Program
# The user enters a cost and then the amount of money given. The program will figure out the needed change in INR currency


def calcChange(tC, aR):
    balanceAmount = aR-tC
    changeList = [1000,500,100,50,20,10,5,2,1] # Currency denomination of Indian Rupees

    if balanceAmount==0:
        print("Recieved exact amount, no change needs to be returned")

    else:
        print("Please return the change as follows:")
        for change in changeList:
            while balanceAmount>=change:
                print(change, end=" ")
                balanceAmount = balanceAmount-change
            if balanceAmount==0:
                print("\n")
                return 0
            else:
                continue

print("\n\t\tChange calculator\n")
totalCost = int(input("Enter the total cost of the bill: "))
amountRecvd = int(input("Enter the amount recieved: "))

calcChange(totalCost, amountRecvd)


