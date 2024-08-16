
# defining the function
def selectionSort(arr):
    # first store the length in a variable
    n = len(arr)
    # start looping
    for i in range(n):
        ## to store the value of minimum index
        print("The value of i is ", i)
        min_index = i
        for j in range(i+1, n):
            print("The value of I in j loop is ", i)
            if arr[j] < arr[min_index]:
                min_index = j
            # we perform the swap here  of the element i and min_index
        arr[i],arr[min_index] = arr[min_index],arr[i]

    return arr











# Driver code
arr = [30, 38, 45, 79, 19, 27, 29]
result = selectionSort(arr)

# Printing the result
print("The result of the selection sort is ", result)