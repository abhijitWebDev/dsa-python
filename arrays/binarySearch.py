
# Implementation of binary search
# First the array should be an sorted array

# def binarySearch(arr, i, j, x):
#     while i<=j:
#         mid = i + (j-i)//2
#         if arr[mid] == x:
#             return mid
#         elif arr[mid]<x:
#             # using recursion , calling binarySearch again with different parameteres
#             return binarySearch(arr, mid+1, j, x)
#         else:
#             return binarySearch(arr, i, mid-1, x)
#     return -1 # The searching element is not present in the array

def binarySearch(arr, i, j, x):
    while i<=j:
        mid = i + (j-i)//2
        if arr[mid] == x:
            return mid
        elif arr[mid]<x:
           # Update the parameter, value of i should be mid+1
            i = mid+1
        else:
            # Update the parameter, value of j should be mid-1
            i = mid-1
    return -1 # The searching element is not present in the array






# Driver code
arr = [1, 3, 4, 6, 7, 10, 20, 40, 50, 60]
x = 50
i = 0
j = len(arr)-1
## function call
result = binarySearch(arr, i, j, x)
print("Searching element present is", result)