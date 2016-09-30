# Sorting
# Implement two types of sorting algorithms: Merge sort and bubble sort.

def mergeSort(numList):
    if len(numList)>1:
        mid = len(numList)//2
        leftList = numList[:mid]
        rightList = numList[mid:]

        mergeSort(leftList)
        mergeSort(rightList)

        i = 0
        j = 0
        k = 0

        while i<len(leftList) and j <len(rightList):
            if leftList[i]<rightList[j]:
                numList[k] = leftList[i]
                i += 1
            else:
                numList[k] = rightList[j]
                j += 1
            k += 1

        while i<len(leftList):
            numList[k] = leftList[i]
            i += 1
            k += 1

        while j<len(rightList):
            numList[k] = rightList[j]
            j += 1
            k += 1
        return numList

def bubbleSort(numList):
    # Do the magic here
    ps = 0
    while(True):
        swpC = 0
        for i in range(len(numList)-1):
            j = i + 1
            if int(numList[j])<int(numList[i]):
                numList[i], numList[j] = numList[j], numList[i]
                swpC += 1
        ps += 1
        print("\n>>>After "+str(ps)+" passes, list is :")
        print(numList)

        if swpC == 0:
            print("\n***List is now sorted in "+str(ps)+" passes!***")
            break
    return numList

while(True):
    print("\n\t\tSorting")
    numList = input("Please enter the list of numbers seprated by comma ',': ").split(",")
    print("\n>>>Perform :\n(M)erge sort\n(B)ubble sort\n(Q)uit")
    ch = input("\nEnter your choice: ").lower()
    
    if ch == 'm':
        print(mergeSort(numList))

    elif ch == 'b':
        print(bubbleSort(numList))

    elif ch == 'q':
        break

    else:
        print("\nWrong choice entered, please try again.")

    input("\nPress enter to continue...")

