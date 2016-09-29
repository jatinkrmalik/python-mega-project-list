# Sorting
# Implement two types of sorting algorithms: Merge sort and bubble sort.

def mergeSort(numList):
    print("Do the magic here")
    
def bubbleSort(numList):
    # Do the magic here
    ps = 0
    while(True):
        swpC = 0
        for i in range(len(numList)-1):
            j = i + 1
            if numList[j]<numList[i]:
                numList[i], numList[j] = numList[j], numList[i]
                swpC += 1
        ps += 1
        print("\n>>>After "+str(ps)+" passes, list is :\n")
        print(numList)

        if swpC == 0:
            print("\n***List is now sorted!***")
            break
    return numList

while(True):
    print("\n\t\tSorting")
    numList = input("Please enter the list of numbers seprated by comma ',': ").split(",")
    ch = input("Perform :\n(M)erge sort\n(B)ubble sort\n(Q)uit\n").lower()
    
    if ch == 'm':
        mergeSort(numList)

    elif ch == 'b':
        print(bubbleSort(numList))

    elif ch == 'q':
        break

    else:
        print("\nWrong choice entered, please try again.")

    input("\nPress enter to continue...")

