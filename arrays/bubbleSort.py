"""
Sorts a list of elements in ascending order using the bubble sort algorithm.

Parameters:
arr (list): A list of elements to be sorted.

Returns:
list: The sorted list in ascending order.

The bubble sort algorithm repeatedly steps through the list, compares adjacent
elements and swaps them if they are in the wrong order. The pass through the
list is repeated until the list is sorted.
"""



def bubbleSort(arr):


    n= len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
    return arr

    

#Driver code
arr = [70, 20, 50, 30, 90, 5, 15]
# arr = [1 , 2, 3, 4, 5, 6, 7, 8]


result = bubbleSort(arr)
print("After applying the bubblesort the sorted array will be", result)