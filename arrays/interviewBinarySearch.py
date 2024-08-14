





def binarySearch(arr, i, j, x):
   """
   Perform binary search on a sorted array to find the index of a given element.
   
   Args:
   arr (list): A sorted list of elements.
   i (int): Starting index of the search range.
   j (int): Ending index of the search range.
   x: The element to search for in the array.
   
   Returns:
   int: The index of the element x in the array if found, otherwise -1.
   """

   while i < j:
        mid = i + (j-i)//2
        if(arr[mid] == x):
            return mid
        elif(arr[mid]<x):
            i  = mid + 1
        else:
            j = mid-1
   return -1 # no element found


# def linearSearch(arr, i, j, x):
#     """
#     Perform linear search on an array to find the index of a given element within a specified range.
    
#     Args:
#     arr (list): A list of elements.
#     i (int): Starting index of the search range.
#     j (int): Ending index of the search range.
#     x: The element to search for in the array.
    
#     Returns:
#     int: The index of the element x in the array if found, otherwise -1.
#     """
    
#     for index in range(i, j + 1):
#         if arr[index] == x:
#             return index
#     return -1  # element not found

# Driver code
# arr = [20, -30, 10, 5, 7, 0, 29, 29, 29, 29]
# i = 0
# j = len(arr) - 1
# x = 29
# result = linearSearch(arr, i, j, x)
# print(result)


# Driver code
arr = [20, -30, 10, 5, 7, 0, 29, 29, 29, 29]
# arr.sort()
print(arr)
i=0
j=len(arr)-1
x=29
result = binarySearch(arr, i, j, x)

print(f"The {x} is found at the index {result}")
