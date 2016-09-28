# Sorting
# Implement two types of sorting algorithms: Merge sort and bubble sort.

def mergeSort(numList):
    # Do the magic here

def bubbleSort(numList):
    # Do the magic here

while(True):
    print("\n\t\tSorting")
    numList = input("Please enter the list of numbers seprated by comma ',': ").split(",")
    ch = input("Perform :\n(M)erge sort\n(B)ubble sort\n(Q)uit\n").lower()
    
    if ch == 'm':
        mergeSort(numList)

    elif ch == 'b':
        bubbleSort(numList)

    elif ch == 'q':
        break

    else
        print("\nWrong choice entered, please try again.")

