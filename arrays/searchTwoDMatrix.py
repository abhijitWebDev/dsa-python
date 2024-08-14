
## function difinition
def searchInSortedMatrix(matrix, target):
    # here we get no of rows
    m = len(matrix)
    if m == 0:
        return False
    
    # here we get no of columns
    n = len(matrix[0])

    left, right = 0, m * n-1

    while(left <= right):
        mid = left + (right - left) //2
        mid_element = matrix[mid//n][mid%n]

        if target == mid_element:
            return True
        elif target < mid_element:
            right = mid - 1
        else:
            left = mid + 1
    return False








# Driver code
matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34,60]]
target = 55
# function calling 
result = searchInSortedMatrix(matrix, target)
print(result)