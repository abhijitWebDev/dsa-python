# Implementation of insertion sort

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1

        # now checking the value of j should be grater than 0 , using while loop
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]

            j = j - 1
        arr[j+1] = key
    return arr










# Driver code
arr= [9, 5, 1, 4, 3]

# storing the value or sorted value in result
result = insertionSort(arr)

# Printing result
print("The result of insertion algo is", result)