
def ternarySearch(l, r, x, arr):
    while l <= r:
        mid1 = l + (r-l)//3
        mid2 = r - (r-l)//3
        if x == arr[mid1]:
            return mid1
        elif x == arr[mid2]:
            return mid2
        elif x < arr[mid1]:
            return ternarySearch(l, mid1-1, x, arr)
        elif x > arr[mid2]:
            return ternarySearch(mid2+1, r, x , arr)
        else:
            return ternarySearch(mid1+1, mid2-1, x, arr)
    return -1














# Driver code
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# number which is searched
x = 20
# The left index is
l = 0
# The right index is
r = len(arr)-1

# function calling
result = ternarySearch(l, r, x , arr)

print("Searching element present at index:", result)